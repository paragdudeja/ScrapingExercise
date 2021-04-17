# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GrantsinfoItem(scrapy.Item):
    # define the fields for your item here like:
    fund_title = scrapy.Field()
    summary = scrapy.Field()
    opportunity_status = scrapy.Field()
    award_range = scrapy.Field()
