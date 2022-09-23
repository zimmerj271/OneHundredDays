from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
INSTAGRAM_URL = "https://www.instagram.com/"
SIMILAR_ACCOUNT = "zi4reel"
USERNAME = "korokhunter"
PASSWORD = os.environ("INSTA_PW")

class InstaFollower:
    def __init__(self):
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.maximize_window()
        self.driver.get(INSTAGRAM_URL)
        time.sleep(10)
        user_field = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Phone number, username, or email"]')
        user_field.send_keys(USERNAME)
        pw_field = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Password"]')
        pw_field.send_keys(PASSWORD)
        pw_field.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"{INSTAGRAM_URL}/{SIMILAR_ACCOUNT}/followers")
        time.sleep(10)
        pop_up = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div')
        follow_buttons = pop_up.find_elements(By.TAG_NAME, "button")
        return follow_buttons

    def follow(self, buttons):
        for button in buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                cancel_button.click()
                time.sleep(2)

