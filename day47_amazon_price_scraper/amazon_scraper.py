import requests
from bs4 import BeautifulSoup
# from pprint import pprint

class Scraper:
    def __init__(self, url, price_limit):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Accept-Language": "en-US",
        }
        self.url = url
        self.price_limit = price_limit
        self.price = 100000  # Set default value to a high value

    def getPageText(self):
        print(f"scraping from {self.url}")
        response = requests.get(url=self.url, headers=self.headers)
        return BeautifulSoup(response.text, "lxml")

    def scrapeAWS(self):
        soup = self.getPageText()
        try:
            span = soup.find(name="span", class_="a-price")
            price = span.findChild(name="span", class_="a-offscreen").text
            price = float(price[1:])
            self.price = price
            print(self.price)
            return self.price
        except AttributeError:
            print("Price was not found")
        except TypeError:
            print("Price was not found")

    def scrapeCamel(self):
        soup = self.getPageText()
        try:
            span = soup.find(name="span", class_="green")
            price = span.text
            price = float(price[1:])
            self.price = price
            print(self.price)
            return self.price
        except AttributeError:
            print("Price was not found")
        except TypeError:
            print("Price was not found")


    def priceCheck(self):
        return self.price <= self.price_limit



# with open("price.txt", mode="w", encoding="utf-8") as file:
#     pprint(soup, stream=file)

