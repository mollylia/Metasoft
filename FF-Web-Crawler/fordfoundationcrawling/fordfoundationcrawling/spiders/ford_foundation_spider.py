import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class FordFoundationSpider(CrawlSpider):
    name = 'fordfoundation'
    allowed_domains = ['fordfoundation.org']
    start_urls = ['https://www.fordfoundation.org/']

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    rules = (
        Rule(LinkExtractor(allow='work/challenging-inequality/disability-rights'), callback='parse_item', follow=True),   # TODO: change rules later
        # Rule(LinkExtractor(), callback="parse_item", follow=True)
    )

    def remove_media_files(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        for data in soup(['style', 'script', 'meta', 'img', 'button', 'input', 'figure', 'picture', 'select']):
            data.decompose()

        return soup.prettify()
        # return soup
        # return ' '.join(soup.stripped_strings)

    def parse_item(self, response):
        title = response.css('.alignwide h1::text').get()

        # Creates a directory to save crawled pages if it doesn't exist
        if not os.path.exists('fordfoundation.org'):
            os.mkdir('fordfoundation.org')

        url = response.request.url
        page = requests.get(url)
        content = self.remove_media_files(page.content.decode())
        # content = self.remove_media_files(page.content)

        name_split = url.split('/')
        file_name = name_split[len(name_split)-2] + '.html'

        with open(file_name, 'w') as html_file:
            html_file.write(str(content))
            # html_file.write(content)
