# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QianchengPipeline(object):
    def process_item(self, item, spider):
        print('开始存储信息，=========================', )
        json_file = item
        # json_str = json.dumps()
        with open('test_data.txt', 'w') as json_file:
            json_file.writelines(json.dumps(json_file) +'\n')

        # with open('qiancheng.txt', 'w') as f:
        #     # dump方法页面上的字典或类json格式的转换成json格式的字符串
        #     # json.dump(item, f)
        #     # ensure_ascii = False(输出中文)， indent = 4(缩进为4)
        #
        #     f.write(json_str)
        return item
