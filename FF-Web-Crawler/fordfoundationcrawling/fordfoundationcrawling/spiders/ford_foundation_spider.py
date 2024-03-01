import os.path

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class FordFoundationSpider(CrawlSpider):
    name = "fordfoundation"
    allowed_domains = ["fordfoundation.org"]
    start_urls = ["https://www.fordfoundation.org/"]

    custom_settings = {
        "DEPTH_LIMIT": 3
    }

    rules = (
        Rule(LinkExtractor(allow="work/"), callback="parse_item", follow=True),   # TODO: change rules later
        # Rule(LinkExtractor(), callback="parse_item", follow=True)
    )

    def parse_item(self, response):
        title = response.css(".alignwide h1::text").get()

        # Creates a directory to save crawled pages if it doesn't exist
        if not os.path.exists("fordfoundation.org"):
            os.mkdir("fordfoundation.org")

        url_path = response.request.url
        ford_directory = url_path[31:-1]
        name_split = url_path.split("/")
        file_name = name_split[len(name_split)-2] + ".html"


        yield {
            "directory": ford_directory,
            "file": file_name,
            "title": title
        }
