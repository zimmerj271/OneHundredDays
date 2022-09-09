from bs4 import BeautifulSoup
import requests
import re

website = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(website)
page_text = response.text
soup = BeautifulSoup(page_text, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")
# movies = [tuple(title.text.split(') ')) for title in movie_titles]
movies = [tuple(re.split('[):] ', title.text)) for title in movie_titles]
sorted_movies = sorted(movies, key=lambda x: x[0])
with open("top_movies.txt", "w", encoding='utf-8') as file:
    for movie in sorted_movies:
        file.write(f"{movie[0]}) {movie[1]}\n")

