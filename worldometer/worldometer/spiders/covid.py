# -*- coding: utf-8 -*-
import scrapy


class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['www.worldometers.info/coronavirus']
    start_urls = ['http://www.worldometers.info/coronavirus/']

    def parse(self, response):

        rows = response.xpath(
            '(//tbody[1])[1]//td/a[@class="mt_a"]/parent::td//parent::tr')
        for row in rows:
            country = row.xpath(".//td[1]/a/text()").get()
            totalCase = row.xpath(".//td[2]/text()").get()
            totalDeath = row.xpath(".//td[4]/text()").get()
            totalRecovered = row.xpath(".//td[6]/text()").get()
            activeCase = row.xpath(".//td[7]/text()").get()
            seriousCritical = row.xpath(".//td[8]/text()").get()

            yield {
                "CountryName": country,
                "Total Case": totalCase,
                "Total Deaths": totalDeath,
                "Total Recovered": totalRecovered,
                "Active Cases": activeCase,
                "Critical Cases": seriousCritical
            }
