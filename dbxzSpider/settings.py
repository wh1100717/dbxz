#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Scrapy settings for dbxzSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dbxzSpider'

LOG_LEVEL='DEBUG'

SPIDER_MODULES = ['dbxzSpider.spiders']
NEWSPIDER_MODULE = 'dbxzSpider.spiders'

ITEM_PIPELINES = {
    'dbxzSpider.pipelines.DbxzPipeline' : 300,
    'dbxzSpider.pipelines.ProcessPipeline' : 400,
    'dbxzSpider.pipelines.SaveTopicPipeline' : 500
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dbxzSpider (+http://www.yourdomain.com)'

#--------------------avoid banning:2 seconds once time--------------
DOWNLOAD_DELAY = 1
COOKIES_ENABLED = False
RANDOMIZE_DOWNLOAD_DELAY = True

DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'dbxzSpider.util.RandomUseragentUtil.RotateUserAgentMiddleware' :400,
    }
