# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from dbxzSpider.util import UpyunUtil
from dbxzSpider.util import TopicUtil


class DbxzPipeline(object):
    def process_item(self, item, spider):
        if not item or not item['name']:
            raise DropItem(item)
        return item

class ProcessPipeline(object):
    def process_item(self, item, spider):
        print item['tid']
        topic = self.get_topic(str(item['tid']))
        print topic
        if not topic:
            print "topic does not exist in mongodb!"
            self.download_pic(item)
            self.upload_pic(item)
        else:
            print "topic exists in mongodb!"
            raise DropItem(item)
        return item

    def get_topic(self, tid):
        topic = TopicUtil.get_topic_by_id(tid)
        return topic

    def download_pic(self, item):
        imgs = item['imgs']
        if len(imgs) == 1: return
        for img in imgs:
            UpyunUtil.download(img)

    def upload_pic(self, item):
        imgs = item['imgs']
        if len(imgs) == 1: return
        for img in imgs:
            UpyunUtil.upload(img)

class SaveTopicPipeline(object):
    def process_item(self, item, spider):
        TopicUtil.save_topic(dict(item))
        return item



