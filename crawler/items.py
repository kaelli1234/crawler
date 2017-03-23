# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HotListItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    post_link = scrapy.Field()
    video_link = scrapy.Field()
    gita_images = scrapy.Field()
    created_at = scrapy.Field()
