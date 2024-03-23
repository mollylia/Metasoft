import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class JCFMontrealSpider(CrawlSpider):
    name = 'jcfmontreal'
    allowed_domains = ['jcfmontreal.org']
    start_urls = ['https://jcfmontreal.org/']

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

        # Replaces href URL with file path
        for a in soup.findAll('a'):
            if 'href' in a.attrs:
                url = a['href']
                file_path = "/jcfmontreal.org/"

                if url == 'https://jcfmontreal.org/':
                    a['href'] = f"{file_path}index.html"

                elif '/cdn-cgi/l' in url:
                    a['href'] = f"{file_path}email-protection.html"

                elif 'https://jcfmontreal.org/' in url:
                    directories = url[:-1].split('/')[3:]
                    if directories:
                        file_name = directories.pop()

                        for directory in directories:
                            file_path += f"{directory}/"

                        file_path += f"{file_name}.html"
                        a['href'] = file_path

        return soup.prettify()

    def go_to_directory(self, url):
        os.chdir('jcfmontreal.org')
        directories = url[:-1].split('/')[3:]

        if (len(directories) in [0, 1]) or (directories[0] == 'cdn-cgi'):
            return
        else:
            directories.pop()
            for directory in directories:
                if not os.path.exists(directory):
                    os.mkdir(directory)
                os.chdir(directory)

    def return_from_directory(self, url):
        directories = url[:-1].split('/')[3:]

        if (len(directories) in [0, 1]) or (directories[0] == 'cdn-cgi'):
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
        if '/fr' in url:
            return

        os.chdir('..')
        if not os.path.exists('jcfmontreal.org'):
            os.mkdir('jcfmontreal.org')

        # Gets the file name for the pages
        file_name = self.get_file_name(url)

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.get_page_content(page.content.decode())
        crawl_depth = response.meta['depth']

        # Saves the content in a directory corresponding to the website
        self.go_to_directory(url)
        self.save_file(file_name, content)
        self.return_from_directory(url)
