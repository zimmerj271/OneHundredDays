import os
import requests
import pickle


class MovieSearch:
    # tmdb_api_key = os.environ["TMDB_API_KEY"]
    tmdb_api_key = '262e8bff1facc96ed9f3beef0d4dcfad'
    # tmdb_token = os.environ["TMDB_TOKEN"]
    tmdb_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNjJlOGJmZjFmYWNjOTZlZDlmM2JlZWYwZDRkY2ZhZCIsInN1YiI6IjYzN2Q2MzNlNzVmMWFkMDBmY2YzOTU3ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YfTuUZ2J_QF6xFTmMaRYDSFe5bOwIPPhTZJLxcmai2Q'
    endpoint = "https://api.themoviedb.org/4"

    def __init__(self):
        # API Token is added to request header
        self.headers = {"Authorization": f"Bearer {MovieSearch.tmdb_token}"}

    def search_movie(self, movie: str) -> list:
        # Note if using API key, need to add to the search query with keyword 'api_key'
        search_endpoint = f"{MovieSearch.endpoint}/search/movie"
        query = {
            "language": "en-US",
            "query": movie,
            "include_adult": "false"
        }
        response = requests.get(url=search_endpoint, headers=self.headers, params=query)
        data = response.json()
        return data['results']

    def get_poster(self, backdrop_path: str) -> str:
        poster_url = f"https://image.tmdb.org/t/p/w500/{backdrop_path}"
        return poster_url

