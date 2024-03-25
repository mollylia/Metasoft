import os.path

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class VancouverFoundationSpider(CrawlSpider):
    name = 'vancouver'
    allowed_domains = ['vancouverfoundation.ca']
    start_urls = ['https://www.vancouverfoundation.ca/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('vancouverfoundation.ca'):
        os.mkdir('vancouverfoundation.ca')
    os.chdir('vancouverfoundation.ca')

    custom_settings = {
        'DEPTH_LIMIT': 5
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://www.vancouverfoundation.ca/#content':
            return "index.html"

        name_split = url[:-1].split('/')
        if 'page' in url:
            page_index = name_split.index('page')
            file_name = f"{name_split[page_index-1]}-{name_split[page_index]}-{name_split[page_index+1]}.html"
        else:
            file_name = f"{name_split.pop()}.html"

        return file_name

    def parse_item(self, response):
        url = response.request.url
        if ('?' in url) or ('/l/' in url) or ('/e/' in url) or ('/s/' in url) or ('.zip' in url):
            return

        # Gets the file name for the pages
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
