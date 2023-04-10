# 00. 라이브러리
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import urllib
import time
import random
import sys
import re
import os
import pyautogui
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

# 01. 이미지 저장 폴더 설정
f_dir = 'C:/Users/KimBumYun/Desktop/crawling/'
#f_dir = input('이미지를 저장할 폴더(예:C:\\Users\\) : ')

# 02. 시간 설정
now = time.localtime()
f_name = '%04d-%02d-%02d-%02d-%02d-%02d' %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
dir_name = '사진저장'

# 03. 이미지 저장 폴더 설정
os.makedirs(f_dir+f_name+'-'+dir_name)
os.chdir(f_dir+f_name+'-'+dir_name)
f_result_dir=f_dir+f_name+'-'+dir_name

s_time = time.time()

# 04. 웹 열기
dr = webdriver.Chrome("/chromedriver.exe")
dr.set_window_size(1440, 1440)
dr.get('http://www.7-eleven.co.kr/product/presentList.asp')
time.sleep(1)

# 05. 1+1 페이지
oneone_page = dr.find_element(By.XPATH, '//*[@id="actFrm"]/div[3]/div[1]/ul/li[1]/a')
#twoone_page = dr.find_element(By.XPATH, '//*[@id="actFrm"]/div[3]/div[1]/ul/li[2]/a')
oneone_page.send_keys('\n')

scroll_count = 0
# 06. 스크롤
while True:
    try:
        if scroll_count == 0:
            page_down = dr.find_element(By.XPATH, '//*[@id="listUl"]/li[15]/a')
        else:
            page_down = dr.find_element(By.XPATH, '//*[@id="moreImg"]/a')
        page_down.send_keys('\n')
        time.sleep(0.5)
        scroll_count = scroll_count + 1
    except:
        break

dr.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)

# 06. 이미지 다운로드
images = dr.find_elements(By.CSS_SELECTOR, 'img')

li_count = 1
image_count = 2

for image in images:
    try:
        if image_count <= 14:
            imgUrl= dr.find_element(By.XPATH, '//*[@id="listUl"]/li[' + str(image_count) + ']/div/img').get_attribute("src")
            urllib.request.urlretrieve(imgUrl, str(image_count) + ".jpg")
            product_name = dr.find_element(By.XPATH, '//*[@id="listUl"]/li[' + str(image_count) + ']/div/div/div[1]').text
            print(product_name)
            product_price = dr.find_element(By.XPATH, '//*[@id="listUl"]/li[' + str(image_count) + ']/div/div/div[2]/span').text
            print(product_price)
        else:
            imgUrl= dr.find_element(By.XPATH, '//*[@id="listUl"]/li[' + str(image_count) + ']/div/div/img').get_attribute("src")
            urllib.request.urlretrieve(imgUrl, str(image_count) + ".jpg")
            product_name = dr.find_element(By.XPATH, '//*[@id="listUl"]/li[' + str(image_count) + ']/div/div/div/div[1]').text
            print(product_name)
            product_price = dr.find_element(By.XPATH, '//*[@id="listUl"]/li[' + str(image_count) + ']/div/div/div/div[2]/span').text
            print(product_price)
        image_count = image_count + 1
        li_count = li_count + 1
    except:
        pass

e_time = time.time()#끝난시간 체크

t_time = e_time - s_time #크롤링에 쓰인 시간

print('='*100)
print('총 소요시간은 %s 초입니다.'%round(t_time, 1))
print('총 저장 건수는 %s 건입니다.'%(image_count-1))
print('파일 저장 경로: %s 입니다.'%f_result_dir)
print('='*100)