from bs4 import BeautifulSoup
import requests

# playlist_date = input("Which year do you want to travel to (YYYY-MM-DD)? ")
playlist_date = "2000-08-12"
top_songs_site = f"https://www.billboard.com/charts/hot-100/{playlist_date}/"

response = requests.get(top_songs_site)
page_text = response.text
# print(page_text)
# with open("songs.html", "w") as file:
#     file.write(page_text)
soup = BeautifulSoup(page_text, "html.parser")
listing = soup.find_all(name="li", class_="o-chart-results-list__item")
for item in listing:
    print(item)