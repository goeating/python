from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from lxml import etree
import xlwt
import urllib.request
import urllib 
import re
import requests
from bs4 import BeautifulSoup
#引入ActionChains 類*
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re

chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe' #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

url = "https://www.ptt.cc/bbs/TW_Entertain/index.html"
web.get(url)

def finditem(urll):
    req = requests.get(url = urll)
    html = req.text
    bf = BeautifulSoup(html,'lxml')
    texts = bf.find_all('div',class_ = 'title')
    title_list = []
    for a in texts:
        title = a.find('a')
        if title != None:
            title = title.text
            title_list.append(title)
    return title_list


lists = []
count = 0
for i in range(5):
    names = finditem(web.current_url)
    lists.extend(names)
    web.find_element_by_xpath("//*[@id='action-bar-container']/div/div[2]/a[2]").click()
    sleep(2)

keywords = []
for items in lists:
    string= items
    regex = re.compile(r'\[(.*?)\]')
    match = regex.search(string)
    a = match.group(1)
    keywords.append(a)
    print(items)

keywordscount = dict((a, keywords.count(a)) for a in keywords)
print(keywordscount)

web.quit()


#string= lists


