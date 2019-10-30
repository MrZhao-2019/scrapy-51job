# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QianchengPipeline(object):

    def __init__(self):
        self.file = open('qiancheng.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print('开始存储信息，=========================', )
        # dict()创建一个新的字典，接受item的值。
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)
        return item
