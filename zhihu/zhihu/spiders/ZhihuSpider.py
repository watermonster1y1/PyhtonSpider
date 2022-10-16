import scrapy


class ZhihuspiderSpider(scrapy.Spider):
    name = 'ZhihuSpider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
