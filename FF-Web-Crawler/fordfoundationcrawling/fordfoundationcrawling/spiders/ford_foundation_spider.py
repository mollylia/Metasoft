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
        'DEPTH_LIMIT': 3
    }

    rules = (
        # Rule(LinkExtractor(allow="news-and-stories/"), callback="parse_item", follow=True),
        # Rule(LinkExtractor(allow="work/challenging-inequality/"), callback="parse_item", follow=True),
        # Rule(LinkExtractor(allow="work/challenging-inequality/disability-rights"), callback="parse_item", follow=True),
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def get_file_name(self, url):
        if url == 'https://www.fordfoundation.org/':
            return "index.html"

        name_split = url[:-1].split('/')
        if 'page' in name_split:
            page_index = name_split.index('page')
            file_name = f"{name_split[page_index-1]}-{name_split[page_index]}-{name_split[page_index+1]}.html"
        else:
            substrings_to_remove = ["?filter", "?query", "?grant", "?popup"]
            name_split = [item for item in name_split if not any(substring in item for substring in substrings_to_remove)]
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

                elif url.split('/')[0] == 'https:':
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
            directories = directories[:page_index-1]
        else:
            substrings_to_remove = ["?filter", "?query", "?grant", "?popup"]
            directories = [item for item in directories if not any(substring in item for substring in substrings_to_remove)]
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
            directories = directories[:page_index-1]
        else:
            substrings_to_remove = ["?filter", "?query", "?grant", "?popup"]
            directories = [item for item in directories if not any(substring in item for substring in substrings_to_remove)]
            directories.pop()

        for directory in range(len(directories)):
            os.chdir('..')

    def save_file(self, file_name, content):
        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

    def parse_item(self, response):
        os.chdir('..')

        # Creates a directory to save crawled pages if it doesn't already exist
        if not os.path.exists('fordfoundation.org'):
            os.mkdir('fordfoundation.org')

        # Gets the file name for the pages
        url = response.request.url
        crawl_depth = response.meta['depth']
        file_name = self.get_file_name(url)

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.get_page_content(page.content.decode())

        # Saves the content in a directory corresponding to the website
        self.go_to_directory(url)
        self.save_file(file_name, content)
        self.return_from_directory(url)

        # yield {
        #     "file name": file_name,
        #     "url": url
        # }
