import os.path
import scrapy

from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup


class MastercardFoundationSpider(scrapy.Spider):
    name = 'mastercard'
    allowed_domains = ['mastercardfdn.org']
    start_urls = ['https://mastercardfdn.org/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('mastercardfoundation.org'):
        os.mkdir('mastercardfoundation.org')
    os.chdir('mastercardfoundation.org')

    def start_requests(self):
        url = 'https://mastercardfdn.org/'
        yield SeleniumRequest(url=url, callback=self.parse_item)

    def get_file_name(self, url):
        if url == 'https://mastercardfdn.org/':
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
        # Gets the file name for the pages
        url = response.request.url
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        # Gets page content
        html_content = response.body
        content = self.get_page_content(html_content)

        # Saves page content
        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
