import scrapy

class YtsSpider(scrapy.Spider):
    name = 'khabar'
    start_urls = ['https://english.onlinekhabar.com/last-24-hours']

    def parse(self, response):
        for movie in response.css('div.ok-news-post'):
            title = movie.css('div.ok-post-contents a::text').get()
            catagory = movie.css('span::text').get()
            yield {
                'title': title,
                'catagory': catagory,
            }
