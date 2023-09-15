import scrapy

class EmojiSpider(scrapy.Spider):
    name = 'emoji'
    start_urls = ["https://discordmojis.com/"]


    def parse(self, response):

        for link in response.xpath('//div[@class="seemore"]/a/@href').getall():
            yield response.follow(link, callback=self.parse)

            for e in response.xpath("//img/@src").getall():
                e = e.split('?')[0]
                yield {
                    'emoji urls' : e
                }
