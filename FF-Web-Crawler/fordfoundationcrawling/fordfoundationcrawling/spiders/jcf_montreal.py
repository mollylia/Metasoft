import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

class JCFMontrealSpider(CrawlSpider):
    name = 'jcfmontreal'
    allowed_domains = ['jcfmontreal.org']
    start_urls = ['https://jcfmontreal.org/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('jcfmontreal.org'):
        os.mkdir('jcfmontreal.org')
    os.chdir('jcfmontreal.org')

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://jcfmontreal.org/#main':
            return "index.html"
        elif url == 'https://50.jcfmontreal.org/':
            return "50th-anniversary.html"
        elif 'email-protection' in url:
            return "email-protection.html"
        else:
            name_split = url[:-1].split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script', 'meta', 'style', 'img', 'video', 'button', 'input', 'iframe']):
            data.decompose()

        return soup.prettify()

    def parse_item(self, response):
        url = response.request.url
        if '/fr' in url:
            return

        # Gets the file name for the pages
        file_name = self.get_file_name(url)

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.get_page_content(page.content.decode())

        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

        crawl_depth = response.meta['depth']

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
