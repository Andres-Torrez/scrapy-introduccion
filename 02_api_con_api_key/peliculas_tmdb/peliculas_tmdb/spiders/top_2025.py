import scrapy
import json

class Top2025Spider(scrapy.Spider):
    name = "top_2025"

    api_key = "5f433464ffcd17cb0d2ae62e934b5168"

    def start_requests(self):
        url = (
            "https://api.themoviedb.org/3/discover/movie"
            f"?api_key={self.api_key}"
            "&primary_release_year=2025"
            "&sort_by=vote_average.desc"
            "&vote_count.gte=500"
        )
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)

        for peli in data["results"]:
            yield {
                "titulo": peli["title"],
                "fecha": peli["release_date"],
                "rating": peli["vote_average"],
                "votos": peli["vote_count"]
            }