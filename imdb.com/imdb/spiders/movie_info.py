# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
import os.path

class MovieInfoSpider(scrapy.Spider):
    name = 'movie_info'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top/']

    def parse(self, response):
    	if(response.url == self.start_urls[0]):
    		urls = response.css("td.titleColumn a::attr(href)").re("(.*)[?]")
    		links_count = 0
    		for url in urls:
    			yield scrapy.Request(urllib.parse.urljoin("http://www.imdb.com/", url))
    			links_count += 1
    			if links_count >= 10:
    				break
    	else:
    		director = response.xpath('//*[@itemprop="director"]/a/span/text()').extract()[0]
    		path = urllib.parse.urlparse(response.url).path
    		imdb_id = os.path.split(path)
    		while(imdb_id[-1] == '' and imdb_id[0] != ''):
    			imdb_id = os.path.split(imdb_id[0])
    		yield {
    			"imdb_id":imdb_id[-1],
    			'director': director 
    		}