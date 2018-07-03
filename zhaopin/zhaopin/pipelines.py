# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class ZhaopinPipeline(object):
    def __init__(self):
        client=MongoClient('192.168.77.130')
        self.collection = client.db.zhaopin

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
