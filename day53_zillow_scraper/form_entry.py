from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

class FormEntry:
    def __init__(self, url: str):
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(10)

    def enter_data(self, data: dict):
        for address in data.keys():
            address_input = self.driver.find_element(By.XPATH,
                                                     '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH,
                                                  '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH,
                                                   '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH,
                                                     '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            link = data[address]["link"]
            price = data[address]["price"]
            print(address, price, link)
            address_input.send_keys(address)
            link_input.send_keys(link)
            price_input.send_keys(price)
            submit_button.click()
            time.sleep(3)
            new_form = self.driver.find_element(By.TAG_NAME, "a")
            new_form.click()
            time.sleep(5)
        time.sleep(10)
