from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

EXPECTED_DOWN_SPEED = 20
EXPECTED_UP_SPEED = 20
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SERVICE = Service(executable_path=CHROME_DRIVER_PATH)
INTERNET_SPEED_URL = "https://www.speedtest.net"


class InternetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get(INTERNET_SPEED_URL)
        time.sleep(10)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)
        down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = float(down_speed.text)
        self.up = float(up_speed.text)
        internet_speeds = (self.down, self.up)
        return internet_speeds

    def check_up_speed(self):
        if self.up > EXPECTED_UP_SPEED:
            return True
        return False

    def check_down_speed(self):
        if self.down > EXPECTED_DOWN_SPEED:
            return True
        return False
