import scrapy


class TongzhispiderSpider(scrapy.Spider):
    name = 'TongzhiSpider'
    allowed_domains = ['www.bkjx.sdu.edu.cn']
    start_urls = ['http://www.bkjx.sdu.edu.cn/']

    def parse(self, response):
        pass
