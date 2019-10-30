# -*- coding: utf-8 -*-
import scrapy
# from scrapy_redis.spiders import RedisSpider
from ..items import QianchengItem

class QianchengSpider(scrapy.Spider):
    name = 'qiancheng'
    allowed_domains = ['51job.com']
    # redis_key = 'qiancheng:start_urls'
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html']

    def parse(self, response):
        result = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        for item in result:
            #items = QianchengItem()
            #print(response.text)
            # print(item.extract(), '======================')
            # extract_first()返回字符串 extract()返回数组
            items_list= {}
            items_list['work_name'] = item.xpath('./p[@class="t1 "]/span/a/@title').extract_first()
            #.strip()是去除空格的意思
            items_list['company'] = item.xpath('./span[@class="t2"]/a/text()').extract_first().strip()
            items_list['work_addr'] = item.xpath('./span[@class="t3"]/text()').extract_first().strip()
            items_list['salary'] = item.xpath('./span[@class="t4"]/text()').extract_first()
            items_list['create_time'] = item.xpath('./span[@class="t5"]/text()').extract_first().strip()
            items_list['work_name'] = item.xpath('./p/span/a/text()').extract_first().strip()

            pachong = '爬虫'
            if pachong in items_list['work_name']:  # 如果标题中没有爬虫字段就跳过抓取。
                detail_url = item.xpath('./p/span/a/@href').extract_first().strip()
                items_list['URL_51'] = detail_url
                if not detail_url:  # 意思是如果detail_url不存在就。。。
                    continue  # continue跳过的意思
                yield scrapy.Request(url=detail_url, callback=self.parse_content, meta={'items_list': items_list})
        next_url = response.xpath('//li[@class="bk"][2]/a/@href').extract()[0]  # 获取下一页内容的url
        yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_content(self, response):
        # 对详情页进行数据提取
        items = QianchengItem()
        items_list = response.meta.get('items_list')
        # 岗位职责
        content = response.xpath('//div[@class="bmsg job_msg inbox"]/p//text()').extract()
        items['content'] = ''.join(content)
        # 职能类别
        items['function_job'] = ','.join(response.xpath('//div[@class="mt10"]/p/a/text()').extract())
        # 经验
        xperience = ''.join(response.xpath('//p[@class="msg ltype"]//text()').extract())
        items['experience'] = xperience.replace('\xa0', "")
        # 待遇
        items['salary_package'] = ','.join(response.xpath('//span[@class="sp4"]/text()').extract())
        items['work_name'] = items_list['work_name']
        items['company'] = items_list['company']
        items['work_addr'] = items_list['work_addr']
        items['salary'] = items_list['salary']
        items['create_time'] = items_list['create_time']
        items['work_name'] = items_list['work_name']
        items['URL_51'] = items_list['URL_51']
        yield items