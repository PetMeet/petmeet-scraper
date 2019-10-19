# -*- coding: utf-8 -*-

import scrapy
import logging
import re

from protectoras_scrap.spiders.constants import *
from protectoras_scrap.models.Pet import Pet

class ProtectoraLugoSpider(scrapy.Spider):
    name = 'protectora_lugo_spider'
    allowed_domains = ['www.protectoralugo.org']
    base_url = 'http://www.protectoralugo.org'
    start_urls = ['http://www.protectoralugo.org/templates/jt001_j25/html/com_wrapper/wrapper/adopciones.php?username=&email=&nombreusuario=&password=&pruebas=']        

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_pet_urls)

    def get_next_page(self, response):
        return response.xpath(PROTECTORA_LUGO_PAGE_LINK_XPATH).get()

    def parse_pet_urls(self, response):
        
        next_page = self.get_next_page(response)

        pet_urls = response.xpath(PROTECTORA_LUGO_PAGE_DETAILS_LINK_XPATH).getall()
        
        for url in pet_urls:
            yield scrapy.Request(url, callback=self.parse_pet_info)

        if (next_page):
            yield scrapy.Request(self.base_url + next_page, callback=self.parse_pet_urls)

    def parse_pet_info(self, response):
        
        data = response.xpath(PROTECTORA_LUGO_PET_DATA_XPATH).getall()

        pet = Pet()

        pet['name'] = data[1]
        pet['pet_type'] = self.__get_pet_type(response)
        pet['picture'] = self.__get_pet_picture_url(response)
        pet['breed'] = data[2]
        pet['sex'] = self.__get_pet_sex(data[3])
        pet['born_date'] = data[4]
        pet['dangerous'] = self.__is_pet_dangerous(data[5])
        pet['adopted'] = self.__is_pet_adopted(response)
        pet['resource_url'] = response.url
        pet['animal_shelter'] = PROTECTORA_LUGO_NAME
        pet['animal_shelter_location'] = PROTECTORA_LUGO_LOCATION 
        pet['description'] = ''
        
        yield pet

    def __get_pet_type(self, response):
        return 'DOG' if 'CANINA' in response.url else 'CAT'

    def __get_pet_picture_url(self, response):
        picture_data = response.xpath(PROTECTORA_LUGO_PET_PICTURE_XPATH).get()
        picture_url = re.sub(r'[();]', '', picture_data.split('url')[1])
        return self.base_url + picture_url

    def __get_pet_sex(self, sex):
        return 'MALE' if sex == 'Macho' else 'FEMALE'

    def __is_pet_dangerous(self, dangerous):
        return 'YES' if dangerous == 'SI' else 'NO'

    def __is_pet_adopted(self, response):
        return len(response.xpath(PROTECTORA_LUGO_PET_ADOPTED_XPATH)) > 0
