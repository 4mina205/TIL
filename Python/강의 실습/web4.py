#
# # # fp=open("lang.html",mode="r", encoding="utf-8").read()
# # # soup=BeautifulSoup(fp, "html.parser")
# # # print(soup)
# # # print("="*50)
# # # print(soup.select_one("ul>li"))
# # # print(soup.select_one("ul>li#py"))
# # # print(soup.select_one("#py"))
# # # print(soup.select_one("ul#language > li#py"))
# # # print(soup.select_one("#language #py"))
# # # print(soup.select_one("li[id='py']"))
# # # print(soup.select_one("li:nth-of-type(1)"))
# # # print(soup.select_one("li:nth-of-type(2)"))
# # # print(soup.select_one("li:nth-of-type(3)"))
# # # # print("="*50)
# # # # print(soup.select("ul>li"))
# # #
# # #
# # # #################################################################################
# # # ######### 네이버 환율 정보 ####################################################33
# # # import urllib.request as req           #url가져올 때 임폴트 해줘야 함
# # # url="https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
# # # res=req.urlopen(url).read().decode('euc-kr')
# # # soup=BeautifulSoup(res, "html.parser")
# # # print(soup)
# # # print("달러당",soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value").string,"원")
# # # print("달러당",soup.select_one("#oilGoldList > li.on > a.head.wti > div > span.value").string,"원")
# # # print("기사",soup.select_one("#content > div.section_news > div > ul > li:nth-child(1) > p > a").string)
# # # #oilGoldList > li.on > a.head.wti > div > span.value
# # # #content > div.section_news > div > ul > li:nth-child(1) > p > a
# # #
# # #
# #
# # #################################################################################
# # ##################################### 위키 피디아##################################
# # import urllib.request as req           #url가져올 때 임폴트 해줘야 함
# # url="https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"  #url주소 복붙
#
# # res=req.urlopen(url)                  # url 읽어주기
# # soup=BeautifulSoup(res, "html.parser")    # 수프
# # # print(soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li"))
# #                       mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a
#                        #mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li:nth-child(1) > a
# #
# # mylist=soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li")
# # for li in mylist:
# #     print(li.string)
# #
# # #mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li
#
#
# ##################################################
# ####################   css   ##############################
# fp=open("fruits-vegetables.html", encoding="utf-8")
# soup=BeautifulSoup(fp, "html.parser")
#
#
#
#
# # dic={"data-lo":"us"}#속성명:속성값
# # print(soup.findAll("li", dic)) # find 함수 == select_one함수, findALL==select함수
# # dic={"data-lo":"us","class":"black"}
# # print(soup.findAll("li", dic))
# # print(soup)
# # print(soup.select("div > h1"))  #[<h1>과일과 야채</h1>]
# # print(soup.select("div > ul#fr-list"))
# # print(soup.select("li"))
# # print(soup.select("li.black"))
# # print(soup.select("li.black")[1])
# # print(soup.select("li.black")[1].string)                  #클래스를 나타낼 때는 (.) 사용!!!!@#!#!@!@@#
# # print(soup.select("#ve-list"))
# # print(soup.select("#ve-list > li"))
# # print(soup.select("#ve-list > li:nth-of-type(4)")[0].string)
# # print(soup.select("#ve-list > li[data-lo='us']")[1])  #<li class="black" data-lo="us">아보카도</li>
# # print(soup.find(id="ve-list").find("li",dic))
# ###############################################################################################
# ###############################################################################################
# ########################################################################################################
# #######################################웹브라우저 조종할 때 제일 중요함#####################################
# from bs4 import BeautifulSoup
# from selenium import webdriver                              #셀레니움에 있는 웹드라이버 모듈 임포트

# driver=webdriver.Chrome("c:/scrap/chromedriver.exe")        #크롭드라이버 다운받은거 왜하는지는 모름
# url="https://www.melon.com/chart/index.htm"
# driver.get(url)
# html=driver.page_source
# soup=BeautifulSoup(url, "html.parser")
# songs=soup.select("tr")[1:]
# song=songs[0]
# title=song.select("a")
# print("곡명 :", song.select("div.ellipsis.rank01 > span")[0].str)
# for song in songs:
#     print("곡명 :", song.select("div.ellipsis.rank01")[0].string)
#     print("가수명 :", song.select("div.ellipsis.rank02 > span")[0].string)
#     print("="*50)

# 네이버 -> 강아지 -> 이미지 탭 주소
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B0%95%EC%95%84%EC%A7%80
#고양이
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4





#################################################################################
########################    리뉴얼 보류    #######################################
#################################################################################
# from bs4 import BeautifulSoup
# from selenium import webdriver
# baseUrl="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# word=input("검색어를 입력하세요 :")
# from urllib.request import urlopen
# from urllib.parse import quote_plus
# num=int(input("개수 입력 :"))
# url=baseUrl+quote_plus(word)
# html=urlopen(url)
# soup=BeautifulSoup(html, "html.parser")
# img=soup.find_all(class_="_img")
# print(len(img))






















































































