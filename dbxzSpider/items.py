# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class dbxzItem(Item):
    topic_name = Field()
    topic_id = Field()
    author_name = Field()
    author_id = Field()
    comment_num = Field()
    last_comment_time = Field()

    def __repr__(self):
        #Debug和Info模式下，Pipeline处理完成后不打印Item内容
        return "\n"

class topicItem(Item):
    tid = Field()
    url = Field()
    name = Field()
    imgs = Field()
    group = Field()
    author_name = Field()
    author_id = Field()
    create_time = Field()

    def __repr__(self):
        #Debug和Info模式下，Pipeline处理完成后不打印Item内容
        return "\n"
