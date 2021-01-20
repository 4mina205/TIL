# web.1_21.01.11



## 실습

* 맵함수 활용

  ```
  def twoTimes(n):
      return n*2
  res=list(map(twoTimes, [1,2,3]))
  print(res)
  [2, 4, 6]
  ```

  

* pow함수 활용

  ```
  print(pow(3,2))
  9
  ```



* round함수 : 소수점 반올림

  ```
  print(round(3.141592,4))
  3.1416
  ```

  

* zip함수 : 같은 위치끼리 (튜플형식으로) 묶음

  ```
  print(list(zip([1,2],[3,4],[5,6],[7,8])))
  [(1, 3, 5, 7), (2, 4, 6, 8)]
  ```

  

* filter 함수 : 특정 조건으로 걸러진 요소들을 묶어서 리턴

  map과의 차이점이라면, 함수의 결과가 참/거짓인지에 따라 요소를 포함할지 결정

  * for, if 사용시

    ```
    t=list(range(1,11))
    def isEven(n):
        return True if n%2==0 else False
    res=[]
    for v in t:
        if isEven(v):
            res.append(v)
    print(res)
    [2, 4, 6, 8, 10]
    ```

  * filter 사용시

    ```
    t=list(range(1,11))
    def isEven(n):
        return True if n%2==0 else False
    print(list(filter(isEven,t)))
    [2, 4, 6, 8, 10]
    ```

  *  lamda 사용시

    ```
    print(list(filter(lambda x: x%2==0, t)))
    [2, 4, 6, 8, 10]
    ```

    

* os 모듈 : 디렉토리, 파일의 경로 등 확인/제어

  ```
  import os
  print(os.environ) #내pc 환경(사용일 거의 x)
  print(os.getcwd()) #현재 작업 경로 확인
  os.mkdir("sample") #현재 작업 위치에 폴더 생성
  os.rmdir("sample") #폴더 제거
  os.rename("sample","test") # 폴더명 변경
  ```

  

* sh util 모듈

  ```
  import shutil
  shutil.copy("hi.txt", "hicopy.txt") # 복사 가능
  ```

  

* glob

  ```
  import glob
  print(glob.glob("C:/Users/SAMSUNG/PycharmProjects/*"))
  ```





## 웹

* 주민번호 뒷자리

  ```
  jumin="""
  park 940907-1212121
  kang 151515-9797979
  """
  for line in jumin.split("\n"):
      for word in line.split(" "):
          if len(word)==14:
              word=word[:6]+"-"+"*******"
              print(word)
  940907-*******
  151515-*******
  
  
  jumin="""
  park 940b07-1212121
  kang 151515-9797979
  """
  for line in jumin.split("\n"):
      for word in line.split(" "):
          if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
              word=word[:6]+"-"+"*******"
              print(word)
  151515-*******
  
  
  d="1234"
  print(d.isdigit())
  True
  
  ```

  

* 정규표현식 compile

  ```
  jumin="""
  park 940b07-1212121
  kang 151515-9797979
  """
  import re # regular expression(정규표현식 모듈)
  p=re.compile("(\d{6})[-]\d{7}")#정규식 작성
  print(p.sub("\g<1>-*******",jumin))
  park 940b07-1212121
  kang 151515-*******
  주민번호가 정상인경우 변환되지만, 정상적이지 않은경우는 변환이 안됩
  정상적인 주민번호에 대한 일반적인 규칙을 정의
  ```

  

* 정규표현식 match :

  '문자열'이 '패턴'에 부합되나요?

  패턴에 대한 정의를 잘 해야함

  ```
  re.match("패턴","문자열") 문자열이 패턴으로 시작해야함
  ```

  ```
  print(re.match("hello","hello, world"))
  # "hello, world" #문자열에 hello 문자열이 있는지 판단
  <re.Match object; span=(0, 5), match='hello'>
  
  
  print(re.match("hi","hello, world"))
  None
  
  
  if re.match("hello","hello, world"):
      print("주어진 hello, world 문자열은 hello(문자열)패턴에 매치가 되었습니다.")
  else:
      print("매치 x")
  주어진 hello, world 문자열은 hello(문자열)패턴에 매치가 되었습니다
  ```

  

  위치 찾는거는 find로도 가능

  ```
  print("hello, world".find("world"))
  7
  ```



