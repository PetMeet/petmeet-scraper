# -*- coding: utf-8 -*-

import scrapy
from protectoras_scrap.spiders.protectora_gatocan_spider.constants import *
from protectoras_scrap.models.Pet import Pet

class ProtectoraGatoCanSpider(scrapy.Spider):
    name = 'protectora_gatocan_spider'
    allowed_domains = ['www.gatocan.com']
    base_url = 'http://www.gatocan.com'
    start_urls = ['http://www.gatocan.com/ListaAnimales.php?tipo=G', 'http://www.gatocan.com/ListaAnimales.php?tipo=P']        
    
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
                        
        pet_urls = response.xpath(PROTECTORA_GATOCAN_PAGE_DETAILS_LINK_XPATH).getall()
        
        for url in pet_urls:
            yield scrapy.Request('/'.join([self.base_url, url]), callback=self.parse_pet_info, meta={'pet_type': self.__get_pet_type(response.url)})
            
    # Extract pet info
    def parse_pet_info(self, response):
        
        data = [d.replace(u'\xa0','').strip() for d in response.xpath(PROTECTORA_GATOCAN_PET_DATA_XPATH).getall()]
        
        pet = Pet()

        pet['name'] = data[0]
        pet['pet_type'] = response.meta['pet_type']
        pet['picture'] = self.__get_pet_picture_url(response)
        pet['breed'] = data[1]
        pet['sex'] = self.__get_pet_sex(data[2])
        pet['born_date'] = data[5] if pet['pet_type'] == 'CAT' else data[8]
        pet['dangerous'] = '-'
        pet['adopted'] = '-'
        pet['resource_url'] = response.url
        pet['animal_shelter'] = PROTECTORA_GATOCAN_NAME
        pet['animal_shelter_location'] = PROTECTORA_GATOCAN_LOCATION
        pet['description'] = data[7] if pet['pet_type'] == 'CAT' else data[10]

        yield pet

    # Determine the pet type based on url
    def __get_pet_type(self, url):
        return 'CAT' if 'G' in url else 'DOG'

    # Get pet picture url
    def __get_pet_picture_url(self, response):
        return '/'.join([self.base_url, response.xpath(PROTECTORA_GATOCAN_PET_PICTURE_XPATH).get()])

    # Get pet sex
    def __get_pet_sex(self, sex):
        return 'MALE' if sex == 'Macho' else 'FEMALE'