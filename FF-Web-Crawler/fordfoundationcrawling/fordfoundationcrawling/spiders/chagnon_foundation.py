import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class ChagnonFoundationSpider(CrawlSpider):
    name = 'chagnon'
    allowed_domains = ['fondationchagnon.org']
    start_urls = ['https://fondationchagnon.org/en/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('fondationchagnon.org'):
        os.mkdir('fondationchagnon.org')
    os.chdir('fondationchagnon.org')

    rules = (
        Rule(LinkExtractor(allow='/en/'), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://fondationchagnon.org/en/':
            return "index.html"
        else:
            name_split = url[:-1].split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script']):
            data.decompose()

        return soup.prettify()

    def parse_item(self, response):
        url = response.request.url
        if '?' in url:
            return

        # Gets the file name for the pages
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.get_page_content(page.content.decode())

        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
