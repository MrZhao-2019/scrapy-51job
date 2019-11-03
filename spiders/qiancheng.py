# -*- coding: utf-8 -*-
import scrapy
from ..items import QianchengItem

class QianchengSpider(scrapy.Spider):
    name = 'qiancheng'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html']

    def parse(self, response):
        result = response.xpath('//div[@class="dw_table"]/div[@class="el"]')

        for item in result:
            items = QianchengItem()
            # print(result.xpath('./p').extract())
            items['work_name'] = item.xpath('./p[@class="t1 "]/span/a/@title').extract_first()
            # .strip()是去除空格的意思
            items['company'] = item.xpath('./span[@class="t2"]/a/text()').extract_first().strip()
            items['work_addr'] = item.xpath('./span[@class="t3"]/text()').extract_first().strip()
            items['salary'] = item.xpath('./span[@class="t4"]/text()').extract_first()
            items['create_time'] = item.xpath('./span[@class="t5"]/text()').extract_first().strip()
            items['work_name'] = item.xpath('./p/span/a/text()').extract_first().strip()

            detail_url = item.xpath('./p/span/a/@href').extract_first()
            if not detail_url:
                continue
            yield scrapy.Request(url=detail_url, callback=self.parse_content, meta={'items': items})

    def parse_content(self, response):
        items = response.meta.get('items')
        items['content'] = ''.join(response.xpath('//div[@class="bmsg job_msg inbox"]//text()').extract())
        yield items


