import scrapy

class EmojiSpider(scrapy.Spider):
    name = 'emoji'
    start_urls = ["https://discordmojis.com/"]


    def parse(self, response):

        emojis = set()
        for e in response.xpath('//img/@src').getall():
            emojis.add(e.split('?')[0])

        for link in response.xpath('//div[@class="seemore"]/a/@href').getall():
            yield response.follow(link, callback=self.parse)


        for e in emojis:
            yield {'emoji urls' : e}
