# -*- coding: utf-8 -*-

import unittest
from unittest.mock import MagicMock

from protectoras_scrap.spiders.protectora_lugo_spider import protectora_lugo_spider
from protectoras_scrap.tests.utils.response_provider import ResponseProvider
from protectoras_scrap.tests.protectora_lugo_spider.test_constants import *
from protectoras_scrap.tests.protectora_lugo_spider.protectora_lugo_test_factory import ProtectoraLugoTestFactory


class TestProtectoraLugoSpider(unittest.TestCase):

    def setUp(self):
        self.spider = protectora_lugo_spider.ProtectoraLugoSpider()
        self.spider.custom_settings = {}

    def test_get_next_page_local_response(self):
        result = protectora_lugo_spider.get_next_page(
            ResponseProvider().create_response_from_file(PET_LIST_HTML_SOURCE, self.spider.start_urls[0]))
        self.assertEqual(NEXT_PAGE_URL, result, "Expected next page doesn't match")

    def test_get_next_page_web_response(self):
        result = protectora_lugo_spider.get_next_page(ResponseProvider().create_response_from_web(self.spider.start_urls[0]))
        self.assertEqual(NEXT_PAGE_URL, result, "Expected next page doesn't match")

    def test_parse_pet_urls_local_response(self):
        protectora_lugo_spider.get_next_page = MagicMock(return_value=None)

        requests = list(self.spider.parse_pet_urls(
            ResponseProvider().create_response_from_file(PET_LIST_HTML_SOURCE, self.spider.start_urls[0])))

        requests = [r.url for r in requests]

        self.assertListEqual(requests, ProtectoraLugoTestFactory().create_expected_urls(), "Expected urls don't match")

    def test_parse_pet_urls_web_response(self):
        protectora_lugo_spider.get_next_page = MagicMock(return_value=None)

        requests = list(
            self.spider.parse_pet_urls(ResponseProvider().create_response_from_web(self.spider.start_urls[0])))

        self.assertTrue(len(requests) == 9, "Expected 9 urls but found %d" % len(requests))

    def test_parse_pet_info_with_local_response(self):
        parsed_pet = list(
            self.spider.parse_pet_info(ResponseProvider().create_response_from_file(PET_HTML_SOURCE, PET_RESOURCE_URL)))

        self.assertEqual(ProtectoraLugoTestFactory().create_pet_model(), parsed_pet[0],
                         "Expected pet model doesn't match")

    def test_parse_pet_info_with_web_response(self):
        parsed_pet = list(self.spider.parse_pet_info(ResponseProvider().create_response_from_web(PET_RESOURCE_URL)))

        self.assertEqual(ProtectoraLugoTestFactory().create_pet_model(), parsed_pet[0],
                         "Expected pet model doesn't match")


if __name__ == '__main__':
    unittest.main()
