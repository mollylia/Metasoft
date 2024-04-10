import os.path

import scrapy
from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup


class FoundationSearchSpider(scrapy.Spider):
    name = 'foundationsearch'
    # allowed_domains = ['fordfoundation.org', 'lillyendowment.org']
    # start_urls = ['https://www.fordfoundation.org/', 'https://lillyendowment.org/']

    allowed_domains = ['fordfoundation.org', 'lillyendowment.org', 'mastercardfdn.org', 'solitudenaturereserve.com',
                       'azrielifoundation.org', 'fondationchagnon.org', 'jcfmontreal.org', 'fcm.ca',
                       'vancouverfoundation.ca', 'sickkidsfoundation.com', 'giftfunds.com']
    start_urls = ['https://www.fordfoundation.org/', 'https://lillyendowment.org/', 'https://mastercardfdn.org/',
                  'https://solitudenaturereserve.com/', 'https://azrielifoundation.org/',
                  'https://fondationchagnon.org/en/', 'https://jcfmontreal.org/', 'https://www.fcm.ca/en/',
                  'https://www.vancouverfoundation.ca/', 'https://www.sickkidsfoundation.com/',
                  'https://www.giftfunds.com/']

    # allowed_domains = ['fordfoundation.org']
    # start_urls = ['https://www.fordfoundation.org/']

    # allowed_domains = ['lillyendowment.org']
    # start_urls = ['https://lillyendowment.org/']

    # allowed_domains = ['mastercardfdn.org']
    # start_urls = ['https://mastercardfdn.org/']

    # allowed_domains = ['solitudenaturereserve.com']
    # start_urls = ['https://solitudenaturereserve.com/']

    # allowed_domains = ['azrielifoundation.org']
    # start_urls = ['https://azrielifoundation.org/']

    # allowed_domains = ['fondationchagnon.org']
    # start_urls = ['https://fondationchagnon.org/en/']

    # allowed_domains = ['jcfmontreal.org']
    # start_urls = ['https://jcfmontreal.org/']

    # allowed_domains = ['fcm.ca']
    # start_urls = ['https://www.fcm.ca/en/']

    # allowed_domains = ['vancouverfoundation.ca']
    # start_urls = ['https://www.vancouverfoundation.ca/']

    # allowed_domains = ['sickkidsfoundation.com']
    # start_urls = ['https://www.sickkidsfoundation.com/']

    # allowed_domains = ['giftfunds.com']
    # start_urls = ['https://www.giftfunds.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse_item)

    def get_file_name(self, url, crawl_depth):
        if crawl_depth == 0:
            return "index.html"
        elif 'email-protection' in url:
            return "email-protection.html"
        elif url[-1] == '/':
            url = url[:-1]

        name_split = url.split('/')
        file_name = f"{name_split.pop()}.html"
        return file_name

    def get_page_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script']):
            data.decompose()

        return soup.prettify()

    def go_to_directory(self, url, root):
        os.chdir(root)
        directories = url[:-1].split('/')[3:]
        if (len(directories) in [0, 1]) or ('email-protection' in url):
            return
        else:
            directories.pop()
            for directory in directories:
                if not os.path.exists(directory):
                    os.mkdir(directory)
                os.chdir(directory)

    def return_from_directory(self, url):
        directories = url[:-1].split('/')[3:]
        if (len(directories) in [0, 1]) or ('email-protection' in url):
            return
        else:
            directories.pop()
            for directory in range(len(directories)):
                os.chdir('..')

    def save_file(self, file_name, content):
        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

    def parse_item(self, response):
        # Skips parsing for unrelated redirected pages: not an allowed domain, is a subdomain, or contains media files
        url = response.request.url
        if not any(domain in url for domain in self.allowed_domains):
            return
        elif ('www.' not in url) and (any(f".{domain}" in url for domain in self.allowed_domains)):
            return
        elif 'wp-content' in url:
            return

        # Gets the file name for the pages
        crawl_depth = response.meta['depth']
        file_name = self.get_file_name(url, crawl_depth)

        # Gets page content
        html_content = response.body
        content = self.get_page_content(html_content)

        # Saves page content in a directory corresponding to the website
        os.chdir('..')
        directory = url.split('/')[2].replace('www.', '')

        if not os.path.exists(directory):
            os.mkdir(directory)

        self.go_to_directory(url, directory)
        self.save_file(file_name, content)
        self.return_from_directory(url)

        yield {
            "file name": file_name,
            "url": url,
            "depth": crawl_depth
        }

        if crawl_depth < self.settings.get('DEPTH_LIMIT'):
            soup = BeautifulSoup(html_content, 'html.parser')

            for link in soup.find_all('a', href=True):
                next_url = response.urljoin(link['href'])
                languages = ['/fr', '/he']
                substrings = ['?', 'pdf', 'png', 'jpg', 'jpeg', 'mp4', 'xlsx', 'docx', 'pptx', 'zip', 'mailto', '/fr/', '/he/']

                # Skips external links, filters, pdfs, and images
                if ((next_url.startswith(tuple(self.start_urls))) and (not next_url.endswith(tuple(languages)))
                        and (not any(substring in next_url for substring in substrings))):
                    yield SeleniumRequest(url=next_url, callback=self.parse_item)
