# Crawlers and Scrapers

The goal of this session is to build and run our own scraper using the **scrapy** python library. Our scraper will crawl through different customer-review pages and get all of the available ratings and reviews.

First we will install scrapy using **pip** command in terminal/cmd:
```shell
pip install scrapy
```

Next, we'll use scrapy to automatically generate a skeleton of the code needed for our scraper. On terminal/cmd type the following:
```shell
scrapy genspider amazon_scraper amazon.com
``` 

A new python-script, **amazon_scraper.py** file will be created.
The final content of our scraper will be as follows:

```python
# -*- coding: utf-8 -*-
import scrapy

class AmazonScraperSpider(scrapy.Spider):
    name = 'amazon_scraper'
    allowed_domains = ['amazon.com']
    # assing a product-review-page url below
    start_urls = ['']
    
    def parse(self, response):
        all_text = response.css('.a-size-base.review-text')
        for i in range(len(all_text)):
            all_text[i] = " ".join(all_text[i].css('::text').extract())

        all_ratings = response.css('[data-hook="review-star-rating"] > span::text').extract()

        for i in range(len(all_text)):
            review = {
                'text' : all_text[i],
                'rating': all_ratings[i]
            }
            yield review

        next_page_url = response.css('.a-last > a::attr(href)').extract_first()
        yield response.follow(next_page_url, self.parse)
```

We can call the script from terminal/cmd as follows:

```shell
scrapy runspider amazon_scraper.py -o out.json
```
