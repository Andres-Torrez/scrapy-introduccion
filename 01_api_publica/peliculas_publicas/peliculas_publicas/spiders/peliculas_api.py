import scrapy
import json

class PeliculasApiSpider(scrapy.Spider):
    name = "peliculas_api"
    start_urls = ["https://ghibliapi.vercel.app/films"]

    def parse(self, response):
        data = json.loads(response.text)

        for peli in data:
            yield {
                "titulo": peli["title"],
                "director": peli["director"],
                "año": peli["release_date"],
                "rating": peli["rt_score"]
            }
