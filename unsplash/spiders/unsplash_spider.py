import scrapy
from scrapy.exceptions import CloseSpider

class UnsplashSpider(scrapy.Spider):
    name = 'asdf'
    # allowed_domains = ['x']
    # start_urls = ['http://x/']
    def start_requests(self):
        # self.search_term = getattr(self, 'search_term', None)
        if not self.search_term:
            raise CloseSpider('Search term missing')
        
        url='https://unsplash.com/napi/search/photos?query={}&per_page=20&page={}'
        for i in range(2):
            yield scrapy.Request(url=url.format(self.search_term,i),callback=self.parse)
            
    def parse(self, response):
        for result in response.json().get('results'):
            yield {
                'image_urls' :[result.get('urls')['full']], #must be list
                'kind':'full',
                'id':result.get('id'),
                'search':self.search_term,
                'tags' : [t.get('title') for t in result.get('tags_preview')]
            }
