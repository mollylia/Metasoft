import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

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
        'DEPTH_LIMIT': 1
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

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script', 'meta', 'style', 'img', 'button', 'input']):
            data.decompose()

        # Replaces href URL with file path
        for a in soup.findAll('a'):
            if 'href' in a.attrs:
                url = a['href']
                file_path = "/vancouverfoundation.ca/"

                if url == 'https://www.vancouverfoundation.ca/':
                    a['href'] = f"{file_path}index.html"

                elif url.split('/')[0] == '':
                    directories = url[1:].split('/')
                    if directories[len(directories)-1] == '':
                        directories.pop()

                    if directories:
                        file_name = directories.pop()
                        for directory in directories:
                            file_path += f"{directory}/"

                        file_path += f"{file_name}.html"
                        a['href'] = file_path

                elif 'https://www.vancouverfoundation.ca/' in url:
                    directories = url.split('/')[3:-1]
                    if directories:
                        file_name = directories.pop()

                        for directory in directories:
                            file_path += f"{directory}/"

                        file_path += f"{file_name}.html"
                        a['href'] = file_path

        return soup.prettify()

    def parse_item(self, response):
        url = response.request.url
        if ('?' in url) or ('/l/' in url) or ('/e/' in url) or ('/s/' in url) or ('.zip' in url):
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
