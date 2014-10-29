#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dbxzSpider.util import MongoUtil

TopicCollection = MongoUtil.db.topic

def get_topic_by_id(tid):
    return TopicCollection.find_one({'tid': tid})

def save_topic(topic):
    print type(topic)
    TopicCollection.insert(topic)