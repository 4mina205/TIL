from bs4 import BeautifulSoup
# fp=open("lang.html",mode="r", encoding="utf-8").read()
# soup=BeautifulSoup(fp, "html.parser")
# print(soup)
# print("="*50)
# print(soup.select_one("ul>li"))
# print(soup.select_one("ul>li#py"))
# print(soup.select_one("#py"))
# print(soup.select_one("ul#language > li#py"))
# print(soup.select_one("#language #py"))
# print(soup.select_one("li[id='py']"))
# print(soup.select_one("li:nth-of-type(1)"))
# print(soup.select_one("li:nth-of-type(2)"))
# print(soup.select_one("li:nth-of-type(3)"))
# # print("="*50)
# # print(soup.select("ul>li"))


#################################################################################
######### 네이버 환율 정보 ####################################################33
import urllib.request as req           #url가져올 때 임폴트 해줘야 함
url="https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res=req.urlopen(url)
soup=BeautifulSoup(res, "html.parser")
# print(soup)

















































































































































































