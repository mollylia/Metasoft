import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class PhilMcNameeSpider(CrawlSpider):
    name = 'philmcnamee'
    allowed_domains = ['solitudenaturereserve.com']
    start_urls = ['https://solitudenaturereserve.com/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('solitudenaturereserve.com'):
        os.mkdir('solitudenaturereserve.com')
    os.chdir('solitudenaturereserve.com')

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://solitudenaturereserve.com/#content':
            return "index.html"
        else:
            name_split = url[:-1].split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script', 'meta', 'style', 'img', 'iframe']):
            data.decompose()

        # Replaces href URL with file path
        for a in soup.findAll('a'):
            if 'href' in a.attrs:
                url = a['href']
                file_path = "/solitudenaturereserve.com/"

                if url == 'https://solitudenaturereserve.com/':
                    a['href'] = f"{file_path}index.html"

                elif ('https://solitudenaturereserve.com/' in url) and ('png' not in url):
                    directories = url.split('/')[3:]
                    if directories[len(directories)-1] == '':
                        directories.pop()

                    file_name = directories.pop()
                    for directory in directories:
                        file_path += f"{directory}/"

                    file_path += f"{file_name}.html"
                    a['href'] = file_path

        return soup.prettify()

    def parse_item(self, response):
        url = response.request.url

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
