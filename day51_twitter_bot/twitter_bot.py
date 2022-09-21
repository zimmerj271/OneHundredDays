from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_USER = "TrackerInternet"
TWITTER_PW = os.environ("TWITTER_PW")
SERVICE = Service(executable_path=CHROME_DRIVER_PATH)
TWITTER_URL = "https://twitter.com"

class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE)
        self._tweet_button = self.twitter_login()

    def twitter_login(self):
        self.driver.maximize_window()
        self.driver.get(TWITTER_URL)
        time.sleep(10)
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in_button.click()
        time.sleep(2)
        user_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user_field.send_keys(TWITTER_USER)
        user_field.send_keys(Keys.ENTER)
        time.sleep(1)
        pw_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pw_field.send_keys(TWITTER_PW)
        pw_field.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Tweet"]')
        return tweet_button

    def tweet_at_provider(self, speeds: tuple):
        speed_down = str(speeds[0])
        speed_up = speeds[1]
        if speed_down and speed_up:
            message = f"Excellent speeds by Internet provider with {speed_down} down and {speed_up} up!"

    def say_hello(self):
        self._tweet_button.click()
        text_box = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Tweet text"]')
        text_box.send_keys("Hello!")
        send_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        send_tweet.click()

    def send_tweet(self, message):
        self._tweet_button.click()
        text_box = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Tweet text"]')
        text_box.send_keys(message)
        send_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        send_tweet.click()
