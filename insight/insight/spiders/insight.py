# -*- coding: utf-8 -*-
import scrapy
from .utils import replace_symbols
from ..items import InsightItem


class InsightSpider(scrapy.Spider):
    name = 'insight'
    allowed_domains = ['insight.com']
    start_urls = ['https://www.insight.com/en_US/content-and-resources/tech-journal.html']
    base_url = 'https://www.insight.com'

    def parse(self, response):
        link = self.base_url + response.css('.btn-left::attr(href)').extract_first()

        yield scrapy.Request(link, callback=self.parse_content)

    def parse_content(self, response):
        for item in response.css('.fc-flex-item a::attr(href)').extract():
            yield scrapy.Request(self.base_url + item, callback=self.parse_article)

    def parse_article(self, response):
        items = InsightItem()

        data = response.css('.js-learn-content-column')
        text = data.css('p::text').extract()

        if len(text) != 0:
            items['link'] = response.url
            items['title'] = replace_symbols(response.css('.headline::text').extract_first())
            items['text'] = ' '.join(list(map(replace_symbols, text)))

            yield items
