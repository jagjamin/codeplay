import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests
from bs4 import BeautifulSoup

brower = webdriver.Chrome(ChromeDriverManager().install())
url = "https://comic.naver.com/webtoon?tab=sat"

brower.get(url)
time.sleep(1) 

soup = BeautifulSoup(brower.page_source, "lxml")

top3 = soup.find("ul", attrs = {"class" : "TripleRecommendList__triple_recommend_list--vm8_k"})
title = top3.findAll("span", attrs = {"class" : "ContentTitle__title--e3qXt"})
author = top3.findAll("a", attrs = {"class" : "ContentAuthor__author--CTAAP"})
rate = top3.findAll("span", attrs = {"class" : "Rating__star_area--dFzsb"})

print("----------토요 웹툰 추천 3개-----------")

for i in range(len(title)):
    print(f"{i+1} - {title[i].text} || {author[i].text} || {rate[i].text[2:]}")

