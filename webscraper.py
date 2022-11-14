from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import getpass
import time
import html_to_json
import json
import os
import sys


password = getpass.getpass("Input your password for swop please\n")
userame = sys.argv[1]
url = sys.argv[2]

try:
    auth = open("./auth.json", "r")
    options = json.loads(auth)
    auth.close()
except:
    print("auth.json not found")



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(options['url'])


driver.find_element(by=By.XPATH, value="/html/body/div/div/div[1]/div/form/input[1]").send_keys(options['username'])
driver.find_element(by=By.XPATH, value="/html/body/div/div/div[1]/div/form/input[2]").send_keys(options['password'])
driver.find_element(by=By.XPATH, value="/html/body/div/div/div[1]/div/form/button").click()

time.sleep(3)

try:
    html = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[1]/div/div/div/div[2]/div[3]/div[3]").get_attribute("innerHTML")
    print(html)
except:
    print("Could not find homework element")
    driver.quit()
    
driver.quit()
print("\n\n SUCCESSFULLY RETRIEVED DATA \n\n")

output = html_to_json.convert(html)

try:
    os.remove("./homework.json")
except:
    pass

json_file = open("./homework.json", "w")

json_file.write(json.dumps(output, indent=4, sort_keys=True))

json_file.close()


j = 1
os.system('cls')
print("\n")
print("================================")

for i in output['div'][0]['div']:
    assignment = i['div'][0]['div'][0]['b'][0]["_value"]
    teacher = i['div'][0]['i'][0]['_value'].replace('von ', '')
    subject = i['div'][0]['span'][0]['strong'][0]['_value']
    date = i['div'][0]['span'][1]['_value']
    deadline = i['div'][0]['span'][2]['_value']  
    print("Assignment number ", j)
    print("{}, \n by {} from your {} class, \n from {} till {}".format(assignment, teacher, subject, date, deadline))
    print("================================")
    j += 1