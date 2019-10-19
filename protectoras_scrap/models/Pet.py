import scrapy

class Pet(scrapy.Item):
    
    name = scrapy.Field()                      # Pet name
    pet_type= scrapy.Field()                   # Pet type (CAT/DOG)
    picture = scrapy.Field()                   # Pet picture, (url to the resource)
    breed = scrapy.Field()                     # Pet breed
    sex = scrapy.Field()                       # Pet sex (MALE/FEMALE)
    born_date = scrapy.Field()                 # Born date
    dangerous = scrapy.Field()                 # Pet is dangerous (YES/NO/-)
    adopted = scrapy.Field()                   # Pet is already adopted (True/False)
    resource_url = scrapy.Field()              # Url where the resource data is located
    animal_shelter = scrapy.Field()            # Name of animal shelter
    animal_shelter_location = scrapy.Field()   # Animal shelter location (Coordinates spplited by ;)
    description = scrapy.Field()               # Description offered by the animal shelter