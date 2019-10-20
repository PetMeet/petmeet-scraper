# -*- coding: utf-8 -*-

# Scrapy settings for protectoras_scrap project

BOT_NAME = 'protectoras_scrap'

# Spiders
SPIDER_MODULES = ['protectoras_scrap.spiders']
NEWSPIDER_MODULE = 'protectoras_scrap.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Enable/Disable log
LOG_ENABLED = False

# Encoding when exporting data
FEED_EXPORT_ENCODING = 'utf-8'

# RabbitMQ connection params
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'
RABBITMQ_ROUTING_KEY = 'protectoras'