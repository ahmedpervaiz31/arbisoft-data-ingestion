# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CityItem(scrapy.Item):
    city_url = scrapy.Field()

class RestaurantItem(scrapy.Item):
    url = scrapy.Field()
    rating = scrapy.Field()
    price_range = scrapy.Field()
    cuisine = scrapy.Field()
    meals = scrapy.Field()
    location = scrapy.Field()
    google_maps_link = scrapy.Field()
    website = scrapy.Field()
    email = scrapy.Field()
    phone_number = scrapy.Field()
