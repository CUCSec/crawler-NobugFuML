# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy import Item
from scrapy import Field
 
class JianshuHotTopicItem(scrapy.Item):


    collection_name = Field()
    collection_description = Field()
    collection_article_count = Field()
    collection_attention_count = Field()
