# -*- coding: utf-8 -*-

import unittest
from scrapy.utils.serialize import ScrapyJSONEncoder

from protectoras_scrap.spiders.protectora_gatocan_spider import protectora_gatocan_spider
from protectoras_scrap.tests.protectora_gatocan_spider.test_constants import *
from protectoras_scrap.tests.utils.response_provider import ResponseProvider
from protectoras_scrap.tests.protectora_gatocan_spider.protectora_gatocan_test_factory import \
    ProtectoraGatocanTestFactory


class TestProtectoraGatocanSpider(unittest.TestCase):

    def setUp(self):
        self.spider = protectora_gatocan_spider.ProtectoraGatoCanSpider()
        self.spider.custom_settings = {}
        self.encoder = ScrapyJSONEncoder(ensure_ascii=False)

    def test_parse_pet_urls_local_response(self):
        requests = list(self.spider.parse_pet_urls(
            ResponseProvider().create_response_from_file(PET_LIST_HTML_SOURCE, self.spider.start_urls[0])))

        requests = [r.url for r in requests]

        self.assertListEqual(requests, ProtectoraGatocanTestFactory.create_expected_urls(), "Expected urls don't match")

    def test_parse_pet_urls_web_response(self):
        requests = list(
            self.spider.parse_pet_urls(ResponseProvider().create_response_from_web(self.spider.start_urls[0])))

        self.assertTrue(len(requests) > 0, "Expected at leas 1 url")

    def test_parse_pet_info_cat_with_local_response(self):
        parsed_pet = list(self.spider.parse_pet_info(
            ResponseProvider().create_response_from_file(PET_CAT_HTML_SOURCE, PET_CAT_RESOURCE_URL,
                                                         {'pet_type': 'CAT'})))

        self.assertEqual(ProtectoraGatocanTestFactory.create_cat_model(), parsed_pet[0],
                         "Expected pet model doesn't match")

    def test_parse_pet_info_cat_with_web_response(self):
        parsed_pet = list(self.spider.parse_pet_info(
            ResponseProvider().create_response_from_web(PET_CAT_RESOURCE_URL, {'pet_type': 'CAT'})))

        self.assertEqual(ProtectoraGatocanTestFactory.create_cat_model(), parsed_pet[0],
                         "Expected pet model doesn't match")

    def test_parse_pet_info_dog_with_local_response(self):
        parsed_pet = list(self.spider.parse_pet_info(
            ResponseProvider().create_response_from_file(PET_DOG_HTML_SOURCE, PET_DOG_RESOURCE_URL,
                                                         {'pet_type': 'DOG'})))

        self.assertEqual(ProtectoraGatocanTestFactory.create_dog_model(), parsed_pet[0],
                         "Expected pet model doesn't match")

    def test_parse_pet_info_dog_with_web_response(self):
        parsed_pet = list(self.spider.parse_pet_info(
            ResponseProvider().create_response_from_web(PET_DOG_RESOURCE_URL, {'pet_type': 'DOG'})))

        self.assertEqual(ProtectoraGatocanTestFactory.create_dog_model(), parsed_pet[0],
                         "Expected pet model doesn't match")


if __name__ == '__main__':
    unittest.main()
