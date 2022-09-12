from bs4 import BeautifulSoup
import requests

class Billboard:
    def __init__(self, date):
        self.billboard_site = f"https://www.billboard.com/charts/hot-100/{date}/"
        self.song_list = self.getSongs(self.parsePage())

    def parsePage(self):
        response = requests.get(self.billboard_site)
        page_text = response.text
        soup = BeautifulSoup(page_text, "html.parser")
        site_list = soup.find_all(name="li", class_="o-chart-results-list__item")
        return site_list

    def getSongs(self, element_list):
        song_titles = []
        artists = []
        for tag in element_list:
            song = tag.find(name="h3", class_="c-title", id="title-of-a-story")
            artist = tag.find(name="span", class_="a-no-trucate")
            if song is not None:
                song_titles.append(song.text.strip())
            if artist is not None:
                artists.append(artist.text.strip())
        return zip(song_titles, artists)
