from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"  # exact path to the browser driver
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# # Get price from Amazon page
# driver.get("https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-phone-call/dp/B0863TXGM3/ref=sr_1_9?crid=2ELX4ZSA819O9&keywords=sony%2Bwh-1000xm4%2Bwireless%2Bheadphones&qid=1663114993&s=electronics&sprefix=Sony%2BWH-1000XM4%2Celectronics%2C133&sr=1-9&ufe=app_do%3Aamzn1.fos.ac2169a1-b668-44b9-8bd0-5ec63b24bcb5&th=1")
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.tag_name)
# print(price.get_attribute('innerHTML'))
# # driver.close()  # closes current browser tab
# driver.quit()   # closes the entire browser

# # Get link from a page
# driver.get("https://www.python.org")
# document_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")  # use a CSS Selector to find an element 'a' inside parent element with class documentation-widget
# print(document_link.get_attribute("href"))
#
# # Get link from XPath
# # Find an XPath for an element by going to Developer Tools -> Inspect
# # then right-click on the element -> Copy -> Copy XPath
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))
#
# # Scrape all event dates from the python.org website
# event_times = driver.find_elements(By.CSS_SELECTOR, ".shrubbery time")
# event_titles = driver.find_elements(By.CSS_SELECTOR, ".shrubbery a")
# events = dict(zip(event_titles, event_times))
# for event, time in events.items():
#     event_time = time.get_attribute('datetime')[:9]
#     print(f"{event.text}, {event_time}")

# Get article count from Wikipedia page
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# driver.quit()