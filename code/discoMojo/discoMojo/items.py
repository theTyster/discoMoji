# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Emoji(scrapy.Item):
    # define the fields for your item here like:
     emoji_links = scrapy.Field()

class Urls(scrapy.Item):
    emoji_pages = scrapy.Field()
