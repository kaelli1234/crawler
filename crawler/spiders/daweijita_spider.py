import scrapy
import time

from crawler.items import HotListItem
from scrapy.http import  Request

class DaweijitaSpider(scrapy.spiders.Spider):
    name = "daweijita"
    allowed_domains = ["daweijita.com"]
    start_urls = [
        "http://www.daweijita.com/2441.html",
    ]

    def parse(self, response):
        for sel in response.xpath('//article[@id="post-2441"]/div/table/tbody/tr/td'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            if not title and not link:
                title = sel.xpath('strong/span/a/text()').extract()
                link = sel.xpath('strong/span/a/@href').extract()
                if not title and not link:
                    continue

            item = HotListItem()
            item['title'] = title[0]
            item['author'] = title[0]
            item['post_link'] = link[0]

            if link[0].startswith('http://www.daweijita.com'):
                url = link[0]
                yield Request(url, callback=self.parse_detail, meta={'item':item})

    def parse_detail(self, response):
        item = response.meta['item']
        video_link = response.xpath('//article/div[@class="entry"]/iframe/@src').extract()
        if not video_link:
            video_link = response.xpath('//article/div[@class="entry"]/p/iframe/@src').extract()
        item['video_link'] = video_link
        item['gita_images'] = response.xpath('//article/div[@class="entry"]/p/a/@href').extract()
        item['created_at'] = time.strftime('%Y-%m-%d %H:%M:%S')
        yield item