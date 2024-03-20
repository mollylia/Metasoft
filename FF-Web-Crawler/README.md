# Ford Foundation Web Crawler
## How to deploy

```
# Make sure you are in the project directory FF-Web-Crawler

# Install frameworks
pip install scrapy
pip install beautifulsoup4

cd fordfoundationcrawling
scrapy crawl fordfoundation

# Use this if you want to see the results from yield in parse_item
scrapy crawl fordfoundation -o output.json```
