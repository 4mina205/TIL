# # 1.
# with open("text.txt","w") as f:
#     f.write("big data")
# with open("text.txt", "r") as f:
#     print(f.read())
#
# 2.
import re
# a="""
# park 010-9999-9988
# kim 010-9909-7789
# lee 010-8789-7768
# """
# b=re.sub("....\n","####\n",a)
# print(b)
#
# # 3.
# <meta charset="UTF-8">
#
# # 4.
# from selenium import webdriver
# from bs4 import BeautifulSoup
# driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
# driver.get("https://news.v.daum.net/v/20210126101652413")
# html=driver.page_source
# soup=BeautifulSoup(html, "html.parser")
# news=soup.find("section").text
# print(news)

