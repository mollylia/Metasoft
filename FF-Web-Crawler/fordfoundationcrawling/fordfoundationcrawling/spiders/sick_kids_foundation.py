import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class SickKidsFoundationSpider(CrawlSpider):
    name = 'sickkids'
    allowed_domains = ['sickkidsfoundation.com']
    start_urls = ['https://www.sickkidsfoundation.com/']

    custom_settings = {
        'DEPTH_LIMIT': 5
    }

    rules = (
        Rule(LinkExtractor(allowed_domains), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://www.sickkidsfoundation.com/#main':
            return "index.html"
        else:
            name_split = url.split('/')
            if name_split[len(name_split)-1] == '':
                name_split.pop()

            file_name = f"{name_split.pop()}.html"
            return file_name

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script', 'meta', 'img', 'button', 'input']):
            data.decompose()

        return soup.prettify()

    def go_to_directory(self, url):
        os.chdir('sickkidsfoundation.com')
        directories = url.split('/')[3:]
        if directories[len(directories)-1] == '':
            directories.pop()

        if len(directories) in [0, 1]:
            return
        else:
            directories.pop()
            for directory in directories:
                if not os.path.exists(directory):
                    os.mkdir(directory)
                os.chdir(directory)

    def return_from_directory(self, url):
        directories = url[:-1].split('/')[3:]
        if directories[len(directories)-1] == '':
            directories.pop()

        if len(directories) in [0, 1]:
            return
        else:
            directories.pop()
            for directory in range(len(directories)):
                os.chdir('..')

    def save_file(self, file_name, content):
        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

    def parse_item(self, response):
        url = response.request.url
        if ('?' in url) or ('https://www.sickkidsfoundation.com/' not in url):
            return

        os.chdir('..')
        if not os.path.exists('sickkidsfoundation.com'):
            os.mkdir('sickkidsfoundation.com')

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
