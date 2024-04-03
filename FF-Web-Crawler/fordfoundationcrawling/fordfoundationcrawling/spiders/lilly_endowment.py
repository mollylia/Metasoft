import os.path

import scrapy
from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup


class LillyEndowmentSpider(scrapy.Spider):
    name = 'lillyendowment'
    allowed_domains = ['lillyendowment.org']
    start_urls = ['https://lillyendowment.org/']

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse_item)

    def get_file_name(self, url):
        if url == 'https://lillyendowment.org/':
            return "index.html"
        else:
            name_split = url[:-1].split('/')
            file_name = f"{name_split.pop()}.html"
            return file_name

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script', 'meta', 'style', 'img', 'iframe', 'button', 'input', 'select']):
            data.decompose()

        # Replaces href URL with file path
        for a in soup.findAll('a'):
            if 'href' in a.attrs:
                url = a['href']
                file_path = "/lillyendowment.org"

                if url == 'https://lillyendowment.org':
                    a['href'] = f"{file_path}/index.html"

                elif 'lillyendowment.org' in url:
                    directories = url.split('/')[3:]
                    if directories[len(directories)-1] == '':
                        directories.pop()

                    if directories:
                        file_name = directories.pop()
                        for directory in directories:
                            file_path += f"{directory}/"

                        file_path += f"{file_name}.html"
                        a['href'] = file_path

                elif url and url[0] == '/':
                    path = url
                    if url[-1] == '/':
                        path = url[:-1]

                    file_path += f"{path}.html"
                    a['href'] = file_path

        return soup.prettify()

    def go_to_directory(self, url):
        os.chdir('lillyendowment.org')
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
        if not os.path.exists('lillyendowment.org'):
            os.mkdir('lillyendowment.org')

        # Gets the file name for the pages
        url = response.request.url
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        # Gets page content
        html_content = response.body
        content = self.get_page_content(html_content)

        # Saves the content in a directory corresponding to the website
        self.go_to_directory(url)
        self.save_file(file_name, content)
        self.return_from_directory(url)

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }

        # if crawl_depth < self.settings.get('DEPTH_LIMIT'):
        if crawl_depth == 0:
            soup = BeautifulSoup(html_content, 'html.parser')
            for link in soup.find_all('a', href=True):
                next_url = response.urljoin(link['href'])

                if self.allowed_domains[0] in next_url:
                    yield SeleniumRequest(url=next_url, callback=self.parse_item)
