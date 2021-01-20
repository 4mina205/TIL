from bs4 import BeautifulSoup
from selenium import webdriver                              #셀레니움에 있는 웹드라이버 모듈 임포트
driver=webdriver.Chrome("c:/scrap/chromedriver.exe")        #크롭드라이버 다운받은거 왜하는지는 모름
url="http://search.danawa.com/dsearch.php?nSiteCode=0&k1=%EB%85%B8%ED%8A%B8%EB%B6%81"                   # url 읽어주기 깨짐 방지
     # url 읽어주기 깨짐 방지
driver.get(url)                                             #url열어
html=driver.page_source                                     #url연곳에서 소스코드를 html에 저장
soup=BeautifulSoup(html, "html.parser")    # 수프
print(soup)



