from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

url = "https://www.linkedin.com/jobs/search/?keywords=Data%20Engineer&location=United%20States&locationId=&geoId=103644278&f_TPR=&f_WT=2&f_JT=F&position=1&pageNum=0"

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)
time.sleep(5)  # wait for page to load
sign_in_button = driver.find_element(By.CLASS_NAME, "cta-modal__primary-btn")
sign_in_button.click()

# sign-in
time.sleep(5)
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
username_field.send_keys("zimmerju@gmail.com")
password_field.send_keys("3Arnhofthi-3")
sign_in_button.click()

# Save the first 5 jobs on the list
time.sleep(5)
ul_element = driver.find_element(By.CLASS_NAME, 'scaffold-layout__list-container')
job_card_containers = ul_element.find_elements(By.CLASS_NAME, 'job-card-container')
for card in job_card_containers:
    link = card.find_element(By.CSS_SELECTOR, 'a')
    link.click()
    time.sleep(3)  # wait for link to load, needed for dynamic pages in Chrome
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()  # click button to save
    time.sleep(1)
    save_button.click()  # click button to un-save since I really don't want it on my list
    time.sleep(5)
