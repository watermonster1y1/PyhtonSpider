import scrapy
import json
from zhihu.items import ZhihuItem

class ZhihuspiderSpider(scrapy.Spider):
    name = 'ZhihuSpider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=103&offset=0&period=hour']
    def parse(self, response):
        tmp = json.loads(response.text)
        data = tmp['data']
        for i in range(len(data)):
            link = data[i]['question']['url']
            title = data[i]['question']['title']
            value = data[i]['reaction']['score']
            tag = []
            for j in data[i]['question']['topics']:
                tag.append(j['name'])
            res = ZhihuItem(link = link, title = title, value = value, tag = str(tag))
            yield res
