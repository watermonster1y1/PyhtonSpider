import scrapy


class BilispiderSpider(scrapy.Spider):
    name = 'BiliSpider'
    allowed_domains = ['space.bilibili.com']
    start_urls = ['https://space.bilibili.com/']
    uid_A = input("输入uid")
    uid_B = input("输入uid")
    base = 'https://space.bilibili.com/'
    tail = '/fans/follow'
    def parse(self, response):
        pass
