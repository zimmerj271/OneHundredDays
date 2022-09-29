from zillow_scraper import ZillowScraper
from form_entry import FormEntry

GOOGLE_FORM = "https://forms.gle/Ki8jNcSnpXz6nKB47"
ZILLOW_SEARCH = "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-116.56796188128328%2C%22east%22%3A-116.0632774330411%2C%22south%22%3A43.46493891205879%2C%22north%22%3A43.72502139346523%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sch%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22max%22%3A500000%7D%2C%22mp%22%3A%7B%22max%22%3A2486%7D%2C%22beds%22%3A%7B%22min%22%3A4%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%2C%22sqft%22%3A%7B%22min%22%3A2000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22customRegionId%22%3A%2268d40632faX1-CR1ijmaee5jgwou_101x2x%22%7D"
zillow_scraper = ZillowScraper(url=ZILLOW_SEARCH)
house_data = zillow_scraper.parsePage()

form_entry = FormEntry(url=GOOGLE_FORM)
form_entry.enter_data(data=house_data)