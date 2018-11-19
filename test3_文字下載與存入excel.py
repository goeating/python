import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import xlwt

if __name__ == '__main__':
    target = 'https://join.gov.tw/idea/index/search/ENDORSING?page=2'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html,'lxml')
    texts = bf.find_all('div',class_ = 'list_item')
    
    array=[]
    a = 0
    for p in texts:
        array.append([])
        array[a].append(p.find('h4').text)
        #array[a].append(p.find(class_ ='show_4').text) 
        array[a].append(p.find(class_ ='date').text) 
        array[a].append(p.find(class_ ='show_3_1').text) 
        a=a+1

def save_to_excel():
    try:
        workbook = xlwt.Workbook()
        wooksheet = workbook.add_sheet('test',cell_overwrite_ok=True)
        head = ['名稱', '日期', '留言數']
        for h in range(len(head)):
            wooksheet.write(0, h, head[h])

        for row in range(len(array)):
            for column in range(len(array[0])):
                wooksheet.write(row,column,array[row][column])
        workbook.save('test.xls')
        print('寫入excel成功')
    except Exception:
        print('寫入excel失敗')

save_to_excel()