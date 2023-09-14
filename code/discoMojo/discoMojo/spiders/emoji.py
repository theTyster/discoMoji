import scrapy
from discoMojo.items import Emoji


class EmojiSpider(scrapy.Spider):
    name = 'emoji'
    allowed_domains = ['discordmojis.com']
    start_urls = [
    ]


    def parse(self, response):
        emoji = Emoji()
        url_array = response.xpath("//img/@src").getall()
        emoji_csv = ""

        for i in url_array:
            i = i.split('?')[0]
            emoji_csv += "\n"
            emoji_csv += i

        emoji["emoji_links"] = emoji_csv
        return emoji
