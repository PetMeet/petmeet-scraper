import unittest
from unittest.mock import MagicMock
from scrapy.utils.serialize import ScrapyJSONEncoder

from protectoras_scrap.spiders import protectora_lugo_spider
from protectoras_scrap.models.Pet import Pet
from protectoras_scrap.spiders.constants import PROTECTORA_LUGO_LOCATION
from protectoras_scrap.spiders.constants import PROTECTORA_LUGO_NAME
from protectoras_scrap.tests.utils.response_provider import ResponseProvider

class TestProtectoraLugoSpider(unittest.TestCase):
    
    PET_LIST_HTML_SOURCE = 'resources/protectora_lugo_petlist.html'
    PET_HTML_SOURCE = 'resources/protectora_lugo_petdata.html'
    PET_RESOURCE_URL = 'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14322&especie=FELINA&nombre_animal=RABUDA&pagina=1'
    NEXT_PAGE_URL = '/templates/jt001_j25/html/com_wrapper/wrapper/adopciones.php?username=&email=&nombreusuario=&password=&pruebas=&_pagi_pg=2'

    def setUp(self):
        self.response_provider = ResponseProvider()
        self.spider = protectora_lugo_spider.ProtectoraLugoSpider()
        self.spider.custom_settings = {}

    def test_get_next_page_local_response(self):
        result = self.spider.get_next_page(self.response_provider.create_response_from_file(self.PET_LIST_HTML_SOURCE, self.spider.start_urls[0]))
        self.assertEqual(self.NEXT_PAGE_URL, result, "Expected next page doesn't match")

    def test_get_next_page_web_response(self):
        result = self.spider.get_next_page(self.response_provider.create_response_from_web(self.spider.start_urls[0]))
        self.assertEqual(self.NEXT_PAGE_URL, result, "Expected next page doesn't match")

    def test_parse_pet_urls_local_response(self):
        
        self.spider.get_next_page = MagicMock(return_value=None)

        requests = list(self.spider.parse_pet_urls(self.response_provider.create_response_from_file(self.PET_LIST_HTML_SOURCE, self.spider.start_urls[0])))
        
        requests = [ r.url for r in requests]

        self.assertListEqual(requests, self._create_expected_urls(), "Expected urls don't match")

    def test_parse_pet_urls_web_response(self):
        
        self.spider.get_next_page = MagicMock(return_value=None)

        requests = list(self.spider.parse_pet_urls(self.response_provider.create_response_from_web(self.spider.start_urls[0])))

        self.assertTrue(len(requests)==9, "Expected 9 urls but found %d" % len(requests))

    def test_parse_pet_info_with_local_response(self):
        
        parsedPet = list(self.spider.parse_pet_info(self.response_provider.create_response_from_file(self.PET_HTML_SOURCE, self.PET_RESOURCE_URL)))

        self.assertEqual(self._create_pet_model(), parsedPet[0], "Expected pet model doesn't match")
    
    def test_parse_pet_info_with_web_response(self):
        
        parsedPet = list(self.spider.parse_pet_info(self.response_provider.create_response_from_web(self.PET_RESOURCE_URL)))

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
        expectedPet['resource_url'] = self.PET_RESOURCE_URL
        expectedPet['animal_shelter'] = PROTECTORA_LUGO_NAME
        expectedPet['animal_shelter_location'] = PROTECTORA_LUGO_LOCATION 
        expectedPet['description'] = ''

        return expectedPet

    def _create_expected_urls(self):
        return [
            'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14322&especie=FELINA&nombre_animal=RABUDA&pagina=1',
            'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14320&especie=CANINA&nombre_animal=FUSCA&pagina=1',
            'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14321&especie=FELINA&nombre_animal=ROMI&pagina=1',
            'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14319&especie=CANINA&nombre_animal=CESTEIRO&pagina=1',
            'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14318&especie=CANINA&nombre_animal=QUEIZ%C3%81N&pagina=1',
            'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14310&especie=CANINA&nombre_animal=MACRO&pagina=1',
            'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14296&especie=FELINA&nombre_animal=FENDER&pagina=1',
            'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14297&especie=FELINA&nombre_animal=CASTER&pagina=1',
            'http://www.protectoralugo.org/index.php?option=com_content&view=article&id=67&ref=14293&especie=CANINA&nombre_animal=CHUSCO&pagina=1'
        ]

if __name__ == '__main__':
    unittest.main()