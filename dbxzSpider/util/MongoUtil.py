#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

from pymongo import MongoClient

__mongo_config__ = {
    # 'host': '10.0.1.202',
    'host': '127.0.0.1',
    'port': 27017,
    'db': 'dbxz',
}

client = MongoClient(__mongo_config__['host'], __mongo_config__['port'])
db = client[__mongo_config__['db']]
