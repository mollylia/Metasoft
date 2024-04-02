import os.path

import scrapy
from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup


class LillyEndowmentSpider(scrapy.Spider):
    name = 'lillyendowment'
    allowed_domains = ['lillyendowment.org']
    start_urls = ['https://lillyendowment.org/']

    # TODO: move this to parse_item
    os.chdir('..')
    if not os.path.exists('lillyendowment.org'):
        os.mkdir('lillyendowment.org')
    os.chdir('lillyendowment.org')

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

        return soup.prettify()

    def save_file(self, file_name, content):
        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

    def parse_item(self, response):
        # Gets the file name for the pages
        url = response.request.url
        file_name = self.get_file_name(url)
        crawl_depth = response.meta['depth']

        # Gets page content
        html_content = response.body
        content = self.get_page_content(html_content)

        # Saves the content
        self.save_file(file_name, content)

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
