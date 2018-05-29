import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
input=browser.find_elements_by_css_selector('.service-bd li')
for ii in input:
    print(ii.text)
# input.send_keys('iphone')
# input.send_keys(Keys.ENTER)









