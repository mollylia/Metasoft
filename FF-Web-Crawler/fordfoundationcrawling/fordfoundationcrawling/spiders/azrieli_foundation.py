import os.path

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AzrieliFoundationSpider(CrawlSpider):
    name = 'azrieli'
    allowed_domains = ['azrielifoundation.org']
    start_urls = ['https://azrielifoundation.org/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('azrielifoundation.org'):
        os.mkdir('azrielifoundation.org')
    os.chdir('azrielifoundation.org')

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://azrielifoundation.org/':
            return "index.html"
        else:
            name_split = url[:-1].split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def parse_item(self, response):
        url = response.request.url
        if ('/fr/' in url) or ('/he/' in url) or ('?' in url):
            return

        # Gets the file name for the pages
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
