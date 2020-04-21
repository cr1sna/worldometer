# -*- coding: utf-8 -*-
import scrapy


class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['www.worldometers.info/coronavirus']
    start_urls = ['http://www.worldometers.info/coronavirus/']

    def parse(self, response):
        pass
