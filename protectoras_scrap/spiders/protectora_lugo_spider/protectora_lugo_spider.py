# -*- coding: utf-8 -*-

import scrapy
import re

from protectoras_scrap.spiders.protectora_lugo_spider.constants import *
from protectoras_scrap.models.Pet import Pet
from scrapy.utils.serialize import ScrapyJSONEncoder


# Retrieve next page of pets
def get_next_page(response):
    return response.xpath(PROTECTORA_LUGO_PAGE_LINK_XPATH).get()


# Determine pet type (DOG/CAT)
def get_pet_type(response):
    return 'DOG' if 'CANINA' in response.url else 'CAT'


# Build pet picture url
def get_pet_picture_url(base_url, response):
    picture_data = response.xpath(PROTECTORA_LUGO_PET_PICTURE_XPATH).get()
    picture_url = re.sub(r'[();]', '', picture_data.split('url')[1])
    return base_url + picture_url


# Determine pet sex (MALE/FEMALE)
def get_pet_sex(sex):
    return 'MALE' if sex == 'Macho' else 'FEMALE'


# Determine if pet is dangerous (YES/NO)
def is_pet_dangerous(dangerous):
    return 'YES' if dangerous == 'SI' else 'NO'


# Determine if pet is already adopted
def is_pet_adopted(response):
    return 'YES' if (len(response.xpath(PROTECTORA_LUGO_PET_ADOPTED_XPATH)) > 0) else 'NO'


class ProtectoraLugoSpider(scrapy.Spider):
    name = 'protectora_lugo_spider'
    allowed_domains = ['www.protectoralugo.org']
    base_url = 'http://www.protectoralugo.org'
    start_urls = [
        'http://www.protectoralugo.org/templates/jt001_j25/html/com_wrapper/wrapper/adopciones.php?username=&email=&nombreusuario=&password=&pruebas=']

    # Used to easily disable pipeline during tests
    custom_settings = {
        'ITEM_PIPELINES': {
            'protectoras_scrap.pipelines.ProtectorasScrapPipeline': 300
        }
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_pet_urls)

    # Extract urls for each pet
    def parse_pet_urls(self, response):

        next_page = get_next_page(response)

        pet_urls = response.xpath(PROTECTORA_LUGO_PAGE_DETAILS_LINK_XPATH).getall()

        for url in pet_urls:
            yield scrapy.Request(url, callback=self.parse_pet_info)

        if next_page:
            yield scrapy.Request(self.base_url + next_page, callback=self.parse_pet_urls)

    # Extract pet info
    def parse_pet_info(self, response):

        data = response.xpath(PROTECTORA_LUGO_PET_DATA_XPATH).getall()

        pet = Pet()

        pet['name'] = data[1]
        pet['pet_type'] = get_pet_type(response)
        pet['picture'] = get_pet_picture_url(self.base_url, response)
        pet['breed'] = data[2]
        pet['sex'] = get_pet_sex(data[3])
        pet['born_date'] = data[4]
        pet['dangerous'] = is_pet_dangerous(data[5])
        pet['adopted'] = is_pet_adopted(response)
        pet['resource_url'] = response.url
        pet['animal_shelter'] = PROTECTORA_LUGO_NAME
        pet['animal_shelter_location'] = PROTECTORA_LUGO_LOCATION
        pet['description'] = ''

        yield pet
