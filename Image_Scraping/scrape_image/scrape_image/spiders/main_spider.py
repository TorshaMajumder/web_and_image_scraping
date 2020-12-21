from ..items import ScrapeImageItem
import scrapy

class MainSpider(scrapy.Spider):

    name = "my_spider"
    start_urls = ["https://rubikscode.net/blog/"]

    def parse(self, response):
        image = ScrapeImageItem()
        img_urls = []

        for img in response.css(".entry-featured-image-url img::attr(src)").extract():
            img_urls.append(img)

        image["image_urls"] = img_urls
        return image
