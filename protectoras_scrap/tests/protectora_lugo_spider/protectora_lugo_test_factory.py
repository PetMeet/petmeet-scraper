# -*- coding: utf-8 -*-

from protectoras_scrap.spiders.protectora_lugo_spider.constants import PROTECTORA_LUGO_NAME
from protectoras_scrap.spiders.protectora_lugo_spider.constants import PROTECTORA_LUGO_LOCATION
from protectoras_scrap.tests.protectora_lugo_spider.test_constants import *
from protectoras_scrap.models.Pet import Pet

class ProtectoraLugoTestFactory:

    @staticmethod
    def create_pet_model():
        
        expectedPet = Pet()
        expectedPet['name'] = 'RABUDA'
        expectedPet['pet_type'] = 'CAT'
        expectedPet['picture'] = BASE_URL + '/cache/jw_simpleImageGallery/jwsig_cache_a5d7a332a1_14322.jpg'
        expectedPet['breed'] = 'Europeo'
        expectedPet['sex'] = 'FEMALE'
        expectedPet['born_date'] = '05/12/2018'
        expectedPet['dangerous'] = 'NO'
        expectedPet['adopted'] = 'NO'
        expectedPet['resource_url'] = PET_RESOURCE_URL
        expectedPet['animal_shelter'] = PROTECTORA_LUGO_NAME
        expectedPet['animal_shelter_location'] = PROTECTORA_LUGO_LOCATION 
        expectedPet['description'] = ''

        return expectedPet

    @staticmethod
    def create_expected_urls():
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