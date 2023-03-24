from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import sys


def getHomeworkHTML(options):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(options['url'])
    driver.find_element(by=By.NAME, value="loginname").send_keys(options['username'])
    driver.find_element(by=By.NAME, value="password").send_keys(options['password'])
    driver.find_element(by=By.XPATH, value=options['loginbtn_xpath']).click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value=options['bookbtn_xpath']).click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value=options['pagebtn_xpath']).click()


    try:
        time.sleep(3)
        html = driver.find_element(by=By.XPATH, value=options['homeworkdiv_xpath']).get_attribute("innerHTML")
    except:
        sys.stderr.write("ERR::COULD NOT FIND HOMEWORK DIV -> PLEASE UPDATE AUTH.JSON")
        driver.quit()

        with open("../../crshrprt.txt", "w") as crshrprt:
            crshrprt.write(f"{datetime.now()}::ERR::COULD NOT FIND HOMEWORK DIV -> PLEASE UPDATE AUTH.JSON")

        sys.exit("Programm failed to retrive data")
        
    driver.quit()
    return html
