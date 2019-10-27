# -*- coding: utf-8 -*-
import pika
import json
from scrapy.utils.serialize import ScrapyJSONEncoder

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
class ProtectorasScrapPipeline(object):

    def __init__(self, host, port, user, password, routing_key):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.routing_key = routing_key

        credentials = pika.PlainCredentials(self.user, self.password)

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port, credentials=credentials))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=self.routing_key)

        self.encoder = ScrapyJSONEncoder(ensure_ascii=False)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('RABBITMQ_HOST'),
            port=crawler.settings.get('RABBITMQ_PORT'),
            user=crawler.settings.get('RABBITMQ_USER'),
            password=crawler.settings.get('RABBITMQ_PASS'),
            routing_key=crawler.settings.get('RABBITMQ_ROUTING_KEY')
        )

    def close_spider(self, spider):
        self.channel.close()
        self.connection.close()

    def process_item(self, item, spider):
        data = self.encoder.encode(item)
        self.channel.basic_publish(exchange='',
                      routing_key=self.routing_key,
                      body=data)