from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class FordFoundationSpider(CrawlSpider):
    name = "fordfoundation"
    allowed_domains = ["fordfoundation.org"]
    start_urls = ["https://www.fordfoundation.org/"]

    # custom_settings = {
    #     "DEPTH_LIMIT": 3
    # }

    rules = (
        Rule(LinkExtractor(allow="work/investing-in-individuals"), callback="parse_item"),   # TODO: change rules later

    )

    def parse_item(self, response):
        yield {
            "title": response.css(".alignwide h1::text").get()
        }

