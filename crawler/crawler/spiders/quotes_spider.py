import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    def start_requests(self):
        urls = [
            'http://www.freeproxylists.net/zh/?c=US&page=1',
        ]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        pageNumber = response.url.split('/')[-2]
        filename = 'vpns_{}.html'.format(pageNumber)
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('page:{} saved'.format(pageNumber))

