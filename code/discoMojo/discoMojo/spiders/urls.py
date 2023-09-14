import scrapy
from discoMojo.items import Urls


class UrlsSpider(scrapy.Spider):
    name = "urls"
    allowed_domains = ["discordmojis.com"]
    start_urls = ["https://discordmojis.com/"]

    def parse(self, response):
        links = Urls()
        urls = response.xpath('//div[@class="seemore"]/a/@href').getall()
        formatted_urls = set()

        for url in urls:
            url = f'https:/discordmojis.com{url}'
            formatted_urls.add(url)

        links["emoji_pages"] = formatted_urls
        return links
