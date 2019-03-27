from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe' #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)

web.get("https://www.google.com.tw/")
print(web.title)

# inputElement = web.find_element_by_name("q")
# inputElement.send_keys("cheese!")
# inputElement.submit()#

# try:
#     # 直到標題有 cheese
#     WebDriverWait(web, 10).until(EC.title_contains("cheese!"))
 
#     # 顯示標題，可看到 cheese
#     print(web.title)
# except TimeoutException:
#     print('time out')
# finally:
#     web.quit()

"""
web.get('http://www.cwb.gov.tw/V7/')
web.set_window_position(0,0) #瀏覽器位置
web.set_window_size(700,700) #瀏覽器大小
time.sleep(5)

web.find_element_by_link_text('天氣預報').click() #點擊頁面上"天氣預報"的連結
time.sleep(5)

web.close()
"""