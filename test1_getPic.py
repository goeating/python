# -*- coding: utf-8 -*-

import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.reaSd()
    return html

def getImg(html):
    reg = r'src="(http.*?\.jpg)"'
    imgre = re.compile(reg)
    html=html.decode('utf-8')#python3
    imglist = re.findall(imgre,html)
    return imglist

num = 1
def Dl(title):
    for num in range(1,len(title)):
        urllib.request.urlretrieve(title[num],'%s.jpg' % num)
        num += 1

html = getHtml("https://tieba.baidu.com/p/2957576690?fr=good")
title = getImg(html)
Dl(title)