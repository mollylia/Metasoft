import os.path

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MastercardFoundationSpider(CrawlSpider):
    name = 'mastercard'
    allowed_domains = ['mastercardfdn.org']
    start_urls = ['https://mastercardfdn.org/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('mastercardfoundation.org'):
        os.mkdir('mastercardfoundation.org')
    os.chdir('mastercardfoundation.org')

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://mastercardfdn.org/':
            return "index.html"
        else:
            name_split = url[:-1].split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def parse_item(self, response):
        url = response.request.url

        # Gets the file name for the pages
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
