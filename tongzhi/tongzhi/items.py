# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TongzhiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 通知标题
    title = scrapy.Field()
    # 通知链接
    link = scrapy.Field()
    # 通知发布时间
    time = scrapy.Field()
    pass
