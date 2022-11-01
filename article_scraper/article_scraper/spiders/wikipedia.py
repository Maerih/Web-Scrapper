import scrapy
from article_scraper.items import Article

class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Bob_Marley', 'https://en.wikipedia.org/wiki/Marcus_Garvey']
    

    def parse(self, response):
        return {
            'title': response.xpath('//h1/text()').get(),
            'url' : response.url,
	    'last_edited': response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        }
        article = Article()
        article['title'] = response.xpath('//h1/text()').get()
        article['url'] = response.url
        article['lastUpdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get
        return article
