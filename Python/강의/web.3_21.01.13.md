# web.3_21.01.13

## 실습

* $ : 끝나야함

  ```
  import re
  if re.match("\d{4}$","12345"):   #4자리로 끝나야한다
      print("정")
  else:
      print("비정상")
  ```

* sub 함수

  대한민국, 한국, 코리아 --> 대한민국

  ```
  re.sub("패턴","바꿀문자열","문지열",바꿀횟수)
  ```

  ```
  print(re.sub("apple|orrange","fruit","apple tree banana orange"))
  fruit tree banana orange
  ```

  ```
  print(re.sub("[0-9]+",'num',"1 2 apple 3 banana 4 7 9 40 tree"))
  num num apple num banana num num num num tree
  ```

  

## 웹

* url

  ```
  import urllib.request
  url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
  urllib.request.urlretrieve(url,"test.png")
  print("저장됐습니다.")
  #이미지 저장
  
  url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
  mem=urllib.request.urlopen(url).read()
  with open("test2.png","wb") as f:          #이미지 파일은 바이너리 형식으로 저장해야함 wb
      f.write(mem)
      print("저장")
  #이미지 저장
  ```

  

## 웹언어

xml을 잘 알아야함 웹에 xml형식으로 저장 많이 돼있음

정제한 데이터를 분석하고 분석 결과물을 만들어 내야함



* 웹에서 사용하는 언어 

  -서버, 클라이언트 간에 데이터를 주고 받을 떄 사용하는 언어(HTML)

  클라이언트(페이지 요청, 웹 브라우저에 www.naver.com) ==> 웹서버 ==> 메인페이지 제공(index.html)
  
  

* XML : Extensible Markup Language
* HTML : hyperText Markup Language



## xml $ html

* 정적 페이지 : 변하지 않는 데이터
* 동적 페이지 : jsp, asp php 등



* html 역사

  인터넷에서 서버와 클라이언트간에 데이터를 주고받기 위한 약속, 공용어

  



구조화된 문서(xml) : 정적 페이지

비구조화된 문서(html) : 정적 페이지



클라이언트(날씨 클릭) -> 웹서버(날씨 페이지(동적, jsp) 생성) -> 생성된 페이지를 html형식의 문서로 만들어서 제공 -> 웹브라우저 해석 -> 결과를 화면에 출력

출력 : 오늘의 날씨는 맑습니다. 기온은 섭씨 영하 2도입니다.



## 문서의 종류

BTS를 검색하고 싶은데 기억이 안날 때 우회적으로 노래제목, 맴버들, ... 를 검색하게 됨



**비구조화된 문서(HTML)**: 웹페이지 내용에 대해 기계가 해석하지 못하는 문서 -> 검색어를 기반으로 검색

ex) BTS가 서울 강남구에서 공연을 했습니다.



**구조화된 문서(XML)** : 웹페이지 내용에 대해 기계가 해석 가능한 문서 -> 의미를 기반으로 검색

-> 검색 폭 넓음, 검색 결과에 대한 정확도 높음

BTS가 서울 강남구에서 공연을 했습니다.

<가수> (꺽쇠를 **태그**라 부름)

​	<그룹명>BTS</그룹명>

​	<도시이름>서울</도시이름>

​	<구이름>강남구</구이름>

​	<맴버이름>........</맴버이름>

</가수>

대부분의 문서는 비구조화된 문서 





강사님 딕셔너리에서 특정 value값을 기준으로 key와 value를 출력하고 싶을때는 어떤방법으로 하는건가요?

 예를 들어서

{'a':1, 'b':2, 'c':3, 'd':4}일 떄 



## 실습

* 

  ```
  import urllib.parse as parse
  import urllib.request as requst
  addr="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
  values={'stdId':'109'}
  
  params=parse.urlencode(values)
  url=addr+"?"+params
  print(url)
  print("@"*50)
  data=requst.urlopen(url).read()
  data=data.decode('utf-8')
  print(data)
  ```



## BeatifulSoup : 웹스크래핑 패키지

파이참 -> 세팅 -> 프로젝트 -> 하단 + -> beatufulsoup4 install

```
from bs4 import BeautifulSoup
```

