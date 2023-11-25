import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml
import requests
from bs4 import BeautifulSoup

brower = webdriver.Chrome()



def lol_find(nickname):

    

    url = f"https://www.op.gg/summoners/kr/{nickname}"
    time.sleep(3) 
    brower.get(url)
    time.sleep(1) 

    soup = BeautifulSoup(brower.page_source, "lxml")

    top5 = soup.find("strong", attrs = {"class" : "css-ao94tw e1swkqyq1"})
    title = soup.find("div", attrs = {"class" : "tier"})
    author = soup.find("div", attrs = {"class" : "k-d-a"})

    print("----------실시간 인기 웹툰-----------")
    print(f"{top5.text} - {title.text} || {author.text}")

nickname = input("닉네임 입력")
lol_find(nickname)