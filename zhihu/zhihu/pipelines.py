# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ZhihuPipeline:
    def open_spider(self,spider):
        self.fp = open('data.json','a',encoding = 'utf-8')
    def process_item(self, item, spider):
        self.fp.write(str(item)+'\n')
    def close_spider(self,spider):
        self.fp.close()

from scrapy.utils.project import get_project_settings
import pymysql

class MysqlPipeline:
    # 传入数据库参数
    def open_spider(self, spider):
        settings = get_project_settings()
# DB_HOST = '123.60.211.16'
# DB_PORT = 3306
# DB_USER = 'root'
# DB_PASSWORD = 'daybreak1!'
# DB_NAME = 'spider_tongzhi'
# DB_CHARSET = 'utf8'
        self.host = settings['DB_HOST']
        self.port =  settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        self.connect()

    # 连接数据库
    def connect(self):
        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.name,
            charset = self.charset,
        )
        self.cursor = self.conn.cursor()

    # 上传数据
    def process_item(self, item, spider):
        sql = 'insert into zhihu(link, title, tag, value) values("{}","{}","{}","{}")'.format(item['link'], item['title'], item['tag'], item['value'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()