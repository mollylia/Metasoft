import os.path

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class FCMSpider(CrawlSpider):
    name = 'fcm'
    allowed_domains = ['fcm.ca']
    start_urls = ['https://www.fcm.ca/en/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('fcm.ca'):
        os.mkdir('fcm.ca')
    os.chdir('fcm.ca')

    custom_settings = {
        'DEPTH_LIMIT': 3
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://www.fcm.ca/en#main-content':
            return "index.html"
        else:
            name_split = url.split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def parse_item(self, response):
        url = response.request.url
        if ('?' in url) or ('https://www.fcm.ca/en' not in url):
            return

        # Gets the file name for the pages
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
