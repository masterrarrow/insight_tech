# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InsightItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()   # Article link
    title = scrapy.Field()  # Title
    text = scrapy.Field()   # Text
