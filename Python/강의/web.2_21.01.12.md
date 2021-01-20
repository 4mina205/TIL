# web.2_21.01.12



## 실습


* ```
  \d : 숫자([0-9])dh krkxdma
  \D : not \d의미, [^0-9]와 같음
  
  \s : 공백문자, 탭문자, 엔터문자 등
  \S : not 공백문자, 탭문자, 엔터문자 의미
  
  \w : 문자 + 숫자를 의미, [a-zA-Z_]와 같음
  \W : not 문자 + 숫자를 의미, [^a-zA-Z0-9_]어ㅣ같음
  
  ? 또는 . : 문자가 1개만 있는지 판단
  ?는 문자가 0개 또는 1개인지 판단
  .은 문자가 1개인지 판단
  ab?c --> a + b가 있어도 없어도 됨 + c
  ```

  

* search vs match

  ```
  print(re.match("[a-z]+","python"))
  print(re.search("[a-z]+","python"))
  print(re.match("[a-z]+","7python"))
  print(re.search("[a-z]+","7python"))  #내가 원하는 키워드가 있는지 찾는 느낌? #search 결과는 1개으 ㅣ매치 객체가 리턴
  
  <re.Match object; span=(0, 6), match='python'>
  <re.Match object; span=(0, 6), match='python'>
  None
  <re.Match object; span=(1, 7), match='python'>
  ```

  ​    

* **findall** : 정규식과 매치되는 모든 문자열을 리스트로 리턴

  * 내가 원하는 것을 리스트형태로 리턴

  ```
  print(re.findall("[a-z]+","7python8java8cpp")) # 이거 사기다
  ['python', 'java', 'cpp']
  
  print(re.findall("[a-z]+","7python8java8cpp"))
  pat = re.compile("[a-z]+") #정의한 패턴을 pat에 저장
  res = pat.findall("7python8java8cpp")
  print(res)
  ['python', 'java', 'cpp']
  ```

  

* **finditer** : 정규식과 매치되는 모든 문자열을 **반복가능한 객체** 형태로 리턴(리스트, 튜플 등)

  ```
  res = re.finditer("[a-z]+","7python8java8cpp")
  for i in res:
  
      print(i)
  <re.Match object; span=(1, 7), match='python'>
  <re.Match object; span=(8, 12), match='java'>
  <re.Match object; span=(13, 16), match='cpp'>
  
  	print(i.start()) # 매치 시작 위치
  1
  8
  13
  
      print(i.end()) # 매치 끝 위치
  7
  12
  16
  
      print(i.group()) #대치된 문자열
  python
  java
  cpp
  
      print(i.span()) # 매치 시작, 끝 위치
  (1, 7)
  (8, 12)
  (13, 16)
  ```

  

* . (점)  메타문자는 모든 문자 1개와 매치. **예외**(줄바꿈 문자: \n)

  ```
  print(re.match("a.b","a0b"))
  <re.Match object; span=(0, 3), match='a0b'>
  
  print(re.match("a.b","a\nb"))
  None
  ```

  ```
  pat = re.compile("a.b", re.DOTALL) # 역슬래시를 포함 하겠다!
  print(pat.match("a\nb"))
  <re.Match object; span=(0, 3), match='a\nb'>
  ```



* 대소문자

  ```
  pat=re.compile("[a-z]")
  print(pat.match("python"))
  print(pat.match("Python"))
  
  <re.Match object; span=(0, 1), match='p'>
  None
  ```

  ```
  pat=re.compile("[a-z]",re.I) #I=ignorecase(대문자인지 소문자인지 무시하겠다)
  <re.Match object; span=(0, 1), match='P'>
  ```

  

* \ (역슬래시)

  ```
  print(re.search(r"\\sec", "asdfkdgjsdf\sec sadfasdf"))
  <re.Match object; span=(11, 15), match='\\sec'>
  ```

  

* 문자가 반복되는지 확인하고 싶을 때

  ```
  print(re.match("(hi){3}","hihihihelloworld"))
  ```

  소괄호는 문자 하나로 간주



