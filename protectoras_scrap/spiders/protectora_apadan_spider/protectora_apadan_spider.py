# -*- coding: utf-8 -*-

import scrapy
from protectoras_scrap.models.Pet import Pet
import re


def get_next_page(response):
    return response.xpath(PROTECTORA_APADAN_NEXT_PAGE_XPATH).get()

def get_pet_sex(sex):
    return 'MALE' if sex == 'Macho' else 'FEMALE'


def is_pet_adopted(adopted):
    return 'YES' if adopted == 'No' else 'NO'


class ProtectoraApadanSpider(scrapy.Spider):
    name = 'protectora_apadan_spider'
    allowed_domains = ['www.apadan.net']
    base_url = 'http://www.apadan.net'
    start_urls = ['http://www.apadan.net/nuestros_perros']

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

        pet_urls = response.xpath(PROTECTORA_APADAN_PAGE_DETAILS_LINK_XPATH).getall()

        for url in pet_urls:
            yield scrapy.Request(self.base_url + url, callback=self.parse_pet_info)

        if next_page:
            yield scrapy.Request(self.base_url + next_page, callback=self.parse_pet_urls)

    # Extract pet info
    def parse_pet_info(self, response):

        data = [re.sub(r'\s', '', d) for d in response.xpath(PROTECTORA_APADAN_PET_DATA_XPATH).getall()]

        data = list(filter(lambda element: element != '' and not re.fullmatch(r'\s+', element), data))

        pet = Pet()

        pet['name'] = re.sub(r'\s', '', response.xpath(PROTECTORA_APADAN_PET_NAME_XPATH).get())
        pet['pet_type'] = 'DOG'
        pet['picture'] = response.xpath(PROTECTORA_APADAN_PET_PICTURE_XPATH).get()
        pet['breed'] = response.xpath(PROTECTORA_APADAN_PET_BREED).get()
        pet['sex'] = get_pet_sex(data[0])
        pet['born_date'] = '-'
        pet['dangerous'] = '-'
        pet['adopted'] = is_pet_adopted(data[6])
        pet['resource_url'] = response.url
        pet['animal_shelter'] = PROTECTORA_APADAN_NAME
        pet['animal_shelter_location'] = PROTECTORA_APADAN_LOCATION
        pet['description'] = response.xpath(PROTECTORA_APADAN_PET_DESCRIPTION).get()

        yield pet
