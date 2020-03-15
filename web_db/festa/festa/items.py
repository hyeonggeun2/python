# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FestaItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    image = scrapy.Field()
    data = scrapy.Field()
    price = scrapy.Field()