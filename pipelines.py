# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QianchengPipeline(object):

    #def __init__(self):
        #self.file = open('qiancheng.json', 'w', encoding='utf-8')


    def open_spider(self, spider):  # 当爬虫启动时调用的方法
        self.file = open('qiancheng.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print('开始存储信息，=========================', )
        # dict()用于创建空的字典，接受item的值。
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)
        return item

    def close_spider(self, spider):  # 当爬虫关闭时调用的方法
        self.file.close()  # 关闭文件


