import scrapy
import json

class ZhihuspiderSpider(scrapy.Spider):
    name = 'ZhihuSpider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=100&offset=0&period=hour']
    def parse(self, response):
        data = json.loads(response.text)
