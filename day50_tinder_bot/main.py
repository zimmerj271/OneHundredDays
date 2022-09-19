from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

url = "https://tinder.com"
user = {
    "Jack": 'korokhunter0@gmail.com',
    "Ava": 'miphasgrace20@gmail.com'
}
pw = os.environ("TINDER_PASSWORD")

chrome_driver_path = "/Users/zimmerj/Code/OneHundredDays/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)
time.sleep(5)
login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login.click()
time.sleep(5)
google_login = driver.find_element(By.CSS_SELECTOR, '[aria-label="Log in with Google"]')
google_login.click()
time.sleep(5)

main_window = driver.current_window_handle
driver.switch_to.window(driver.window_handles[1])

email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_field.send_keys(user['Jack'])
email_field.send_keys(Keys.ENTER)
time.sleep(10)
password_field = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_field.send_keys(pw)
password_field.send_keys(Keys.ENTER)
time.sleep(30)
driver.switch_to.window(main_window)
allow_location = driver.find_element(By.CSS_SELECTOR, '[aria-label="Allow"]')
allow_location.click()
time.sleep(2)
notifications = driver.find_element(By.CSS_SELECTOR, '[aria-label="Not interested"]')
notifications.click()
time.sleep(5)
disallow_cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button')
disallow_cookies.click()
time.sleep(5)

for card in range(100):
    reject_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
    reject_button.click()
    time.sleep(5)
