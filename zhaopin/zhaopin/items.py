# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    url = scrapy.Field()
    position = scrapy.Field()
    salary = scrapy.Field()
    area = scrapy.Field()
    education = scrapy.Field()
    experience = scrapy.Field()
    number = scrapy.Field()
    type_ = scrapy.Field()
    pubdate = scrapy.Field()
    validate = scrapy.Field()
    duty = scrapy.Field()
    company = scrapy.Field()
    co_property = scrapy.Field()
    co_scale = scrapy.Field()
    co_type = scrapy.Field()
    address = scrapy.Field()
    