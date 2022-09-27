from bs4 import BeautifulSoup
import requests




class ZillowScraper:
    def __init__(self, website):
        self.response = requests.get(website)

    def parsePage(self):
        page_text = self.response.text
        soup = BeautifulSoup(page_text, "html.parser")
        # house_cards = soup.find(id="search-page-list-container")
        print(soup)