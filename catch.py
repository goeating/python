# -*- coding: utf-8 -*-

import re
import requests
import urllib

def getHtml(url):
    page = requests.get(url)
    return page.text

def getImg(html):
    reg = r'src="(http.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

num = 1
def Dl(title):
    for num in range(1,len(title)):
        urllib.urlretrieve(title[num],'%s.jpg' % num)
        num += 1

urls = raw_input("put url:")

try:
    html = getHtml(urls)
except IOError:
    print "Error: 没有找到url或读取url失败"
else:
    title = getImg(html)
    Dl(title)
    print "Successful!"