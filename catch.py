# -*- coding: utf-8 -*-

import re
import requests
import urllib
from time import sleep
import Tkinter as tk
from Tkinter import *

def getHtml(url):
    page = requests.get(url)
    return page.text

def getImg(html,a):
    reg = r'src=\"(http.*?\.[jpgneif]+)\"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    imglists = ImgFormatList(imglist,a)
    return imglists


def Dl(title):
    for num in range(0,len(title)):
        reg = r'\.([jpgenif]+$)'
        imgre = re.compile(reg)
        filename = re.findall(imgre,title[num])
        if filename[0] == 'jpg' : urllib.urlretrieve(title[num],'%s.jpg' % num)
        elif filename[0] == 'png' : urllib.urlretrieve(title[num],'%s.png' % num)
        elif filename[0] == 'jpeg' : urllib.urlretrieve(title[num],'%s.jpeg' % num)
 	elif filename[0] == 'gif' : urllib.urlretrieve(title[num],'%s.gif' % num)        
	else : urllib.urlretrieve(title[num],'%s.jpg' % num)
	sleep(2)

def ImgFormatList(lists,a):
    list_jpg = []
    list_png = []
    list_gif = []
    list_jpeg = []
    list_all  = []
    for num in range(0,len(lists)):
        reg = r'\.([jpgenif]+$)'
        imgre = re.compile(reg)
        filename = re.findall(imgre,lists[num])
        if filename[0] == 'jpg' : list_jpg.append(lists[num])
        elif filename[0] == 'png' : list_png.append(lists[num])
        elif filename[0] == 'jpeg' : list_jpeg.append(lists[num])
        elif filename[0] == 'gif' : list_gif.append(lists[num])

    if '0' in a: list_all.extend(list_jpg)
    if '1' in a: list_all.extend(list_png)
    if '2' in a: list_all.extend(list_gif)
    if '3' in a: list_all.extend(list_jpeg)
    return list_all


def insert_point():
    try:
        lists = []
        if var1.get() == 1 : lists.append("0")
        if var2.get() == 1 : lists.append("1")
        if var3.get() == 1 : lists.append("2")
        if var4.get() == 1 : lists.append("3")
        t.delete(0.0, END)
        html = getHtml(e.get())
        img = getImg(html,lists)
        downl = Dl(img)
        t.insert('insert',"Successful!")
    except IOError as err:
        t.insert('insert',"I/O error: {0}".format(err))
    except ValueError:
        t.insert('insert',"Error: url輸入錯誤")
    except UnicodeEncodeError as err:
        t.insert('insert',"UnicodeEncode error: {0}".format(err))
    except BaseException as err:
        t.insert('insert',"error: {0}".format(err))


window = tk.Tk() #建立主視窗 
window.title('catch window')
window.geometry('300x250')

e = tk.Entry(window)
e.pack(fill = X , pady = 5 , padx = 5 )

frm = tk.Frame(window)
frm.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
c1 = tk.Checkbutton(frm, text='jpg', variable=var1, onvalue=1, offvalue=0)
c2 = tk.Checkbutton(frm, text='png', variable=var2, onvalue=1, offvalue=0)
c3 = tk.Checkbutton(frm, text='gif', variable=var3, onvalue=1, offvalue=0)
c4 = tk.Checkbutton(frm, text='jpeg', variable=var4, onvalue=1, offvalue=0)
c1.pack(padx=10,side=LEFT)
c2.pack(padx=10,side=LEFT)
c3.pack(padx=10,side=LEFT)
c4.pack(padx=10,side=LEFT)


b1 = tk.Button(window,text="download pictures",width=15,height=2,command = insert_point)
b1.pack(pady = 5)

t = tk.Text(window , height=4)
t.pack(fill = X , pady = 5 , padx = 5 )

window.mainloop()

