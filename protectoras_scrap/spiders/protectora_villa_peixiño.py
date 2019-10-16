# -*- coding: utf-8 -*-
import scrapy
from protectoras_scrap.models.Pet import Pet


class ProtectoraVillaPeixiñoSpider(scrapy.Spider):
    name = 'protectora_villa_peixiño'
    allowed_domains = ['villapeixiño.es']
    start_urls = ['https://villapeixiño.es/adopciones']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_pets_urls)

    ## Work in progress!
    def parse_pets_urls(self, response):
        pet_urls = response.xpath('//div[contains (@class, "col-lg-3 col-md-4 col-sm-6 mix")]//div[@class="pet-image"]')
        
        num = 0
        for url in pet_urls:
            num += 1

            adopted = url.xpath('a[@class="adoptada"]').get()
            if (adopted != None):
                print('Adopted')
            
            pre_adopted = url.xpath('a[@class="preadoptada"]').get()
            if (pre_adopted != None):
                print('Preadopted')
            
            pet_page = url.xpath('a').attrib['href']
            
            print(pet_page)
            print('\n')

        print(num)

