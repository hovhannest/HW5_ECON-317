# -*- coding: utf-8 -*-
import scrapy
import urllib.parse

class PythonQuestionsSpider(scrapy.Spider):
    name = 'python_questions'
    allowed_domains = ['stackoverflow.com']
    start_urls = [
    'https://stackoverflow.com/questions/tagged/python/?page=1&sort=newest&pageSize=50',
    'https://stackoverflow.com/questions/tagged/python/?page=2&sort=newest&pageSize=50',
    'https://stackoverflow.com/questions/tagged/python/?page=3&sort=newest&pageSize=50'
    ]

    def parse(self, response):
        questions = response.xpath('//*[@class="question-summary"]/div[2]/h3')
        for question in questions:
        	yield {
        		'Question': question.xpath("a/text()").extract()[0],
        		'URL': urllib.parse.urljoin("https://stackoverflow.com/", question.xpath("a/@href").extract()[0])
        	}
