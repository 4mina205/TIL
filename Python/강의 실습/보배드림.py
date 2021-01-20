from bs4 import BeautifulSoup
from selenium import webdriver
driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
url="https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"
driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html, "html.parser")

a=["a","vvv","ccc"]


for i in range(20):
    print("차량명 :",soup.select("div.mode-cell.title > p > a")[i].string)
    print("연식 :",soup.select("div.mode-cell.year > span")[i].string)
    print("연료 :",soup.select("div.mode-cell.fuel > span")[i].string)
    print("가격 :",soup.select("div.mode-cell.price > b > em")[i].string)
    print("="*50)
