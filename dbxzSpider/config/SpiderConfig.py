#!/usr/bin/env python
# -*- coding: utf-8 -*-  

topic = {
    'name': '#content > h1::text',
    'imgs': '.topic-figure img::attr(src)',
    'group': '.bd .info a::attr(href)',
    'author_name': '.from a::text',
    'author_id': '.from a::attr(href)',
    'create_time': '.topic-doc span[class=color-green]::text',    
}