import re
import pymongo
from selenium import webdriver
from urllib.parse import urlencode
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
browser = webdriver.Chrome()
shangpin='美食'
wait= WebDriverWait(browser, 10)
client=pymongo.MongoClient(host='localhost',port=27017)
db=client.taobao
Collection=db.taobao
def one_ye():

    browser.get('https://www.taobao.com/')
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
    button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
    input.send_keys('美食')
    button.click()
    total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.total")))
    get_Message()
    return total.text
def main():
    total=int(re.search('(\d+)',one_ye()).group(1))
    for item in range(1,total+1):
        page_skip(item)

def page_skip(total):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
        button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(total)
        button.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(total)))
        get_Message()
    except TimeoutError:
        page_skip(total)
def get_Message():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html=browser.page_source
    doc=pq(html)
    for item in doc('#mainsrp-itemlist .items .item').items():
        Message={
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.row .price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text().strip(),
            'shop':item.find('.shop').text(),
            'shop_area':item.find('.row.row-3 .location').text()

        }
        save_mongodb(Message)
def save_mongodb(Message):
    Collection.insert(Message)
if __name__=='__main__':
    main()