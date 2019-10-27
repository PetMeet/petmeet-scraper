# -*- coding: utf-8 -*-

from protectoras_scrap.spiders import PROTECTORA_APADAN_NAME
from protectoras_scrap.spiders import PROTECTORA_APADAN_LOCATION
from protectoras_scrap.tests.protectora_apadan_spider.test_constants import *
from protectoras_scrap.models.Pet import Pet


class ProtectoraApadanTestFactory:

    @staticmethod
    def create_pet_model():
        expected_pet = Pet()
        expected_pet['name'] = 'NINFA'
        expected_pet['pet_type'] = 'DOG'
        expected_pet['picture'] = 'http://www.apadan.net/sites/default/files/imagecache/image_animales_principal/ninfaa.jpg'
        expected_pet['breed'] = 'Caza'
        expected_pet['sex'] = 'FEMALE'
        expected_pet['born_date'] = '-'
        expected_pet['dangerous'] = '-'
        expected_pet['adopted'] = 'NO'
        expected_pet['resource_url'] = PET_RESOURCE_URL
        expected_pet['animal_shelter'] = PROTECTORA_APADAN_NAME
        expected_pet['animal_shelter_location'] = PROTECTORA_APADAN_LOCATION
        expected_pet['description'] = 'Esta podenca campanera fue utilizada en una rehala en Castilla, y durante esa ' \
                                      'etapa le cortaron las orejas y la cola, lo que unido al abandono la ha ' \
                                      'convertido en una perrita extraordinariamente desconfiada. Tuvo a sus ' \
                                      'cachorros en la calle, y fue recogida por una persona que consiguió ganarse ' \
                                      'su confianza y nos la trajo desde Ávila. Ahora que sus peques han encontrado ' \
                                      'buenos hogares, se recupera con nosotras y está aprendiendo a ser perro de ' \
                                      'verdad: aprende a recibir caricias, a jugar con otros perros, a caminar con ' \
                                      'corrrea... ¿Querrías ayudarla a aprender lo que es un verdadero hogar?'

        return expected_pet

    @staticmethod
    def create_expected_urls():
        return [
            'http://www.apadan.net/ninfa',
            'http://www.apadan.net/beco-0',
            'http://www.apadan.net/jerry',
            'http://www.apadan.net/lisa-2',
            'http://www.apadan.net/lucas-3',
            'http://www.apadan.net/isis',
            'http://www.apadan.net/marne',
            'http://www.apadan.net/john',
            'http://www.apadan.net/neska',
            'http://www.apadan.net/luca-0',
            'http://www.apadan.net/vito',
            'http://www.apadan.net/nysson'
        ]
