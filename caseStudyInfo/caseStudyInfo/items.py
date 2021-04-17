# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CasestudyinfoItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    detail_link = scrapy.Field()
    challenge = scrapy.Field()
    solution = scrapy.Field()
    business = scrapy.Field()
    expertise = scrapy.Field()
