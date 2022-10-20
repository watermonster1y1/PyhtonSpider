# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    value = scrapy.Field()
    tag = scrapy.Field()
    pass
