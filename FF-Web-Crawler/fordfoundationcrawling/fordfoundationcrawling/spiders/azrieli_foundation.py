import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class AzrieliFoundationSpider(CrawlSpider):
    name = 'azrieli'
    allowed_domains = ['azrielifoundation.org']
    start_urls = ['https://azrielifoundation.org/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://azrielifoundation.org/':
            return "index.html"
        elif url == 'https://memoirs.azrielifoundation.org/':
            return "index-memoirs.html"
        else:
            name_split = url.split('/')
            if name_split[len(name_split)-1] == '':
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
                elif url == 'https://memoirs.azrielifoundation.org/':
                    a['href'] = f"{file_path}index-memoirs.html"
                elif ('https://azrielifoundation.org/' in url) or ('https://architectureprize.azrielifoundation.org/' in url):
                    directories = url.split('/')[3:]
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
        os.chdir('azrielifoundation.org')
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
        url = response.request.url
        if ('/fr' in url) or ('/he' in url) or ('?' in url) or ('png' in url):
            return

        os.chdir('..')
        if not os.path.exists('azrielifoundation.org'):
            os.mkdir('azrielifoundation.org')

        # Gets the file name for the pages
        file_name = self.get_file_name(url)

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.get_page_content(page.content.decode())

        # Saves the content in a directory corresponding to the website
        self.go_to_directory(url)
        self.save_file(file_name, content)
        self.return_from_directory(url)
