from bs4 import BeautifulSoup
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 "
                  "(KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

class ZillowScraper:
    def __init__(self, url: str):
        self.response = requests.get(url=url, headers=HEADERS)
        self.houses = {}


    def parsePage(self) -> dict:
        page_text = self.response.text
        soup = BeautifulSoup(page_text, "html.parser")
        house_cards = soup.find(id="search-page-list-container")
        listings = house_cards.find_all("li")
        for house in listings:
            try:
                link = house.find("a", class_="property-card-link")
                address = house.find("address")
                price = house.find("span", attrs={"data-test": "property-card-price"})
                self.houses[address.text] = {
                    "link": link['href'],
                    "price": price.text
                }

            except AttributeError:
                pass
            except TypeError:
                pass
        return self.houses
