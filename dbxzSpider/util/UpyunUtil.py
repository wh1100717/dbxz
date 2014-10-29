#!/usr/bin/env python
# -*- coding: utf-8 -*-

import upyun
import urllib
import hashlib
import os

from dbxzSpider import upyunConfig

dir = "./s"  

up = upyun.UpYun(upyunConfig.bucket, upyunConfig.username, upyunConfig.password, timeout=30, endpoint=upyun.ED_AUTO)

def get_md5_value(s):
    md5 = hashlib.md5()
    md5.update(s)
    return md5.hexdigest()

def download(url):
    try:  
        if not os.path.exists(dir):  
            os.mkdir(dir)
    except:  
        print "Failed to create directory in %s"%dir  
        return
    path = dir + "/" + get_md5_value(url) + "." + url.split('.')[-1]
    print "Download ", url, " to ", path
    urllib.urlretrieve(url, path)

def upload(url):
    path = dir + "/" + get_md5_value(url) + "." + url.split('.')[-1]
    with open(path, 'rb') as f:
        res = up.put("/" + path, f, checksum=True)
    return res