#네이버 카페
from socket import socket
from bs4.element import Comment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

keyword = input("검색어:" )
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://cafe.naver.com/joonggonara")
driver.find_element_by_id("topLayerQueryInput").send_keys(keyword)
driver.find_element_by_id("topLayerQueryInput").send_keys(Keys.RETURN)
driver.switch_to.frame('cafe_main')

try:
    page_url = driver.find_element_by_css_selector('div.prev-next').find_element_by_css_selector('a').get_attribute('href')
    page_url = page_url[:-1]
    count = 1
    url_list = []
    is_finished = False
    for i in range(1,3):
        time.sleep(1)
        driver.get(page_url + str(i))
        driver.switch_to.frame('cafe_main')
        article_board = driver.find_elements_by_css_selector('div.article-board.m-tcol-c')[-1]
        table_tbody = article_board.find_element_by_css_selector('table > tbody')
        article_list = table_tbody.find_elements_by_css_selector('tr')
        for article in article_list:
            if '등록된 게시글이 없습니다' in article.text:
                is_finished = True
            try:
                url = article.find_element_by_css_selector('div.inner_list > a.article').get_attribute('href')
                url_list.append(url)
            except:
                pass 
        if is_finished == True:
            break     
# 게시글 들어가는 부분 
    for url in url_list:
        time.sleep(1)
        driver.get(url)

except Exception as e:
    pass
  
## 네이버 영화댓글 크롤링

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def NaverMovieGeturlFromKeyword(driver):
    keyword = input("영화 제목을 입력해주세요:" )
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://movie.naver.com/")
    driver.find_element_by_id("ipt_tx_srch").send_keys(keyword)
    driver.find_element_by_id("ipt_tx_srch").send_keys(Keys.RETURN)
    s_list = driver.find_element_by_class_name('search_list_1')
    s_item = s_list.find_elements_by_css_selector('li')
    count = 1
    for item in s_item:
        title = item.find_element_by_css_selector('dl > dt').text
        print(str(count)+ "." + title)
        count += 1
        etc_list = item.find_element_by_css_selector('dd.etc')
        for etc in etc_list:
            print(etc.text)
        print("\n")

    
    s_num = input('영화 선택(취소:c): ')
    if(s_num == 'c'):
        print("영화선택 취소")    
        return -1
    s_num = int(s_num)
    if(s_num > count):
        print('잘못된 번호 선택')
        return - 1

    s_movie = s_item[s_num -1]
    s_movie_title = s_movie.find_element_by_css_selector('dl>dt').text
    s_move_url = s_movie.find_element_by_css_selector('dl > dt > a').get_attribute('href')
     
    return s_movie_title, s_move_url

def navermoviegrade(driver, url):
    driver.get(url)
    driver.switch_to.frame('pointAfterListlframe')
    input_netizen = driver.find_element_by_class_name('input_netizen')
    paging = input_netizen.driver.find_element_by_class_name('paging') 
    page_list = paging.driver.find_element_by_css_selector('a')
    first_page = page_list[0].get_attribute('href')

    driver.get(first_page)
    now_page = first_page
    while True:
        time.sleep(1)
        input_netizen = driver.find_element_by_class_name('input_netizen')

        score_table = input_netizen.find_element_by_class_name('score_result')
        score_list = score_table.find_element_by_css_selector('score_result')
        for item in score_list:
            star_score = item.find_element_by_class_name('star_score')
            score = star_score.find_element_by_css_selector('em').text
            score_reple = item.find_element_by_class_name('score_reple')
            reple = score_reple.find_element_by_css_selector('p').text
            date_text = score_reple.find_element_by_css_selector('dl > dl  >em:nth-child(2)').text
            data = {'score':score, 'comment':reple, 'date': date_text}
            score_data_list.append(data)
        paging = input_netizen.driver.find_element_by_class_name('paging') 
        page_list = paging.driver.find_element_by_css_selector('a')
        last_page = page_list[-1].get_attribute('href')
        if(now_page == last_page):
            break
        now_page = last_page
        driver.get(now_page)

driver = webdriver.Chrome('chromedriver.exe')
#title. url = NaverMovieGeturlFromKeyword(driver)
#code = url.split('code=')[-1]
code= '205629'
point_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=' + code
mg = navermoviegrade(driver, point_url)

# Instagram

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


keyword = input('검색어를 입력해주세요: ')
num_of_scroll = int(input('스크롤 횟수를 정해주세요 : '))
url = 'https://www.instagram.com/explore/tags/' + keyword
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

time.sleep(15)
driver.get(url)
time.sleep(5)

url_list = []

for i in range(num_of_scroll):
    time.sleep(0.5)
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
    
post_list = driver.find_element_by_class_name('EZdmt')
for post in post_list:
    href = post.find_element_by_css_selector('a').get_attribute('href')
    url_list.append(href)

print(post_list)

