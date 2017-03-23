import scrapy

from crawler.items import HotListItem

class LilinjianSpider(scrapy.spiders.Spider):
    name = "daweijita"
    allowed_domains = ["daweijita.com"]
    start_urls = [
        "http://www.daweijita.com/2441.html",
    ]

    def parse(self, response):
        for sel in response.xpath('//article[@id="post-2441"]/div/table/tbody/tr/td[@width="271"]'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            if not title and not link:
                continue

            item = HotListItem()
            item['title'] = title[0]
            item['link'] = link[0]
            yield item