# coding=utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import codecs

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    def open_spider(self, spider):
        self.file = codecs.open('./output/%s.json' % spider.filename, 'w', encoding='utf-8')
        self.file.write("[")

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ","
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()
