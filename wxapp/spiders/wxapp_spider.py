# -*- coding: utf-8 -*-
# scrapy genspider -t crawl wxapp_spider "www.wxapp-union.com"
# 爬取微信小程序社区教程文章
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['www.wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_detail', follow=False)
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    # 解析页面详情
    def parse_detail(self, response):
        item = {}
        # get title
        title = response.xpath('//h1[@class="ph"]/text()').get()
        # get title
        author = response.xpath('//p[@class="authors"]/a/text()').get()
        # get time
        pub_time = response.xpath('//p[@class="authors"]/span/text()').get()
        # get content
        article_content = response.xpath('//td[@id="article_content"]//text()').getall()
        article_content = ''.join(article_content).strip()
        item = WxappItem(title=title, author=author, pub_time=pub_time, article_content=article_content)
        yield item

        #
        # return item
