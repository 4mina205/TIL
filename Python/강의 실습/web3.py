import re
# if re.match("\d{4}$","12345"):
#     print("정")
# else:
#     print("비정상")


# re.sub("패턴","바꿀문자열","문지열",바꿀횟수)

# print(re.sub("apple|orrange","fruit","apple tree banana orange"))

# "1 2 apple 3 banana 4 7 9 40 tree"
# print(re.sub("[0-9]+",'num',"1 2 apple 3 banana 4 7 9 40 tree"))

# pat=re.compile("apple|orange")
# print(pat.sub("fruit","apple tree banana orange"))

import urllib.request
# url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# urllib.request.urlretrieve(url,"test.png")
# print("저장됐습니다.")

# url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# mem=urllib.request.urlopen(url).read()
# with open("test2.png","wb") as f:
#     f.write(mem)
#     print("저장")

# http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp

# import urllib.parse as parse
# import urllib.request as requst
# addr="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# values={'stdId':'109'}
#
# params=parse.urlencode(values)
# url=addr+"?"+params
# print(url)
# print("@"*50)
# data=requst.urlopen(url).read()
# data=data.decode('utf-8')
# print(data)

from bs4 import BeautifulSoup

# # html='''
# # <html><body>
# # <h1>스크래핑</h1>
# # <p>웹 페이지 분석</p>
# # <p>원하는 부분 추출</p>
# # </body></html>
# # '''
# #
# # #붕어빵 봉투 = 붕어빵 기계(밀가루,10cm)
# # # print(soup.html.body.h1)
# # # print(soup.html.body.p)
# # # print(soup.html.body.p.string)
# # # print(soup.html.body.p.string)  #동일한 수준에 같은 명칭이 여러개 있을 때
# #
# #
# # soup=BeautifulSoup(html, "html.parser")
# # p1=soup.html.body.p # 엔터(줄바꿈)가 나옴
# # p2=p1.next_sibling.next_sibling.string
# # print(p2)
# # # soup.html.body.p.string
# # #soup.<맨 바깥>.<그 안> <그.안>
#
#
# html2='''
# <html>
# <body>
# <h1 id="title">스크래핑</h1>
# <p id="body">웹 페이지 분석</p>
# <p>원하는 부분 추출</p>
# </body>
# </html>
# '''
#
# soup=BeautifulSoup(html2, "html.parser")
# print(soup.html.body.h1.string)
# print(soup.find(id='title').string)
# print(soup.find(id='body').string)
# #######################################################################################################################
# #######################################################################################################################
html3='''
<html>
<body>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.com">daum</a></li>
</ul>
</body>
</html>
'''
# # <태그명 속성명=속성값 속성명=속성값...>
# # a태그 값 찾기
# soup=BeautifulSoup(html3, "html.parser")
# # print(soup) #<class 'bs4.BeautifulSoup'> #html파서로 분석할 수 있는 객체로 변환
# # print(html3) #<class 'str'>
# links=soup.find_all("a") # 리스트의 요소로 저장이 됨
# # print(html3.find_all("a")) # 에러나옴
# # print(links[])
# for i in links:
#     href=i.attrs['href']          # attribute속성
#     na=i.string
#     print(na,"-->", href)        # a 태그를 찾아내고 그 안에있는 속성같을 찾아냄

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
html4='''
<p><a href="aaa.html name=asdqw">aaa page</a></p>
'''
soup=BeautifulSoup(html4,"html.parser")
# print(soup.p.a.string)
# print(soup.a.string)  #p태그를 안써도 출렫  -->  a태그가 여러곳에 산지해 있는경우에는 p태그를 써줘야함
# aaa page
# aaa page
# print(soup.a.attrs) # dict형태로 나옴!@#!@##
mydict=soup.a.attrs
# print('href' in mydict)

dic=soup.a.attrs
print(list(dic.values()))
# links=soup.find_all("a")
# for i in links:
#     href=i.attrs['href']          # attribute속성
#     a=i.string
#     print(a,"-->", href, )






import urllib.request as req

url='http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
res=req.urlopen(url)
# print(res)
# soup=BeautifulSoup(res, "html.parser")
# print("문서 제목 :",soup.title.string)
# print(soup.find("title"))
# print(soup.find_all("title"))
# print(soup.find_all("title")[0])
#
# # 모든 wf태그의 내용을 출력
# print(soup.find("wf").string)
# print(soup.find_all("wf"))


from bs4 import BeautifulSoup

html5 = """
<html><body>
<div id="lang">
    <h1>프로그래밍언어</h1>     #제목
    <ul class="items">       # unordered list 
        <li>python</li>
        <li>java</li>
        <li>cpp</li>
    </ul>
</div>
</body></html>
"""

soup=BeautifulSoup(html5,"html.parser")
# print(soup.select("div"))
# print(soup.select("div#lang > h1")[0].string) #select함수에서는 > 가 ~안에 있다는 뜻임
#
#
# print(soup.select_one("div#lang > h1"))

# soup.select("div#lang > ul.items > li") # 태그에 클래스 명을 지정할 때
mylist=soup.select("div#lang > ul.items > li")
for i in mylist:
    print(i.string)





























