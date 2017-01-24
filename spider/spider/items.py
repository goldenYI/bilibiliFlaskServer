# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_av_field = scrapy.Field()


class HomeItem(scrapy.Item):
    data_txt = scrapy.Field()
    data_up = scrapy.Field()
    data_tg = scrapy.Field()
    data_gk = scrapy.Field()
    data_dm = scrapy.Field()
    data_title = scrapy.Field()
    data_img = scrapy.Field()
