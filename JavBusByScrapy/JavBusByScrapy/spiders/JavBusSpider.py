# -*- coding: utf-8 -*-
import scrapy
from JavBusByScrapy.items import JavbusbyscrapyItem


class JavbusspiderSpider(scrapy.Spider):
    name = 'JavBusSpider'
    allowed_domains = ['javbus.info/']
    start_urls = ['http://www.javbus.info/actresses']
    base_url = 'http://www.javbus.info'
    count = 1

    def parse(self, response):
        actress = response.css('a[class*=avatar]')
        items = JavbusbyscrapyItem()
        for each in actress:
            name = each.css('span::text').extract_first()
            main_page = each.css('a::attr(href)').extract_first()
            items['name'] = name
            items['main_page'] = main_page
            yield items

        relative_url = response.css('a#next::attr(href)').extract_first()
        if relative_url:
            next_page = self.base_url+relative_url
            yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=True)

