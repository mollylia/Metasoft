import os.path

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SickKidsFoundationSpider(CrawlSpider):
    name = 'sickkids'
    allowed_domains = ['sickkidsfoundation.com']
    start_urls = ['https://www.sickkidsfoundation.com/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('sickkidsfoundation.com'):
        os.mkdir('sickkidsfoundation.com')
    os.chdir('sickkidsfoundation.com')

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    rules = (
        Rule(LinkExtractor(allowed_domains), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://www.sickkidsfoundation.com/#main':
            return "index.html"
        else:
            name_split = url.split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def parse_item(self, response):
        url = response.request.url
        if ('?' in url) or ('https://www.sickkidsfoundation.com/' not in url):
            return

        # Gets the file name for the pages
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
