# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter


class WxappPipeline(object):
    def __init__(self):
        # 创建一个文件对象
        self.fp = open('wxapp.json', 'ab')
        # 创建exporter对象，用于输出数据
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf8')

    def process_item(self, item, spider):
        # 输出数据
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 关闭文件对象
        self.fp.close()
