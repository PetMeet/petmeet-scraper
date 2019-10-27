# -*- coding: utf-8 -*-

from protectoras_scrap.spiders.protectora_gatocan_spider.constants import PROTECTORA_GATOCAN_NAME
from protectoras_scrap.spiders.protectora_gatocan_spider.constants import PROTECTORA_GATOCAN_LOCATION
from protectoras_scrap.tests.protectora_gatocan_spider.test_constants import *
from protectoras_scrap.models.Pet import Pet


class ProtectoraGatocanTestFactory:

    @staticmethod
    def create_cat_model():
        expectedPet = Pet()
        expectedPet['name'] = 'Magno'
        expectedPet['pet_type'] = 'CAT'
        expectedPet['picture'] = BASE_URL + '/fotos/20191012061123.jpg'
        expectedPet['breed'] = 'Común Europeo'
        expectedPet['sex'] = 'MALE'
        expectedPet['born_date'] = '01/09/2019'
        expectedPet['dangerous'] = '-'
        expectedPet['adopted'] = '-'
        expectedPet['resource_url'] = PET_CAT_RESOURCE_URL
        expectedPet['animal_shelter'] = PROTECTORA_GATOCAN_NAME
        expectedPet['animal_shelter_location'] = PROTECTORA_GATOCAN_LOCATION
        expectedPet['description'] = 'Precioso gatiño bo e cariñoso'

        return expectedPet

    @staticmethod
    def create_dog_model():
        expectedPet = Pet()
        expectedPet['name'] = 'Harpo'
        expectedPet['pet_type'] = 'DOG'
        expectedPet['picture'] = BASE_URL + '/fotos/20191025110423.jpg'
        expectedPet['breed'] = 'Caniche'
        expectedPet['sex'] = 'MALE'
        expectedPet['born_date'] = '15/12/2013'
        expectedPet['dangerous'] = '-'
        expectedPet['adopted'] = '-'
        expectedPet['resource_url'] = PET_DOG_RESOURCE_URL
        expectedPet['animal_shelter'] = PROTECTORA_GATOCAN_NAME
        expectedPet['animal_shelter_location'] = PROTECTORA_GATOCAN_LOCATION
        expectedPet[
            'description'] = 'Harpo criouse desde os tres meses ata agora nun fogar, pero por circunstancias da vida, ' \
                             'agora está no refuxio onde busca unha boa familia á que poida acompañar o resto da súa ' \
                             'vida. É nobre,cariñoso, guapo e adora aos nenos.'

        return expectedPet

    @staticmethod
    def create_expected_urls():
        return [
            'http://www.gatocan.com/DatosAnimal.php?id=20191012061123&foto=fotos/20191012061123.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20191012060843&foto=fotos/20191012060843.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190928072822&foto=fotos/20190928072822.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190928072639&foto=fotos/20190928072639.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190928072447&foto=fotos/20190928072447.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190928072232&foto=fotos/20190928072232.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190928072100&foto=fotos/20190928072100.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190928071931&foto=fotos/20190928071931.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190928054409&foto=fotos/20190928054409.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190915045743&foto=fotos/20190915045743.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190912061254&foto=fotos/20190912061254.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190908084913&foto=fotos/20190908084913.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190901051842&foto=fotos/20190901051842.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190901045951&foto=fotos/20190901045951.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190901045351&foto=fotos/20190901045351.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190809081709&foto=fotos/20190809081709.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190706070726&foto=fotos/20190706070726.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190706070529&foto=fotos/20190706070529.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190623065708&foto=fotos/20190623065708.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190623065515&foto=fotos/20190623065515.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190623065358&foto=fotos/20190623065358.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190623065141&foto=fotos/20190623065141.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190526045138&foto=fotos/20190526045138.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190519060320&foto=fotos/20190519060320.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190414072453&foto=fotos/20190414072453.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190310054517&foto=fotos/20190310054517.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190301011802&foto=fotos/20190301011802.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190228115330&foto=fotos/20190228115330.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190217062112&foto=fotos/20190217062112.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190210085209&foto=fotos/20190210085209.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190210084941&foto=fotos/20190210084941.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190127073337&foto=fotos/20190127073337.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190127052625&foto=fotos/20190127052625.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190106091009&foto=fotos/20190106091009.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20190106090155&foto=fotos/20190106090155.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20181225062129&foto=fotos/20181225062129.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20181225061844&foto=fotos/20181225061844.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20181206065113&foto=fotos/20181206065113.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20181206065012&foto=fotos/20181206065012.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20181206064650&foto=fotos/20181206064650.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20181206063857&foto=fotos/20181206063857.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20181027064801&foto=fotos/20181027064801.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20181016124921&foto=fotos/20181016124921.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20181006055411&foto=fotos/20181006055411.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180923062412&foto=fotos/20180923062412.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180909034220&foto=fotos/20180909034220.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180810100641&foto=fotos/20180810100641.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180804052236&foto=fotos/20180804052236.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180729051815&foto=fotos/20180729051815.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180729051637&foto=fotos/20180729051637.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180721050205&foto=fotos/20180721050205.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180721045630&foto=fotos/20180721045630.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180721045212&foto=fotos/20180721045212.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180708040410&foto=fotos/20180708040410.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180701060303&foto=fotos/20180701060303.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180624055853&foto=fotos/20180624055853.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180624055508&foto=fotos/20180624055508.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180624055333&foto=fotos/20180624055333.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180426110841&foto=fotos/20180426110841.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180225075002&foto=fotos/20180225075002.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180225074203&foto=fotos/20180225074203.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180219123003&foto=fotos/20180219123003.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180204053257&foto=fotos/20180204053257.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20180204052930&foto=fotos/20180204052930.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20171223050129&foto=fotos/20171223050129.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20171217054757&foto=fotos/20171217054757.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20171203030859&foto=fotos/20171203030859.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20171124063937&foto=fotos/20171124063937.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20171120101822&foto=fotos/20171120101822.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170827052747&foto=fotos/20170827052747.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170816050303&foto=fotos/20170816050303.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170816045946&foto=fotos/20170816045946.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170722073150&foto=fotos/20170722073150.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170719083110&foto=fotos/20170719083110.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170716071732&foto=fotos/20170716071732.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170709043901&foto=fotos/20170709043901.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170625050232&foto=fotos/20170625050232.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170625050109&foto=fotos/20170625050109.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170625045910&foto=fotos/20170625045910.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170605061020&foto=fotos/20170605061020.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170422063448&foto=fotos/20170422063448.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170402060245&foto=fotos/20170402060245.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170318060612&foto=fotos/20170318060612.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170225085616&foto=fotos/20170225085616.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170203032448&foto=fotos/20170203032448.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20170122033513&foto=fotos/20170122033513.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20161231052326&foto=fotos/20161231052326.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20161227014606&foto=fotos/20161227014606.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20161227014252&foto=fotos/20161227014252.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20161227013833&foto=fotos/20161227013833.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20161130105138&foto=fotos/20161130105138.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20161121113209&foto=fotos/20161121113209.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160804055143&foto=fotos/20160804055143.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160804023258&foto=fotos/20160804023258.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160714031349&foto=fotos/20160714031349.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160714031011&foto=fotos/20160714031011.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160711030507&foto=fotos/20160711030507.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160522063050&foto=fotos/20160522063050.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160502094825&foto=fotos/20160502094825.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160502094544&foto=fotos/20160502094544.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160502094151&foto=fotos/20160502094151.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160320100355&foto=fotos/20160320100355.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160320100118&foto=fotos/20160320100118.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20160306050903&foto=fotos/20160306050903.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20151025073257&foto=fotos/20151025073257.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20151011052144&foto=fotos/20151011052144.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150920064518&foto=fotos/20150920064518.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150614062013&foto=fotos/20150614062013.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150605063224&foto=fotos/20150605063224.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150529054752&foto=fotos/20150529054752.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150516051126&foto=fotos/20150516051126.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150331082552&foto=fotos/20150331082552.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150331080107&foto=fotos/20150331080107.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150326083941&foto=fotos/20150326083941.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150218043955&foto=fotos/20150218043955.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20150125072738&foto=fotos/20150125072738.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140824052751&foto=fotos/20140824052751.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140725100301&foto=fotos/20140725100301.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140616080521&foto=fotos/20140616080521.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140616080242&foto=fotos/20140616080242.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140429074758&foto=fotos/20140429074758.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140414040320&foto=fotos/20140414040320.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140414035428&foto=fotos/20140414035428.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140414034713&foto=fotos/20140414034713.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140414034205&foto=fotos/20140414034205.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140325075152&foto=fotos/20140325075152.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140319093100&foto=fotos/20140319093100.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20140226061808&foto=fotos/20140226061808.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20131207012618&foto=fotos/20131207012618.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20131207012433&foto=fotos/20131207012433.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20131001093705&foto=fotos/20131001093705.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130818042357&foto=fotos/20130818042357.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130805054147&foto=fotos/20130805054147.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130709101035&foto=fotos/20130709101035.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130709100919&foto=fotos/20130709100919.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130709100737&foto=fotos/20130709100737.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130709100559&foto=fotos/20130709100559.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130709100344&foto=fotos/20130709100344.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130619121620&foto=fotos/20130619121620.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130503064226&foto=fotos/20130503064226.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20130409100724&foto=fotos/20130409100724.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20121113061337&foto=fotos/20121113061337.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20120808124329&foto=fotos/20120808124329.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20120703025649&foto=fotos/20120703025649.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20120628050818&foto=fotos/20120628050818.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20120514024511&foto=fotos/20120514024511.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20120430060436&foto=fotos/20120430060436.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20120123064134&foto=fotos/20120123064134.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20110912093658&foto=fotos/20110912093658.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20110728111053&foto=fotos/20110728111053.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20110708042614&foto=fotos/20110708042614.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20110613081942&foto=fotos/20110613081942.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20110524081524&foto=fotos/20110524081524.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20101202081828&foto=fotos/20101202081828.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20101027085727&foto=fotos/20101027085727.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20100815104943&foto=fotos/20100815104943.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20100814110101&foto=fotos/20100814110101.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20100201064754&foto=fotos/20100201064754.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20091113083208&foto=fotos/20091113083208.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20091029041855&foto=fotos/20091029041855.jpg',
            'http://www.gatocan.com/DatosAnimal.php?id=20091007111726&foto=fotos/20091007111726.jpg'
        ]
