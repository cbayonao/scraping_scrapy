# -*- coding: utf-8 -*-
import scrapy


class WikipySpider(scrapy.Spider):
    name = 'wikipy'
    start_urls = ['https://en.wikipedia.org/wiki/Python_(programming_language)']

    def parse(self, response):
        self.log(f'Obteniendo respuesta de: {response.url}')
        list_key = response.css('.tocnumber::text').getall()
        list_values = response.css('.toctext::text').getall()
        content = {}
        for key in list_key:
            for value in list_values:
                content[key] = value
                list_values.remove(value)
                break
        yield content
