import unittest
from scrapy.http import HtmlResponse, Request
import os
from scrapy.utils.serialize import ScrapyJSONEncoder
import urllib.request

from protectoras_scrap.spiders import protectora_lugo_spider
from protectoras_scrap.models.Pet import Pet
from protectoras_scrap.spiders.constants import *

class TestProtectoraLugoSpider(unittest.TestCase):
    
    HTML_SOURCE = 'resources/protectora_lugo_petdata.html'
    RESOURCE_URL = 'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14322&especie=FELINA&nombre_animal=RABUDA&pagina=1'

    def setUp(self):
        self.spider = protectora_lugo_spider.ProtectoraLugoSpider()
        self.spider.custom_settings = {}
        self.encoder = ScrapyJSONEncoder(ensure_ascii=False)
    
    def test_parse_pet_info_with_local_response(self):
        
        parsedPet = list(self.spider.parse_pet_info(self._create_response_from_file()))

        self.assertEqual(self._create_pet_model(), parsedPet[0], "Expected pet model doesn't match")
    
    def test_parse_pet_info_with_web_response(self):
        
        parsedPet = list(self.spider.parse_pet_info(self._create_response_from_web()))

        self.assertEqual(self._create_pet_model(), parsedPet[0], "Expected pet model doesn't match")

    def _create_pet_model(self):
        
        expectedPet = Pet()
        expectedPet['name'] = 'RABUDA'
        expectedPet['pet_type'] = 'CAT'
        expectedPet['picture'] = self.spider.base_url + '/cache/jw_simpleImageGallery/jwsig_cache_a5d7a332a1_14322.jpg'
        expectedPet['breed'] = 'Europeo'
        expectedPet['sex'] = 'FEMALE'
        expectedPet['born_date'] = '05/12/2018'
        expectedPet['dangerous'] = 'NO'
        expectedPet['adopted'] = False
        expectedPet['resource_url'] = self.RESOURCE_URL
        expectedPet['animal_shelter'] = PROTECTORA_LUGO_NAME
        expectedPet['animal_shelter_location'] = PROTECTORA_LUGO_LOCATION 
        expectedPet['description'] = ''

        return expectedPet

    def _create_response_from_web(self):
        web_request = urllib.request.urlopen(self.RESOURCE_URL)
        byte_response = web_request.read()
        response_content =  byte_response.decode("utf8")
        return HtmlResponse(url=self.RESOURCE_URL, body=response_content, encoding='utf-8')

    def _create_response_from_file(self):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        html = open(test_dir + '/' + self.HTML_SOURCE, 'r', encoding='utf-8')
        file_content = html.read()
        html.close()
        return HtmlResponse(url=self.RESOURCE_URL, body=file_content, encoding='utf-8')

if __name__ == '__main__':
    unittest.main()