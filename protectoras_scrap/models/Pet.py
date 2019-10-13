import scrapy

class Pet(scrapy.Item):
    
    name = scrapy.Field()
    breed = scrapy.Field()
    sex = scrapy.Field()
    born_date = scrapy.Field()
    dangerous = scrapy.Field()
    aptitude = scrapy.Field()
    adult_weight = scrapy.Field()