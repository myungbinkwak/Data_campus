# 데이터 프레임
from bs4 import BeautifulStoneSoup, element
from numpy import select
import pandas as pd
from selenium.webdriver.common import keys, service

no = [] # 리스트생성
subject_name = []
no.append(1)
no.append(2)
no.append(3)

subject_name.append('수학')
subject_name.append('과학')
subject_name.append('빅데이터')
# 데이터프레임 만들기 (table 형식)
subject = pd.DataFrame()
subject['과목번호'] = no
subject['과목명'] = subject_name

print(subject)

subject.to_csv('subject.csv', encoding="UTF-8", index = False)

# 웹크롤링 ----------------------------------
#beautiful soup활용하기 
#pip install bs4
import bs4
from bs4 import BeautifulSoup
ex1 = '''
<!doctype>
<html lang = "ko">
<head>
	<meta charset = "utf-8">
	<title> HTML 연습 </title>
</head>
<body>
	<h1> 나의 좌우명 </h1>
	<p> 할 수 있다고 생각을 하든
	    할 수 없다고 생각을 하든
	    생각대로 됩니다 !		</p>
    <p>테스트1</p>
    <p>테스트2</p>
</body>
</html>
'''
soup = BeautifulSoup(ex1, 'html.parser')
soup.find('title')
# find는 하나만 가져올 수 있음
# find_all() 해당태그 모두 가져올수있음
a = soup.find_all('p') # 리스트 형식
for i in a:
    print(i.string)
    print("----")

txt = soup.find('p')
txt.string

txt2 = soup.find_all('p')
for i in txt2:
    print(i.string)

txt3 = soup.find_all('p')
for i in txt3 :
    print(i.get_text())

# 셀레니움 (크롤링하기)
# pip install selenium
import selenium

from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.dongguk.edu")
##-------------------------------------------------------------


from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
query_txt = input('크롤링할 키워드는 무엇입니까?') #입력어
# 셀레니움 불러오기
path ='chromedriver.exe' 
driver = webdriver.Chrome(path)
driver.maximize_window()
# 웹 접근
driver.get('https://korean.visitkorea.or.kr/main/main.html')
time.sleep(2) # 쉬어가는 시간
#driver.find_element_by_id('openSearchForminput').click()
element = driver.find_element_by_id('inp_search')
element.send_keys(query_txt)
element.send_keys(Keys.RETURN)
delay=10
data_list =[]

try:
    wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_last')))
    page_box = driver.find_element_by_id('page_box')
    last_page = page_box.find_element_by_class_name('btn_last').get_attribute("id")
    last_page = int(last_page)
    for num in range(2, 10):
        time.sleep(1)
        wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_last')))

        ul = driver.find_element_by_class_name('list_thumType')
        content_list = ul.find_elements_by_class_name('list_thumType')
        content_list = ul.find_elements_by_css_selector('li>div.area_txt')
        for i in content_list:
            try:
                tit = i.find_element_by_class_name('tit').text
                service = i.find_element_by_class_name('service').text
                tag = i.find_element_by_class_name('tag_type').text
                data = {'tile':tit, "service":service, "tag":tag}
                data_list.append(data)
            except Exception as e:  
                print(e)    

        page_box.find_element_by_id(num).click()

    df = pd.DataFrame(data_list)
    print('성공')
    df.to_csv('여행지.csv', encoding='euc-kr')# 엑셀로 저장
except TimeoutException:
    print("Timeout") 

##2번째꺼-------------------------------------------------------
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
query_txt = input('크롤링할 키워드는 무엇입니까?') #입력어
# 셀레니움 불러오기
path ='chromedriver.exe' 
driver = webdriver.Chrome(path)
driver.maximize_window()
# 웹 접근
driver.get('https://korean.visitkorea.or.kr/main/main.html')
time.sleep(2) # 쉬어가는 시간
#driver.find_element_by_id('openSearchForminput').click()
element = driver.find_element_by_id('inp_search')
element.send_keys(query_txt)
element.send_keys(Keys.RETURN)
delay=10
url_list =[]

