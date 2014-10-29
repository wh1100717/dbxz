#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import re

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from dbxzSpider.items import topicItem
from dbxzSpider.config import SpiderConfig

max_page = 1

group = ["kaopulove", "haixiuzu"]

class byhxSpider(Spider):
    name = "byhx"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/group/haixiuzu/discussion?start=0"
    ]

    def parse(self, response):
        count = 0
        while True:
            if count > max_page: break
            req = Request(url="http://www.douban.com/group/"+group[count % len(group)]+"/discussion?start="+str(count / len(group) * 25),callback = self.parse_group)
            count += 1
            yield req

    def parse_group(self, response):
        urls = response.css('.olt tr')
        # from scrapy.shell import inspect_response
        # inspect_response(response)
        for i in urls:
            td = i.css('td')
            if len(td) == 0: continue
            url = td[0].css('a').xpath('@href').extract()
            if len(url) == 0: continue
            req = Request(url= url[0], callback = self.parse_req)
            yield req

    def parse_req(self, response):
        item = topicItem()
        topicPath = SpiderConfig.topic
        item['url'] = response.url
        item['tid'] = item['url'].split('/')[-2]

        # from scrapy.shell import inspect_response
        # inspect_response(response)

        for key in topicPath:
            value = response.css(topicPath[key]).extract() if topicPath[key]!='' else ''
            item[key] = value[0].strip() if len(value) == 1 else ('' if len(value) == 0 else value)

        imgs = item['imgs']
        if type(imgs) != list: item['imgs'] = [imgs]

        item['group'] = item['group'].split('/')[-2]

        return item
