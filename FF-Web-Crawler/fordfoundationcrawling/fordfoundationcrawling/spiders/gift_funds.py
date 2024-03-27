import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class SickKidsFoundationSpider(CrawlSpider):
    name = 'giftfunds'
    allowed_domains = ['giftfunds.com']
    start_urls = ['https://www.giftfunds.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://www.giftfunds.com/':
            return "index.html"
        else:
            name_split = url[:-1].split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script', 'meta', 'img', 'button', 'select']):
            data.decompose()

        # Replaces href URL with file path
        for a in soup.findAll('a'):
            if 'href' in a.attrs:
                url = a['href']
                file_path = "/giftfunds.com/"

                if url == '/':
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

        return soup.prettify()

    def go_to_directory(self, url):
        os.chdir('giftfunds.com')
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
        os.chdir('..')
        if not os.path.exists('giftfunds.com'):
            os.mkdir('giftfunds.com')

        # Gets the file name for the pages
        url = response.request.url
        file_name = self.get_file_name(url)

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.get_page_content(page.content.decode())

        # Saves the content in a directory corresponding to the website
        self.go_to_directory(url)
        self.save_file(file_name, content)
        self.return_from_directory(url)