* 특정 문자열이 맨앞/뒤에 오는지 판단

  * 문자열 맨 앞에 ^를 붙이면 맨 앞에 오는지 판단
  * 문자열 맬 끝에 $를 붙이면 맨 뒤에 오는지 판단

  ```
  re.search 문자열의 처음과 끝이 부합하냐
  ```

  ```
  print(re.search("^hello","hello, world")) #hello로 시작하는지 확인
  <re.Match object; span=(0, 5), match='hello'>
  
  
  print(re.search("world$","hello, world")) #world로 끝나는지 확인
  <re.Match object; span=(7, 12), match='world'>
  ```

  

* match

  ```
  print(re.match("hello|world","hello")) # hello또는 world 패턴에 문자가 부합하느냐
  <re.Match object; span=(0, 5), match='hello'>
  
  
  print(re.match("hi|world","hello"))
  None
  ```



* 메타문자 (메타 : 정보의 정보, 데이터(전화번호부)의 데이터(색인))

  * 메타문자의 종류 : [], (), {}, \, |, ?, +, *, $, ^

  *  [] 메타문자 : 대괄호 안에는 어떤 문자도 올 수 있음

    * ex) [abcdef] 의미? a,b,...,f 중에서 어떤 한 개의 문자와매치

    ```
    import re
    
    print(re.match("[abcdef]","a"))
    <re.Match object; span=(0, 1), match='a'>
    
    
    print(re.match("[abcdef]","g"))
    None
    
    
    print(re.match("[abcdef]","abc"))   # 이 중 하나만 매치되면 됨
    <re.Match object; span=(0, 1), match='a'>
    
    
    print(re.match("[abcdef]","c"))
    <re.Match object; span=(0, 1), match='c'>
    ```

    ```
    [from-to]
    [a-d] 정규식 의미:[abcd],[a-f]==[abcdef]
    [0-r]==[012345]
    ```

    ```
    print(re.match("[0-9]","1234")) # 1234는 0~9까지 숫자에 해당 
    <re.Match object; span=(0, 1), match='1'>
    
    
    print(re.match("[0-9]*","1234")) # *은 문자(솟자)가 0개 이상 있는지 확인
    <re.Match object; span=(0, 4), match='1234'>
    
    
    print(re.match("[0-9]*","a1234")) # a1234에서 a는 [0-9]범위가 아님. 원래는 none가 나와야 하지만 *이 있기 떄문에  0개 매칭 된걸로 나옴
    <re.Match object; span=(0, 0), match=''>
    ```

    ```
    print(re.match("[0-9]+","1234")) # 1개 이상 있는지 확인
    <re.Match object; span=(0, 4), match='1234'>
    
    
    print(re.match("[0-9]+","12a34"))
    <re.Match object; span=(0, 2), match='12'>
    
    
    print(re.match("[0-9]+","a1234")) # +는 1개 이상 매치하냐를 따지기 때문에 0개면 none출력 (*과+의 차이점)
    None
    ```

    [a-z] : 소문자 전체

    [A-Z] : 대문자 전체

    [a-zA-Z] : 알파벳 전체

    [^0-9] : 0~9(숫자)를 제외한 문자  ( 대괄호 안에 있을때 ^는 반대의 의미)

    

  * re.search

    ```
    print(re.search("^hi", "hello, hi")) # 여기서 ^는 ^()로 시작을 해야 함 (시작하지 않으므로 none
    None
    
    
    print(re.search("hi", "hello, hi"))
    <re.Match object; span=(7, 9), match='hi'>
    ```

  * re.match

    ```
    print(re.match("hi", "hello, hi")) # match는 hi로 시작해야함
    None
    ```

  * | 메타문자

    ```
    print(re.match("hi|hello|good", "hello, hi"))
    <re.Match object; span=(0, 5), match='hello'>
    
    
    print(re.match("hi|hello|good", "goodhello, hi"))
    <re.Match object; span=(0, 4), match='good'>
    ```

  *  [] 에서 *와 + 차이

    ```
    print(re.match("[0-9]","12a34"))
    <re.Match object; span=(0, 1), match='1'>
    
    
    print(re.match("[0-9]*","12a34")) #숫자가 0개 이상 있는지 판단
    <re.Match object; span=(0, 2), match='12'>
    
    
    print(re.match("[0-9]+","12a34")) #숫자가 1개 이상 있는지 판단
    <re.Match object; span=(0, 2), match='12'>
    
    
    print(re.match("[0-9]*","a12a34")) #숫자가 0개 이상 있는지 판단
    <re.Match object; span=(0, 0), match=''>
    
    
    print(re.match("[0-9]+","a12a34")) #숫자가 1개 이상 있는지 판단
    None
    ```

    ```
    print(re.match("[a-z]*","12a34")) #알파벳 문자가 0개 이상 있는지 판단
    <re.Match object; span=(0, 0), match=''>
    
    
    print(re.match("[a-z]+","12a34")) #알파벳 문자가 1개 이상 있는지 판단
    None
    
    
    print(re.match("[a-z]*","aabb12a34")) #알파벳 문자가 0개 이상 있는지 판단
    <re.Match object; span=(0, 4), match='aabb'>
    
    
    print(re.match("[a-z]+","aabb12a34")) #알파벳 문자가 1개 이상 있는지 판단
    <re.Match object; span=(0, 4), match='aabb'>
    ```

  * []를 빼면 match는 어떤 의미냐

    ```
    print(re.match("ab","abc"))
    <re.Match object; span=(0, 2), match='ab'>
    
    
    print(re.match("ba","abacba"))
    None
    ```

  * []를 빼면 search는 어떤 의미냐

    ```
    print(re.search("ab","abc"))
    <re.Match object; span=(0, 2), match='ab'>
    
    
    print(re.search("ba","abcba"))
    <re.Match object; span=(1, 3), match='ba'>
    ```

  * []를 뺀 match에서 *, +

    ```
    print(re.match("a*","b"))   # *은 *앞에 있는 문자가 0개 이상 나왔을 때 매치
    <re.Match object; span=(0, 0), match=''>
    
    
    print(re.match("a+","b"))
    None
    
    
    print(re.match("b*","b"))
    <re.Match object; span=(0, 1), match='b'>
    
    
    print(re.match("a*b","b")) # a문자가 0개 이상 있고 b가 나오면 매치
    <re.Match object; span=(0, 1), match='b'>
    
    
    print(re.match("a*b","bb"))
    <re.Match object; span=(0, 1), match='b'>
    ```

    ```
    print(re.match("a+b","b"))  #a문자가 1개 이상 나와야하고 반드시 b가 그 뒤로 나와야 함
    None
    
    
    print(re.match("a+b","ab"))
    <re.Match object; span=(0, 2), match='ab'>
    
    
    print(re.match("a+b","aaabb")) # aaab까지만 매치
    <re.Match object; span=(0, 4), match='aaab'>
    
    
    print(re.match("a+b","aaaaaaaaabbbbbb")) #aaaaaaaaab까지만 매치
    <re.Match object; span=(0, 10), match='aaaaaaaaab'>
    
    
    print(re.match("a+b+","aaaaaaaaabbbbbb")) #aaaaaaaaabbbbbb까지 매치
    <re.Match object; span=(0, 15), match='aaaaaaaaabbbbbb'>
    ```

