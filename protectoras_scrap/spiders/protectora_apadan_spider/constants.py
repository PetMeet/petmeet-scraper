# -*- coding: utf-8 -*-

# Constants for PROTECTORA_APADAN
PROTECTORA_APADAN_NAME = 'APADAN, Asociación Protectora de Animales Domésticos Abandonados del Noroeste'
PROTECTORA_APADAN_LOCATION = '43.254063;-8.378879'
PROTECTORA_APADAN_PAGE_DETAILS_LINK_XPATH = "//td[@class='views-field views-field-title']/a/@href"
PROTECTORA_APADAN_NEXT_PAGE_XPATH = "//li[contains(@class, 'pager-current')]/following-sibling::li[1]/a/@href"
PROTECTORA_APADAN_PET_NAME_XPATH = "//div[@class='node-title']/text()"
PROTECTORA_APADAN_PET_DATA_XPATH = "//div[@class='field-item odd']/text()"
PROTECTORA_APADAN_PET_DESCRIPTION = "//fieldset/following-sibling::p/text()"
PROTECTORA_APADAN_PET_BREED = "//div[@class='taxonomy']//li[contains(@class, 'first last')]/a/text()"
PROTECTORA_APADAN_PET_PICTURE_XPATH = "//div[@class='field-item odd']/img/@src"
