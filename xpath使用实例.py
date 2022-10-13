from lxml import etree
import urllib.request

#路径查询
#//:查找所有子孙节点
#/:查找子节点

#谓词查询
#//div[@id]
#//div[@id="maincontent"]

#属性查询
#//@class

#模糊查询
#//div[contains(@id,"xxx")]
#//div[starts-with(@id,"xxx")]

#内容查询
#//div/h1/text()

#逻辑运算
#//div[@id="head" and @class="s_down"]
#title | //price

#解析网页文件
url = 'https://www.zhihu.com/creator/hot-question/hot/100001/week'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))

tree = etree.HTML(response.read().decode('utf-8'))

#查找所有标题
title_list = tree.xpath('//body//div[@class="css-3dzvwq"]/text()')

#fp = open('test.txt','w')
#fp.print(title_list)
print(title_list)
print(len(title_list))