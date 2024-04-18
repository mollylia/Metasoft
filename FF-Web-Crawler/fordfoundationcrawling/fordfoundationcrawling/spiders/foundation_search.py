import os.path
import datetime
import scrapy
import csv

from scrapy_selenium import SeleniumRequest
from scrapy.exceptions import IgnoreRequest
from bs4 import BeautifulSoup


class FoundationSearchSpider(scrapy.Spider):
    name = 'foundationsearch'
    allowed_domains = []
    start_urls = []
    foundation_dictionary = {}

    # csv_file = 'FS.CA-Top3-URLs.csv'
    # csv_file = 'FS.CA-Top3-URLs-with-invalid.csv'
    # csv_file = 'FS.CA-Top3-URLs-403.csv'
    # csv_file = 'FS.CA-Initial-12-URLs.csv'
    # csv_file = 'FS.CA-Top20-URLs.csv'
    # csv_file = 'FS.CA-Top10.1-URLs.csv'
    csv_file = 'FS.CA-tgwhf.csv'

    handle_httpstatus_list = [301]
    substrings = ['?', 'pdf', 'png', 'jpg', 'jpeg', 'mp4', 'xlsx', 'docx', 'pptx', 'zip', 'mail', 'tel', 'fax', 'javascript', '/fr/', '/he/']
    starting_time = datetime.datetime.now()
    ending_time = starting_time

    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs)
        self.start_time = datetime.datetime.now()
        self.load_csv()
        print(f"allowed domains: {self.allowed_domains}")
        print(f"start urls: {self.start_urls}")

    def closed(self, response):
        self.write_summary()

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse_item, errback=self.handle_error, meta={'url': url})

    def handle_error(self, failure):
        self.logger.error('ERROR!!')
        self.logger.error(repr(failure))
        url = failure.request.meta['url']
        domain = url.split('/')[2].replace('www.', '')

        if domain in self.allowed_domains:
            self.allowed_domains.remove(domain)
            self.foundation_dictionary[domain][2] = -1
            raise IgnoreRequest(f"Ignoring subsequent requests related to {url}")

    def parse_item(self, response):
        url = response.request.url
        domain = url.split('/')[2].replace('www.', '')
        crawl_depth = response.meta['depth']

        if ':' in domain:
            domain = domain.split(':')[0]

        if (response.status == 301) and (domain not in self.allowed_domains) and (crawl_depth == 0):
            print("  301 REDIRECT!!")
            self.allowed_domains.append(domain)
            url_original = response.meta['url']
            domain_original = url_original.split('/')[2].replace('www.', '')
            self.foundation_dictionary[domain] = self.foundation_dictionary[domain_original]
            del self.foundation_dictionary[domain_original]

        elif (response.status == 403) and (domain in self.allowed_domains):
            self.allowed_domains.remove(domain)
            self.foundation_dictionary[domain][2] = -1
            raise IgnoreRequest(f"403: Ignoring subsequent requests related to {url}")

        # Skips parsing for unrelated redirected pages: not an allowed domain, is a subdomain, or contains media files
        if not any(domain in url for domain in self.allowed_domains):
            return
        elif ('www.' not in url) and (any(f".{domain}" in url for domain in self.allowed_domains)):
            return
        elif 'wp-content' in url:
            return

        os.chdir('..')
        directory = self.foundation_dictionary[domain][0]

        if not os.path.exists(directory):
            os.mkdir(directory)

        # Gets the file name for the pages
        file_name = self.get_file_name(url, crawl_depth)

        # Gets page content
        html_content = response.body
        content = self.get_page_content(html_content, directory)

        # Increment foundation_dictionary counter
        self.foundation_dictionary[domain][2] = self.foundation_dictionary[domain][2] + 1

        # Saves page content in a directory corresponding to the website
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

                # Skips external links, filters, pdfs, and images
                if ((any(domain in url for domain in self.allowed_domains)) and (not next_url.endswith(tuple(languages)))
                        and (not any(substring in next_url for substring in self.substrings))):
                    yield SeleniumRequest(url=next_url, callback=self.parse_item)

    def load_csv(self):
        csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', self.csv_file)
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)                        # Skips the header row
            for row in csv_reader:
                # Populates start_urls and allowed_domains
                if 'http' not in row[0]:
                    url = f'http://{row[0]}'
                else:
                    url = row[0]

                domain = url.split('/')[2].replace('www.', '')
                self.start_urls.append(url)
                self.allowed_domains.append(domain)

                # Populates foundation_dictionary with domain as key and a list of values (domain: [id, url, counter])
                self.foundation_dictionary[domain] = [row[1], url, 0]

    def write_summary(self):
        os.chdir('..')
        fields = ['OrgID', 'URL', 'NumPagesCrawled']
        with open('result-summary.csv', 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(fields)
            for key in self.foundation_dictionary.keys():
                csvwriter.writerow(self.foundation_dictionary[key])

            self.ending_time = datetime.datetime.now()
            duration = (self.ending_time - self.starting_time).total_seconds()
            file.write(f"\nTime for spider to complete: {str(duration)} seconds")

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

    def get_page_content(self, html, root):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(['script', 'meta', 'style', 'img', 'picture', 'figure', 'video', 'iframe', 'input', 'button', 'select']):
            data.decompose()

        # Replaces href URL with file path
        for a in soup.findAll('a'):
            if 'href' in a.attrs:
                url = a['href']
                file_path = f"/{root}/"

                if any(substring in url for substring in self.substrings):          # Skips media files and other languages
                    continue
                elif (url in self.start_urls) or (f'{url}/' in self.start_urls):    # Handles URLs representing index pages
                    a['href'] = f"{file_path}index.html"
                elif url in ['/', '/en']:                                           # Handles URLs representing index pages
                    a['href'] = f"{file_path}index.html"
                elif 'email-protection' in url:                                     # Handles URLs representing email protection pages
                    a['href'] = f"{file_path}email-protection.html"

                elif any(href in url for href in self.start_urls):                  # Handles URLs belonging to the same website
                    if url and url[-1] == '/':
                        url = url[:-1]
                    directories = url.split('/')[3:]
                    if directories:
                        file_name = directories.pop()
                        for directory in directories:
                            file_path += f"{directory}/"

                        file_path += f"{file_name}.html"
                        a['href'] = file_path

                elif url and url[0] == '/':                                         # Handles relative URLs within the same domain
                    if url and url[-1] == '/':
                        url = url[:-1]
                    url = url[1:]
                    file_path += f"{url}.html"
                    a['href'] = file_path

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
