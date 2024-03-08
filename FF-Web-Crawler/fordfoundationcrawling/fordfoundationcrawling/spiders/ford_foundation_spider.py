import os.path
import requests

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup


class FordFoundationSpider(CrawlSpider):
    name = "fordfoundation"
    allowed_domains = ["fordfoundation.org"]
    start_urls = ["https://www.fordfoundation.org/"]

    custom_settings = {
        "DEPTH_LIMIT": 3
    }

    rules = (
        Rule(LinkExtractor(allow="news-and-stories/"), callback="parse_item", follow=True),
        # Rule(LinkExtractor(allow="work/challenging-inequality/"), callback="parse_item", follow=True),
        # Rule(LinkExtractor(allow="work/challenging-inequality/disability-rights"), callback="parse_item", follow=True),
        # Rule(LinkExtractor(), callback="parse_item", follow=True),
    )

    def remove_media_files(self, html):
        soup = BeautifulSoup(html, "html.parser")
        for data in soup(["style", "script", "meta", "img", "button", "input", "figure", "picture", "select"]):
            data.decompose()

        return soup.prettify()

    def get_file_name(self, url, crawl_depth):
        if crawl_depth == 1:
            return "index.html"

        name_split = url[31:].split("/")

        if "page" in name_split:
            page_index = name_split.index("page")
            file_name = f"{name_split[page_index-1]}-{name_split[page_index]}-{name_split[page_index+1]}.html"
            return file_name
        else:
            file_name = name_split[len(name_split)-2] + ".html"
            return file_name

    def go_to_directory(self, url, crawl_depth):
        os.chdir("fordfoundation.org")
        directories = url[31:-1].split("/")

        if (crawl_depth != 1) or ("?filter_news_press_type=new" in directories):
            directories.pop()

        for directory in directories:
            if not os.path.exists(directory):
                os.mkdir(directory)

            os.chdir(directory)

    def save_file(self, file_name, content):
        with open(file_name, 'w') as html_file:
            html_file.write(str(content))

    def return_from_directory(self, url, crawl_depth):
        directories = url[31:-1].split("/")

        if (crawl_depth != 1) or ("?filter_news_press_type=new" in directories):
            directories.pop()

        for directory in directories:
            os.chdir("..")

    def parse_item(self, response):
        os.chdir("..")

        # Creates a directory to save crawled pages if it doesn't already exist
        if not os.path.exists("fordfoundation.org"):
            os.mkdir("fordfoundation.org")

        # Gets the file name for the pages
        url = response.request.url
        crawl_depth = response.meta["depth"]
        file_name = self.get_file_name(url, crawl_depth)

        # Get the content from the crawled pages
        page = requests.get(url)
        content = self.remove_media_files(page.content.decode())

        # Saves the content in a directory corresponding to the website
        self.go_to_directory(url, crawl_depth)
        self.save_file(file_name, content)
        self.return_from_directory(url, crawl_depth)

        # yield {
        #     "file name": file_name,
        #     "url": url,
        #     "crawl depth": crawl_depth
        # }
