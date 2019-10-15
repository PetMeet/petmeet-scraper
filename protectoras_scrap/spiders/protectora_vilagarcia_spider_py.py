# -*- coding: utf-8 -*-
import scrapy


class ProtectoraVilagarciaSpiderPySpider(scrapy.Spider):
    name = 'protectora_vilagarcia_spider.py'
    allowed_domains = ['http://protectoravilagarcia.org/']
    base_url = 'http://protectoravilagarcia.org/'
    start_urls = ['http://protectoravilagarcia.org/listado/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_pets_urls)
        
    def get_next_page(self, response):
        return response.xpath("//span[@class='navPaginado']/a[@title='Página siguiente']").attrib['href']
        

    ## Work in progress!
    def parse_pets_urls(self, response):

        next_page = self.get_next_page(response)
        
        data = response.xpath("//div[@id='principal_contenidos']/div/*/text()").getall()

        self.get_next_page(response)

