# -*- coding: utf-8 -*-
import scrapy
from protectoras_scrap.models.Pet import Pet


class ProtectoraVillaPeixiñoSpider(scrapy.Spider):
    name = 'protectora_villa_peixiño'
    allowed_domains = ['xn--villapeixio-beb.es']
    start_urls = ['https://villapeixiño.es/adopciones']
    base_url = 'https://villapeixiño.es/'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_pets_urls)

    ## Work in progress!
    def parse_pets_urls(self, response):
        pet_urls = response.xpath('//div[contains (@class, "col-lg-3 col-md-4 col-sm-6 mix")]//div[@class="pet-image"]')
        
        for url in pet_urls:
            status = None

            adopted = url.xpath('a[@class="adoptada"]').get()
            if (adopted != None):
                status = 'adopted'
            
            pre_adopted = url.xpath('a[@class="preadoptada"]').get()
            if (pre_adopted != None):
                status: 'preadopted'
            
            pet_page = url.xpath('a').attrib['href']
            
            request = scrapy.Request(self.base_url + pet_page, callback= self.parse_pet_info)
            request.cb_kwargs['status'] = status

            yield request

    def parse_pet_info(self, response, status):
        #img = response.xpath('//a[@data-fancybox=""]/img').attrib['src']

        #keys = response.xpath('//ul[@class="pet-info-list"]//span/text()').extract()
        data = response.xpath('//ul[@class="pet-info-list"]/li')

        pet = Pet()

        for index, value in enumerate(data):
            if index == len(data) - 1:
                break
            
            field = value.xpath('span/text()').get()
            
            if (field == 'None'):
                field = None

            contain = value.xpath('text()').get()

            self.write_pet(pet, field, contain)

    def write_pet(self, pet, field, contain):
        if (field == 'Nombre:'):
            pet['name'] = contain
        elif (field == 'Tipo:'):
            return
        elif (field == 'Sexo:'):
            pet['sex'] = contain
        elif (field == 'Nacimiento:'):
            pet['born_date'] = contain
        elif (field == 'Edad:'):
            return
        elif (field == 'Peso:'):
            pet['adult_weight'] = contain
        elif (field == 'Esterilizado:'):
            return
        elif (field == 'Chip:'):
            return
        elif (field == 'Vacunado:'):
            return
        elif (field == 'Observaciones:'):
            return