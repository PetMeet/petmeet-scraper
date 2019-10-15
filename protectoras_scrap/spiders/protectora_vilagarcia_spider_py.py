# -*- coding: utf-8 -*-
import scrapy
import re
from protectoras_scrap.models.Pet import Pet


class ProtectoraVilagarciaSpiderPySpider(scrapy.Spider):
    name = 'protectora_vilagarcia_spider.py'
    allowed_domains = ['protectoravilagarcia.org']
    base_url = 'http://protectoravilagarcia.org/'
    start_urls = ['http://protectoravilagarcia.org/listado/']

    navigation_template = '/listado.php?p='
    index = 1
    total_pages = None

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_pets_urls)
        
    def get_total_pages(self, response):
        last_url = response.xpath("//span[@class='navPaginado']/a[@title='Última página']").attrib['href']
        return int(re.search(r'\d+', last_url).group())

    ## Work in progress!
    def parse_pets_urls(self, response):

        if not (self.total_pages):
            self.total_pages = self.get_total_pages(response)
        
        
        pet_urls = response.xpath("//div[@id='principal_contenidos']/div/a")

        for url in pet_urls:
            pet_page = url.attrib['href']
            yield scrapy.Request(self.base_url + pet_page, callback = self.parse_pet_info)

        if (self.index < self.total_pages ):
            self.index += 1 
            next_page = self.navigation_template + str(self.index) 
            yield scrapy.Request(self.base_url + next_page, callback = self.parse_pets_urls)

    def parse_pet_info(self, response):
        #Picture of the animal
        #img = response.xpath("//div[@id='contenedor_foto']/img").attrib['src']
        #print(img)

        #State of the animal
        #state = response.xpath("//strong[@class='estado estado2']/span/text()").get()
        #print(state)

        #Type of animal
        #animal = response.xpath("//dd[@class='ficha_tipo']/text()").get()
        #print(animal)

        pet = Pet()

        pet['name'] = response.xpath("//dd[@class='ficha_nombre']/text()").get()
        pet['breed'] = response.xpath("//dd[@class='ficha_raza']/text()").get()
        pet['sex'] = response.xpath("//dd[@class='ficha_sexo']/text()").get()
        pet['born_date'] = response.xpath("//dd[@class='ficha_nacimiento']/text()").get()
        pet['dangerous'] = None
        pet['aptitude'] = None
        pet['adult_weight'] = response.xpath("//dd[@class='ficha_peso']/text()").get()

        #print(pet)

