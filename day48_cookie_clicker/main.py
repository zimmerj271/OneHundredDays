from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)  # Allow time for page to load
try:
    english_select_button = driver.find_element(By.ID, "langSelect-EN")
    if english_select_button is not None:
        english_select_button.click()
    time.sleep(5)  # Allow time for page to load
except:
    print("Language Button Not Present")

cookie_button = driver.find_element(By.ID, "bigCookie")
product_buttons = driver.find_element(By.ID, "products")
product_button_list = product_buttons.find_elements(By.CLASS_NAME, "product")

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
NUM_SECONDS = 5
click_time = time.time() + NUM_SECONDS  # Time interval of 5 seconds
is_clicking = True

while is_clicking:
    cookie_button.click()
    if time.time() > click_time:
        try:
            upgrade_buttons = driver.find_element(By.ID, "upgrades")
            upgrade_button_list = upgrade_buttons.find_elements(By.CLASS_NAME, "upgrade")
            for button in upgrade_button_list:
                if button.get_attribute("class") == "crate upgrade enabled":
                    button.click()
                    break
        except IndexError:
            pass
        except StaleElementReferenceException:
            pass
        except NoSuchElementException:
            pass
        for button in reversed(product_button_list):
            if button.get_attribute("class") == "product unlocked enabled":
                button.click()
                break
        try:
            cookies_per_second = driver.find_element(By.ID, "cookiesPerSecond")
            cps = cookies_per_second.get_attribute("innerHTML")
            print(f"Cookies {cps}")
        except StaleElementReferenceException:
            pass
        except NoSuchElementException:
            pass
        click_time = time.time() + NUM_SECONDS