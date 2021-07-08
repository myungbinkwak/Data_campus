from socket import AF_PPPOX, AddressFamily
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import urllib
import os


from urllib3 import request

query_txt = input('크롤링할 키워드는 무엇입니까?')
path = 'chromedriver.exe' 
driver = webdriver.Chrome(path)
driver.maximize_window() 
driver.get('https://www.google.co.kr/imghp?hl=ko')
time.sleep(3)
element = driver.find_element_by_name("q")
element.send_keys(query_txt)
element.send_keys(Keys.RETURN)
delay=10
url_list=[]

try:

opener = urllib.request.build_opner()
opener.addheaders = [('User-Agent', 
'Mozilla/5.0(Windows NT 6.1: WOW64')
AppleWebKit/537.36(KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opner(opener)
urllib.request.urlretrieve(url, save_img_path)



from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import urllib
import os
def GetApaulBassettAddressList(dirver):
    driver.get('https://www.baristapaulbassett.co.kr/store/Store.pb')
    shop_list = driver.find_elements_by_css_selector('#shopList > li')

    address_list = []
    for shop in shop_list:
        address = shop.find_element_by_tag_name('address')
        address_list.append(address.text)

    return address_list
def 10000coffee(driver):
    address_list = []
    for i in range(1, 16):
        driver.get('https://www.10000lab.com/59/?sort=TIME&ketword_type=all&page=' +str(i))
        map_list = driver.EC._find_elements_by_css_selector('div.map-list-detail>')
     driver.get('https://www.10000lab.com/59/?sort=STREET&keyword_type=all&page=')+str((i))
     shop_list = driver.find_elements_by_class_name('map-list')
         
address = '서울특별시 강남구 역삼2동 선릉로69길 19'
url = "https://dapi.kakao.com/v2/local/search/address.json?query="+ address
rest_api_key='e6ca9e5c72e0aac012040fc4d8b512bc'
header = {'Authorization': 'KakaoAk' + rest_api_key}
r = request.get(url, headers=header)
print(r)