```
html='''
<html><body>
<h1>스크래핑</h1>
<p>웹 페이지 분석</p>
<p>원하는 부분 추출</p>
</body></html>
'''

soup=BeautifulSoup(html, "html.parser")
#붕어빵 봉투 = 붕어빵 기계(밀가루,10cm)
print(soup.html.body.h1)   			#soup.<맨 바깥>.<그 안> <그.안>
print(soup.html.body.p)
print(soup.html.body.p.string)


<h1>스크래핑</h1>
<p>웹 페이지 분석</p>
웹 페이지 분석
```


 동일한 수준에 같은 명칭이 여러개 있을 때


```
soup=BeautifulSoup(html, "html.parser")
p1=soup.html.body.p 							# 엔터(줄바꿈)가 나옴
p2=p1.next_sibling
print(p2.next_sibling)
<p>원하는 부분 추출</p>
```

```
soup=BeautifulSoup(html, "html.parser")
p1=soup.html.body.p # 엔터(줄바꿈)가 나옴
p2=p1.next_sibling.next_sibling.string
print(p2)                                          #조금 더 간단하게 나옴
```

```
soup=BeautifulSoup(html2, "html.parser")
print(soup.html.body.h1.string)					  #타고타고타고 들어가는 방법
print(soup.find(id='title').string)               #아이디를 부여하고 그걸 찾을 수 있음
스크래핑
스크래핑
```

```
print(soup.find(id='body').string)
웹 페이지 분석
```

```
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
# <태그명 속성명=속성값 속성명=속성값...>
# a태그 값 찾기
soup=BeautifulSoup(html3, "html.parser")
print(soup) #<class 'bs4.BeautifulSoup'> 		#html파서로 분석할 수 있는 객체로 변환
print(html3) #<class 'str'>
print(soup.find_all("a")) # 리스트의 요소로 저장이 됨
print(html3.find_all("a")) # 에러나옴
```

```
soup=BeautifulSoup(html3, "html.parser")
links=soup.find_all("a") # 리스트의 요소로 저장이 됨
for i in links:
    href=i.attrs['href']          # attribute속성
    na=i.string
    print(na,"-->", href)        # a 태그를 찾아내고 그 안에있는 속성같을 찾아냄
    
naver --> http://www.naver.com
daum --> http://www.daum.com
```

```
html4='''
<p><a href="aaa.html name=asdqw">aaa page</a></p>
'''
soup=BeautifulSoup(html4,"html.parser")
print(soup.p.a.string)  
print(soup.a.string)  #p태그를 안써도 출렫  -->  a태그가 여러곳에 산지해 있는경우에는 p태그를 써줘야함
aaa page
aaa page


print(soup.a.attrs) # dict형태로 나옴!@#!@##
{'href': 'aaa.html'}

mydict=soup.a.attrs
print('href' in mydict)      #딕셔너리에 href키가 있냐
{'href': 'aaa.html name=asdqw'}
True
```



## 웹 스크래핑 가져와서 해보기

```
import urllib.request as req

url='http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
res=req.urlopen(url)
print(res)
<http.client.HTTPResponse object at 0x00000194C866BD60>      #HTTPResponse : 과자의 포장지같은 느낌
```

* 정상응답 --> 200 : ok
* 문서를 찾지 못한경우 --> 40x

* 서버 자체 오류 --> 50x

```
soup=BeautifulSoup(res, "html.parser")
print("문서 제목 :",soup.title.string)
print(soup.find("title"))
print(soup.find_all("title"))
print(soup.find_all("title")[0])

문서 제목 : 기상청 육상 중기예보
<title>기상청 육상 중기예보</title>
[<title>기상청 육상 중기예보</title>, <title>전국 육상 중기예보 - 2021년 01월 13일 (수)요일 06:00 발표</title>, <title>전국 육상중기예보</title>]
<title>기상청 육상 중기예보</title>
```

```
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
print(soup.select("div"))
[<div id="lang">
<h1>프로그래밍언어</h1>     #제목
    <ul class="items">       # unordered list 
        <li>python</li>
<li>java</li>
<li>cpp</li>
</ul>
</div>]


print(soup.select("div#lang > h1")[0].string) #select함수에서는 > 가 ~안에 있다는 뜻임
프로그래밍언어


print(soup.select_one("div#lang > h1"))
<h1>프로그래밍언어</h1>

	
# soup.select("div#lang > ul.items > li") # 태그에 클래스 명을 지정할 때
mylist=soup.select("div#lang > ul.items > li")
for i in mylist:
    print(i.string)
python
java
cpp
```