* 한글 매치

  ```
  print(re.match("[ㄱ-ㅎ]+","ㅋㅋㅋ캬캬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"))
  ㅋㅋㅋ
  
  print(re.match("[ㄱ-ㅎ가-힣]+","ㅋ캬캬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"))
  <re.Match object; span=(0, 20), match='ㅋ캬캬ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ'>
  
  print(re.findall("[ㄱ-ㅎ가-힣]+","ㅋ캬캬ㅋsdfㅋㅋㅋㅋㅋㅋㅋㅋ123ㅋㅋㅋㅋㅋㅋㅋㅋ")) #한글만 추출
  ['ㅋ캬캬ㅋ', 'ㅋㅋㅋㅋㅋㅋㅋㅋ', 'ㅋㅋㅋㅋㅋㅋㅋㅋ']
  
  print(re.findall("[^ㄱ-ㅎ가-힣]+","ㅋ캬캬ㅋsdfㅋㅋㅋㅋㅋㅋㅋㅋ123ㅋㅋㅋㅋㅋㅋㅋㅋ")) #한글 제외한 모든 문자 추출
  ['sdf', '123']
  ```

  

* 활용!

  ```
  print(re.findall("[ㄱ-ㅎ가-힣]+",news))
  print(re.findall("[ㄱ-ㅎ가-힣]+[0-9]+",news))
  print(re.findall("[0-9]+[ㄱ-ㅎ가-힣]+",news))
  
  ['서울', '연합뉴스', '신선미', '기자', '국내', '신종', '코로나바이러스', '감염증', '코로나', '차', '대유행', '이', '완만한', '감소세로', '접어든', '가운데', '이번', '주', '신규', '확진자', '발생', '추이가', '주목된다', '신규', '확진자', '감소세', '지속이냐', '재확산이냐의', '흐름을', '가늠해', '볼', '수', '있기', '때문이다', '지난달', '말까지만', '해도', '연일', '천명', '안팎으로', '발생하던', '신규', '확진자는', '새해', '들어', '명대로', '줄었다가', '일', '명대', '중반까지', '더', '떨어진', '뒤', '일에는', '명대로', '소폭', '증가한', '상태다', '큰', '틀의', '통계만', '보면', '확실한', '감소', '내지', '안정국면으로', '접어드는', '것', '아니냐는', '관측이', '나온다', '하지만', '신규', '확진자가', '명', '명대까지', '낮아진', '데는', '주말과', '휴일', '검사건수', '감소', '영향도', '있어', '아직', '상황을', '낙관하기에는', '이르다는', '게', '감염병', '전문가들의', '공통된', '의견이다', '방역당국', '역시', '긴장의', '끈을', '풀기에는', '위험', '요인이', '너무', '많다며', '국민', '개개인의', '지속적인', '방역', '협조를', '당부하고', '있다']
  ['코로나19']
  ['3차', '1천명', '600명대로', '11일', '400명대', '12일에는', '500명대로', '400명', '500명대까지']
  ```

  

* 특수문자

  ```
  print(re.search("[*]","3*5"))
  print(re.search("[*]+","3**5"))
  <re.Match object; span=(1, 2), match='*'>
  <re.Match object; span=(1, 3), match='**'>
  
  print(re.search("\*","3*5"))
  print(re.search("\*+","3**5"))
  <re.Match object; span=(1, 2), match='*'>
  <re.Match object; span=(1, 3), match='**'>
  
  print(re.search("\$\([a-z]+\)","$(document)"))
  print(re.search("[$(a-z)]+","$(document)"))
  <re.Match object; span=(0, 11), match='$(document)'>
  <re.Match object; span=(0, 11), match='$(document)'>
  ```

  

* 그룹!

  ```
  print(re.search("\w+\s+\d+[-]\d+[-]\d+","kim 010-1234-5867"))
  <re.Match object; span=(0, 17), match='kim 010-1234-5867'>

  
  res=re.search("\w+\s+\d+[-]\d+[-]\d+","kim 010-1234-5867")
  print(res.group())
  print(res.group().split()[1])
  kim 010-1234-5867
  010-1234-5867
  ```
  
  ```
  res=re.search("(\w+)\s+\d+[-]\d+[-]\d+","kim 010-1234-5867")
  print(res.group(0)) # 0은 전체
  kim 010-1234-5867
  
  print(res.group(1))
  kim
  ```
  
  

* 그룹 찾기 쉽도옥 이름 부여 가능

  ```
  res=re.search("(?P<name>\w+)\s+(?P<num>\d+[-]\d+[-]\d+)","kim 010-1234-5867") #작성형식 : (?P<그룹명>)
  print(res.group('name'))
  kim
  print(res.group('num'))
  010-1234-5867
  ```

  