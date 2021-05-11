# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopDetails(scrapy.Item):
    
    id_         = scrapy.Field()
    brand       = scrapy.Field()
    productName = scrapy.Field()
    price       = scrapy.Field()


class ImgData(scrapy.Item):
    id_ = scrapy.Field()
    image_urls = scrapy.Field()
    images     = scrapy.Field()


class ProductURLitem(scrapy.Item):

    producturl = scrapy.Field()
