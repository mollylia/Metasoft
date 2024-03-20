import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class PhilMcNameeSpider(CrawlSpider):
    name = 'philmcnamee'
    allowed_domains = ['solitudenaturereserve.com']
    start_urls = ['https://solitudenaturereserve.com/']

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

    def go_to_directory(self, url):
        os.chdir('solitudenaturereserve.com')
        directories = url[:-1].split('/')[3:]

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
        os.chdir('..')
        if not os.path.exists('solitudenaturereserve.com'):
            os.mkdir('solitudenaturereserve.com')

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
