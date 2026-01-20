import scrapy

class ProductosSpider(scrapy.Spider):
    name = "productos"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for producto in response.css("article.product_pod"):
            yield {
                "titulo": producto.css("h3 a::attr(title)").get(),
                "precio": producto.css("p.price_color::text").get()
            }
