import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class AzrieliFoundationSpider(CrawlSpider):
    name = 'azrieli'
    allowed_domains = ['azrielifoundation.org']
    start_urls = ['https://azrielifoundation.org/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('azrielifoundation.org'):
        os.mkdir('azrielifoundation.org')
    os.chdir('azrielifoundation.org')

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://azrielifoundation.org/':
            return "index.html"
        else:
            name_split = url[:-1].split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script', 'meta', 'style', 'img']):
            data.decompose()

        # Replaces href URL with file path
        for a in soup.findAll('a'):
            if 'href' in a.attrs:
                url = a['href']
                file_path = "/azrielifoundation.org/"

                if (url == 'http://www.azrielifoundation.org') or (url == 'https://architectureprize.azrielifoundation.org/'):
                    a['href'] = f"{file_path}index.html"

                elif ('https://azrielifoundation.org/' in url) or ('https://architectureprize.azrielifoundation.org/' in url):
                    directories = url.split('/')[3:]
                    if directories[len(directories)-1] == '':
                        directories.pop()

                    file_name = directories.pop()
                    for directory in directories:
                        file_path += f"{directory}/"

                    file_path += f"{file_name}.html"
                    a['href'] = file_path

        return soup.prettify()

    def save_file(self, file_name, content):
        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

    def parse_item(self, response):
        url = response.request.url
        if ('/fr/' in url) or ('/he/' in url) or ('?' in url):
            return

        # Gets the file name for the pages
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.get_page_content(page.content.decode())

        # Saves the content in a directory corresponding to the website
        self.save_file(file_name, content)

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }
