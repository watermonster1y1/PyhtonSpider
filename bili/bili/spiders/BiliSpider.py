import scrapy


class BilispiderSpider(scrapy.Spider):
    name = 'BiliSpider'
    allowed_domains = ['space.bilibili.com']
    start_urls = ['http://space.bilibili.com/']

    def parse(self, response):
        pass
