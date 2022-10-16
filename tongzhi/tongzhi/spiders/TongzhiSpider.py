import scrapy


class TongzhispiderSpider(scrapy.Spider):
    name = 'TongzhiSpider'
    allowed_domains = ['https://www.bkjx.sdu.edu.cn/sanji_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010']
    start_urls = ['https://www.bkjx.sdu.edu.cn/sanji_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010']

    def parse(self, response):
        # 获取所有信息
        info_list = response.xpath('//div[@class = "newscontent"]/div[@class = "leftNews3"]')
        for info in info_list:
            # 获取链接
            link = info.xpath('./div[@style = "float:left"]/a/@href').extract_first()
            # 获取标题
            title = info.xpath('./div[@style = "float:left"]/a/text()').extract_first()
            # 获取时间
            time = info.xpath('./div[@style = "float:right;"]/text()').extract_first()
            with open('test.txt','a',encoding='utf-8') as fp:
                fp.write(str(link))
                fp.write('\n')
                fp.write(title)
                fp.write('\n')
                fp.write(str(time))
                fp.write('\n')
        pass
