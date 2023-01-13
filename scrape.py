# Code to scrape Notre Dame classes from ND Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")
DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
wait = WebDriverWait(driver, 10)
#driver = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)
driver.get("https://classsearch.nd.edu/")
select = Select(driver.find_element("id", 'crit-srcdb'))
select.select_by_value('202220')
driver.find_element('id', 'search-button').click()
#driver.find_elements(By.CLASS_NAME, "result result--group-start")
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'result__code')))
listClasses = [my_elem.text for my_elem in driver.find_elements(By.CLASS_NAME, "result__code")]
json_object = json.dumps(listClasses)
with open("NotreDameClasses.json", "w") as outfile:
    outfile.write(json_object)
driver.get_screenshot_as_file('./Screenshots/classes.png')
#driver.quit()