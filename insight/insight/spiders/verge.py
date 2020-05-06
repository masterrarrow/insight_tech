import scrapy
from .utils import replace_symbols
from ..items import InsightItem


class VergeSpider(scrapy.Spider):
    name = 'verge'
    start_urls = ['https://www.theverge.com/tech']

    def parse(self, response):
        for article in response.css('.c-entry-box--compact__title a'):
            links = article.css('::attr(href)').extract()

            for link in links:
                yield scrapy.Request(link, callback=self.parse_content)

    def parse_content(self, response):
        items = InsightItem()

        for data in response.css('.l-main-content'):
            text = []
            for item in data.css('.c-entry-content').css('p'):
                text.append(' '.join(item.css('*::text').extract()))

            title = data.css('.c-page-title *::text').extract_first()

            items["link"] = response.url
            items["title"] = replace_symbols(title)
            items["text"] = ' '.join(list(map(replace_symbols, text)))

            yield items
