from css_finder import PageWork
from selenium import webdriver
import json

f = open('descriptive_scrapper/config/config.json', 'r')
config = json.load(f)


# create a webdriver 
driver = webdriver.Chrome(config['driver_path'])
driver.get(config['target_url'])

## execute page 1
page_1 = PageWork(driver, config['page_1'])
page_1.execute()