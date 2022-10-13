import scrapy


class Zhihu100001Spider(scrapy.Spider):
    name = 'zhihu_100001'
    allowed_domains = ['https://www.zhihu.com/creator/hot-question/hot/100001/week']
    start_urls = ['https://www.zhihu.com/creator/hot-question/hot/100001/week/']

    def parse(self, response):
        pass