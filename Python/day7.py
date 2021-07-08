
## 오늘부터 해보자
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib
import os
path ='chromedriver.exe' 
driver = webdriver.Chrome(path)

driver.get('https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=3c1a0943-222c-4c05-8c96-aff576753602&con_type=10500')

wati = WebDriverWait(driver, 10)
img_list = driver.find_element_by_tag_name('img')






lmg_list[0].get_attribute('src')