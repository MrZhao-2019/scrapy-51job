# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QianchengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    work_name = scrapy.Field()
    # 公司名称
    company = scrapy.Field()
    # 工作地点
    work_addr = scrapy.Field()
    # 薪资范围
    salary = scrapy.Field()
    # 发布时间
    create_time = scrapy.Field()
    # 抓取时间
    utc_time = scrapy.Field()
    # 详情页内容
    content = scrapy.Field()
    # # 职能类别
    # function_job = scrapy.Field()
    # # 经验
    # experience = scrapy.Field()
    # # 待遇
    # salary_package = scrapy.Field()
    # # 网址
    # URL_51 = scrapy.Field()
