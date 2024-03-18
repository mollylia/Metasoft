import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class LillyEndowmentSpider(CrawlSpider):
    name = 'lillyendowment'
    allowed_domains = ['lillyendowment.org']
    start_urls = ['https://lillyendowment.org/']

    os.chdir('..')
    if not os.path.exists('lillyendowment.org'):
        os.mkdir('lillyendowment.org')
    os.chdir('lillyendowment.org')

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://lillyendowment.org':
            return "index.html"
        else:
            name_split = url[:-1].split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    # def get_page_content(self, html):
    #     soup = BeautifulSoup(html, 'html.parser')
    #     for data in soup(['script']):
    #         data.decompose()
    #
    #     return soup.prettify()

    def parse_item(self, response):
        url = response.request.url

        # Gets the file name for the pages
        file_name = self.get_file_name(url)

        # Get the content from the crawled pages
        # page = requests.get(url)
        # content = self.get_page_content(page.content.decode())
        #
        # with open(file_name, 'w') as html_file:
        #     html_file.write(str(content))

        yield {
            "file name": file_name,
            "url": url
        }
