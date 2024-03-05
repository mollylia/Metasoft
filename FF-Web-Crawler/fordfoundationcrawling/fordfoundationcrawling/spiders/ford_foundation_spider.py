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
        Rule(LinkExtractor(allow="work/"), callback="parse_item", follow=True),
        # Rule(LinkExtractor(allow="work/challenging-inequality/disability-rights"), callback="parse_item", follow=True),   # TODO: change rules later
        # Rule(LinkExtractor(), callback="parse_item", follow=True)
    )

    def remove_media_files(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for data in soup(["style", "script", "meta", "img", "button", "input", "figure", "picture", "select"]):
            data.decompose()

        return soup.prettify()

    def get_file_name(self, url, crawl_depth):
        if crawl_depth == 1:
            return "index.html"

        name_split = url.split("/")
        file_name = name_split[len(name_split)-2] + ".html"
        return file_name

    def parse_item(self, response):
        title = response.css(".alignwide h1::text").get()

        # Creates a directory to save crawled pages if it doesn't exist
        if not os.path.exists("fordfoundation.org"):
            os.mkdir("fordfoundation.org")


        url = response.request.url
        crawl_depth = response.meta["depth"]
        file_name = self.get_file_name(url, crawl_depth)
        page = requests.get(url)
        content = self.remove_media_files(page.content.decode())

        # with open(file_name, 'w') as html_file:
        #     html_file.write(str(content))

        yield {
            "file name": file_name,
            "url": url,
            "crawl depth": crawl_depth
        }