try:
    wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_last')))
    page_box = driver.find_element_by_id('page_box')
    last_page = page_box.find_element_by_class_name('btn_last').get_attribute("id")
    last_page = int(last_page)
    for num in range(2, 10):
        time.sleep(1)
        wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_last')))

        ul = driver.find_element_by_class_name('list_thumType')
        content_list = ul.find_elements_by_class_name('list_thumType')
        content_list = ul.find_elements_by_css_selector('li>div.area_txt')
        for i in content_list:
            try:
                href = tit = i.find_element_by_class_name('tit').find_element_by_css_selector('a').get_attribute('href')
                url_list.append(href)

            except Exception as e:  
                print(e)    

    page_box.find_element_by_id(num).click()

    for url in url_list:
        url = url.split('\'')[1]
        base_url = "https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid="
        fonal_url = base_url +url

except TimeoutException:
    print("Timeout") 
## ----페이지 내의 자료 추출
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get('https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=5d063ecc-ff86-4b7e-8ad8-85ce5ae9008c&con_type=11000')
title=''
location=''
data= ''
heart=''
share=''
view=''
content=''
food=''
house=''
editor=''

title = driver.find_element_by_id('topTitle').text
topAddr = driver.find_element_by_id('topAddr').text
titinfo = driver.find_element_by_class_name('wrap_contView').text
print(title)
print(topAddr)

addr = topAddr.split('\n')[0]
date = topAddr.split('\n')[1].split(':')[1].strip()


# 검색된 결과에서 텍스트 추출 후 저장하기

# 방법1 (이건왜 안될까)
#time.sleep(1)
#full_html = driver.page_source
#soup = BeautifulStoneSoup(full_html, 'html.praser')
#content_list = soup.find('ul', class = 'list thumType')
#for i in content_list:
#    print(i.text.strip())
#    print("\n")

#방법2 (이건되네)
time.sleep(1)
ul = driver.find_element_by_class_name('list_thumType')
content_list = ul.find_elements_by_css_selector('li')
for i in content_list:
    print(i.text.strip())
    print("\n")

# 다양한 형식으로 저장하기
time.sleep(1)
ul = driver.find_element_by_class_name('list_thumType')
content_list = ul.find_elements_by_class_name('list_thumType')
content_list = ul.find_elements_by_css_selector('li>div.area_txt')
for i in content_list:
    try:
        tit = i.find_element_by_class_name('tit').text
        service = i.find_element_by_class_name('service').text
        tag = i.find_element_by_class_name('tag_type').text
        data = {'tile':tit, "service":service, "tag":tag}
        data_list.append(data)
    except Exception as e:
        print(e)    

    page_box.find_element_by_id(num).click()


df = pd.DataFrame(data_list)
print('성공')
df.to_csv('여행지.csv', encoding='euc-kr')# 엑셀로 저장

# 참고: 페이지의 특정 element에 접근하는 방식
# find_element_by_name(‘html_name’)
# find_element_by_id(‘html_id’)
# find_element_by_xpath(‘/html/body/some/xpath’)
# find_element_by_css_selector(‘#css > div.selector’)
# find_element_by_class_name(‘some_class_name’)
# find_element_by_tag_name(‘h1’)

#NAVER에서 봄여행 키워드 입력한 후 검색실행
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
query_txt = input('크롤링할 키워드는 무엇입니까?')
# 셀레니움 불러오기
path ='chromedriver.exe' 
driver = webdriver.Chrome(path)
driver.maximize_window() # 전체화면 만들기
# 웹 접근
driver.get(' https://naver.com') # 네이버
time.sleep(2) # 쉬어가는 시간
element = driver.find_element_by_id('query')
element.send_keys(query_txt) # quert_txt를 키값에 보내기
element.send_keys(Keys.RETURN) # enter
# driver.find_element_by_id('search_bin').click() 115line과 동일

##--------------------------------------------------------

title=''
location=''
data= ''
heart=''
share=''
view=''
content=''
food=''
house=''
editor=''

title = driver.find_element_by_id('topTitle').text
topAddr = driver.find_element_by_id('topAddr').text
print(title)
print(topAddr)

addr = topAddr.split('\n')[0]
date = topAddr.split('\n')[1].split(':')[1].strip()