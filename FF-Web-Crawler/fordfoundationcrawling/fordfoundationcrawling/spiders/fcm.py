import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class FCMSpider(CrawlSpider):
    name = 'fcm'
    allowed_domains = ['fcm.ca']
    start_urls = ['https://www.fcm.ca/en/']

    rules = (
        Rule(LinkExtractor(allow='/en/'), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://www.fcm.ca/en':
            return "index.html"
        elif url == 'https://greenmunicipalfund.ca/':
            return "green-municipal-fund.html"
        else:
            name_split = url.split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script']):
            data.decompose()

        return soup.prettify()

    def go_to_directory(self, url):
        os.chdir('fcm.ca')
        directories = url[:-1].split('/')[3:]

        if len(directories) in [0, 1]:
            return

        directories.pop()
        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)
            os.chdir(directory)

    def return_from_directory(self, url):
        directories = url[:-1].split('/')[3:]

        if len(directories) in [0, 1]:
            return

        directories.pop()
        for directory in range(len(directories)):
            os.chdir('..')

    def save_file(self, file_name, content):
        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

    def parse_item(self, response):
        url = response.request.url
        if '?' in url:
            return

        # Creates a directory to save crawled pages if it doesn't already exist
        os.chdir('..')
        if not os.path.exists('fcm.ca'):
            os.mkdir('fcm.ca')

        # Gets the file name for the pages
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.get_page_content(page.content.decode())

        # Saves the content in a directory corresponding to the website
        self.go_to_directory(url)
        self.save_file(file_name, content)
        self.return_from_directory(url)

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
