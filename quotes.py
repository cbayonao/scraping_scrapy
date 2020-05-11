# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        self.log(f'Got response from: {response.url}')
        # print(f'Got response from: {response.url}')
        item = {
            'author': response.css('.author::text').get(),
            'quote': response.css('.text::text').get(),
            'tags': response.css('.tag::text').getall()
        }
        yield item
