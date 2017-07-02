# -*- coding: utf-8 -*-
import scrapy
import urllib.parse


class TopMoviesSpider(scrapy.Spider):
    name = 'top_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top']

    def parse(self, response):
        rank = response.css("td.titleColumn::text").re("\d+")
        #re(".*(\d+).+")
        title = response.css("td.titleColumn a::text").extract()
        url = response.css("td.titleColumn a::attr(href)").re("(.*)[?]")
        info = response.css("td.titleColumn a::attr(title)").re("(.*)\s+\(dir.\)")
        #(.*)\s+\(dir.\)
        year = response.css("td.titleColumn span.secondaryInfo::text").extract()
        rating = response.css("td.ratingColumn strong::text").extract()
        raters = response.css("td.ratingColumn strong::attr(title)").re("on\s+([0-9+,]+)\s+user")
        if(len(title) == len(url) == len(info) == len(year) == len(rating) == len(rank)):
        	sum_rationg = 0.0
        	l = len(title)
        	for i in range(l):
        		r = float(rating[i])
        		sum_rationg += r
        		yield {
        			"rank": int(float(rank[i])),
        			"title": title[i],
        			"url": urllib.parse.urljoin("http://www.imdb.com/", url[i]),
        			"year": int(float(year[i].replace("(", "").replace(")",""))),
        			"rating": r,
        			"director": info[i]
        		}
        	if(l > 0):
        		yield { "average rating": sum_rationg/l}
