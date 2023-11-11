import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests
from bs4 import BeautifulSoup

brower = webdriver.Chrome()
url = "https://comic.naver.com/webtoon?tab=sat"

brower.get(url)
time.sleep(1) 

soup = BeautifulSoup(brower.page_source, "lxml")

top5 = soup.find("ul", attrs = {"class" : "AsideList__content_list--FXDvm"})
title = top5.findAll("span", attrs = {"class" : "ContentTitle__title--e3qXt"})
author = top5.findAll("a", attrs = {"class" : "ContentAuthor__author--CTAAP"})

print("----------실시간 인기 웹툰-----------")

for i in range(len(title)):
    print(f"{i+1} - {title[i].text} || {author[i].text}")