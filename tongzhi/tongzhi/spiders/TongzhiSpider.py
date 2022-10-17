import scrapy
from tongzhi.items import TongzhiItem

class TongzhispiderSpider(scrapy.Spider):
    name = 'TongzhiSpider'
    allowed_domains = ['www.bkjx.sdu.edu.cn']
    start_urls = ['https://www.bkjx.sdu.edu.cn/sanji_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010']

    # url = head + str(page) + tail
    base = 'https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=154&PAGENUM='
    tail = '&urltype=tree.TreeTempUrl&wbtreeid=1010'
    page = 1
    def parse(self, response):
        # 获取所有信息
        info_list = response.xpath('//div[@class = "newscontent"]/div[@class = "leftNews3"]')
        for info in info_list:
            # 获取链接
            link = 'https://www.bkjx.sdu.edu.cn/'+str(info.xpath('./div[@style = "float:left"]/a/@href').extract_first())
            # 获取标题
            title = info.xpath('./div[@style = "float:left"]/a/text()').extract_first()
            # 获取时间
            time = info.xpath('./div[@style = "float:right;"]/text()').extract_first()
            with open('data.txt','a',encoding='utf-8') as fp:
                fp.write(str(link))
                fp.write('\n')
                fp.write(title)
                fp.write('\n')
                fp.write(str(time))
                fp.write('\n')
            data = TongzhiItem(link = link, title = title, time = time)
            yield data
        # 爬取下一页
        if self.page < 154:
            self.page = self.page +1
            url = self.base + str(self.page) + self.tail
            yield scrapy.Request(url = url, callback = self.parse)
