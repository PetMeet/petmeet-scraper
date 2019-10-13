# -*- coding: utf-8 -*-

import scrapy
from protectoras_scrap.models.Pet import Pet

class ProtectoraLugoSpider(scrapy.Spider):
    name = 'protectora_lugo_spider'
    allowed_domains = ['www.protectoralugo.org']
    base_url = 'http://www.protectoralugo.org/'
    start_urls = ['http://www.protectoralugo.org/templates/jt001_j25/html/com_wrapper/wrapper/adopciones.php?username=&email=&nombreusuario=&password=&pruebas=']        

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_pet_urls)

    def get_next_page(self, response):
        return response.css('#pagina_actual + a::attr(href)').extract_first()

    def parse_pet_urls(self, response):

        next_page = self.get_next_page(response)

        pet_urls = response.css('.box_listado a::attr(href)').extract()
        
        for url in pet_urls:
            yield scrapy.Request(url, callback=self.parse_pet_info)

        if (next_page):
            yield scrapy.Request(self.base_url + next_page, callback=self.parse_pet_urls)

    def parse_pet_info(self, response):
        data = response.css('div[style="width: 300px"] b::text').extract()

        pet = Pet()

        pet['name'] = data[1]
        pet['breed'] = data[2]
        pet['sex'] = data[3]
        pet['born_date'] = data[4]
        pet['dangerous'] = data[5]
        pet['aptitude'] = data[7]
        pet['adult_weight'] = data[8]

        yield pet