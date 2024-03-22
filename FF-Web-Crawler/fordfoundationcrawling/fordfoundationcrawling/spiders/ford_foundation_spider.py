import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class FordFoundationSpider(CrawlSpider):
    name = 'fordfoundation'
    allowed_domains = ['fordfoundation.org']
    start_urls = ['https://www.fordfoundation.org/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://www.fordfoundation.org/':
            return "index.html"
        elif 'email-protection' in url:
            return "email-protection.html"

        name_split = url[:-1].split('/')
        if 'page' in name_split:
            page_index = name_split.index('page')
            file_name = f"{name_split[page_index-1]}-{name_split[page_index]}-{name_split[page_index+1]}.html"
        else:
            file_name = f"{name_split.pop()}.html"

        return file_name

    def get_page_content(self, html):
        # Removes media files and CSS selectors
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script', 'meta', 'style', 'img', 'button', 'input', 'figure', 'picture', 'select']):
            data.decompose()

        # Replaces href URL with file path
        for a in soup.findAll('a'):
            if 'href' in a.attrs:
                url = a['href']
                file_path = "/fordfoundation.org/"

                if url == 'https://www.fordfoundation.org/':
                    a['href'] = f"{file_path}index.html"

                elif '/cdn-cgi/l' in url:
                    a['href'] = f"{file_path}email-protection.html"

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

                elif (url.split('/')[0] == 'https:') and (url.split('/')[2] == 'www.fordfoundation.org') and ('pdf' not in url.split('.')):
                    directories = url[31:-1].split('/')
                    file_name = directories.pop()

                    for directory in directories:
                        file_path += f"{directory}/"

                    file_path += f"{file_name}.html"
                    a['href'] = file_path

        return soup.prettify()

    def go_to_directory(self, url):
        os.chdir('fordfoundation.org')
        directories = url[:-1].split('/')[3:]

        if (len(directories) in [0, 1]) or (directories[0] == 'cdn-cgi'):
            return
        elif 'page' in directories:
            page_index = directories.index('page')
            directories = directories[:page_index - 1]
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
        elif 'page' in directories:
            page_index = directories.index('page')
            directories = directories[:page_index - 1]
        else:
            directories.pop()

        for directory in range(len(directories)):
            os.chdir('..')

    def save_file(self, file_name, content):
        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

    def parse_item(self, response):
        url = response.request.url
        if ('preprod' in url) or ('?' in url):
            return

        # Creates a directory to save crawled pages if it doesn't already exist
        os.chdir('..')
        if not os.path.exists('fordfoundation.org'):
            os.mkdir('fordfoundation.org')

        # Gets the file name for the pages
        file_name = self.get_file_name(url)

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.get_page_content(page.content.decode())

        # Saves the content in a directory corresponding to the website
        self.go_to_directory(url)
        self.save_file(file_name, content)
        self.return_from_directory(url)
