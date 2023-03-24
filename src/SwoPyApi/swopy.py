from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import sys


def getHomeworkHTML(options):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    driver.get(options['url'])
    driver.find_element(by=By.NAME, value="loginname").send_keys(options['username'])
    driver.find_element(by=By.NAME, value="password").send_keys(options['password'])
    driver.find_element(by=By.XPATH, value=options['loginbtn_xpath']).click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value=options['bookbtn_xpath']).click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value=options['pagebtn_xpath']).click()


    time.sleep(3)
    html = driver.find_element(by=By.XPATH, value=options['homeworkdiv_xpath']).get_attribute("innerHTML")
        
    driver.quit()
    return html
