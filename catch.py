# -*- coding: utf-8 -*-

import re
import requests
import urllib

def getHtml(url):
    page = requests.get(url)
    return page.text

def getImg(html):
    reg = r'src=\"(http.*?\.[jpgne]+)\"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist


def Dl(title):
    for num in range(0,len(title)):
        reg = r'\.([jpgne]+)'
        imgre = re.compile(reg)
        filename = re.findall(imgre,title[num])
        if filename[0] == 'jpg' : urllib.urlretrieve(title[num],'%s.jpg' % num)
        elif filename[0] == 'png' : urllib.urlretrieve(title[num],'%s.png' % num)
        elif filename[0] == 'jpeg' : urllib.urlretrieve(title[num],'%s.jpeg' % num)
        else : urllib.urlretrieve(title[num],'%s.jpg' % num)

urls = raw_input("input url:")

try:
    html = getHtml(urls)
except IOError as err:
    print("I/O error: {0}".format(err))
except ValueError:
    print ("Error: url輸入錯誤")
else:
    title = getImg(html)
    Dl(title)
    print "Successful!"