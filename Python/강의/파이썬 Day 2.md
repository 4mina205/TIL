# 파이썬 Day 2



## 파이썬 특징

* 매우 인간적인 언어
  	프로그래밍(언어:파이썬, ...)  -->  프로그램(app)
  	[프로그래밍]이란 우리가 생각하는 것을 컴퓨터에 지시하는 행위

* 리스트 : []
  튜플 : ()
  딕셔너리 and 셋 : {}

## 파이썬으로 할 수 있는 것

유틸리티 (소프트웨어(벡신))

GUI(Graphical User Interface)프로그램

웹 프로그래밍

DB 프로그래밍

데이터 분석(분석을 파이썬으로 하는것이 아니라 파이썬에 추가적으로 패키지(pandas)를 설치하여 진행)

IoT

## 파이썬 실습

* print 함수 : print() 

  ```
  print("hello, world")
  ```
  ```
  C:\Users\SAMSUNG\PycharmProjects\pythonbasic\venv\Scripts\python.exe C:/Users/SAMSUNG/PycharmProjects/pythonbasic/pythonmaster96.py
  hello, world
  
  Process finished with exit code 0
  ```



* a=1 #assign 의미



* 들여쓰기

  ```
  a=10
  if a==10:
      print('True') # True
  ```
  
  

* 코드블록 : 들여쓰기가 동일한 코드 집합



* 사칙연산

  ```
  print(1+1) #2
  print(1/2) #0.5
  print(5*8) #40
  print(5//3) #1 (몫만 나옴)
  print(6//3.0) # 2.0
  ```

  

* 나머지 연산자

  ```
  print(7%4) 	#3
  ```

  

* 거듭제곱 연산자

  ```
  print(2**3) #8
  ```

  

* int

  ```
  print(int(3.3)) #3
  print(int(5/2)) #2
  print('10') #str
  print(int('10')) #int
  ```

  

* type

  ````
  print(type(10)) #<class 'int'>
  ````

   

* divmod(x,y) : x(피제수, 나누는 수)를 y(제수, 나뉨 수)로 나눈 후 몫과 나머지 표시

  ```
  print(divmod(15,7)) #(2, 1)
  ```

  

* 함수 괄호 안에 나타내는 데이터 

  ex) divmod(9, 4) ---> 9 : 첫 번째 인수, 4 : 두 번째 인수

  함수(인수1, 인수2)



* 함수의 연산 결과를 저장할 때는 대입 연산자 사용

  ```
  res = divmod(9, 4)
  print(res) # (2, 1)
  ```

  

* 튜플 이해하기

  ```
  res = divmod(9, 4)
  print("결과 :", res) # 결과 : (2, 1)
  ```

   튜플에 저장된 각각을 요소라 부름

  ```
  res = divmod(9, 4)
  print("1번째 요소 :", res[0]) # 1번째 요소 : 2
  ```

  대괄호 0 은 퓨틀에 저장된 첫 번째 요소값을 출력

  첫 번째 데이터가 0임, 두 번째는 1

  ```
  res = divmod(9, 4)
  print("1번째 요소 :", res[1]) # 1번째 요소 : 1
  ```

  **튜플, 리스트에서 데이터의 위치는 0번부터 시작한다** (인덱스를 잘못주지 않도록 주의)



* 각 요소를 바로 변수로 지정 가능

  ```
  res1, res2 = divmod(9, 4)
  print("1번째 요소 :", res1) # 1번째 요소 : 2
  print("2번째 요소 :", res2) # 2번째 요소 : 1
  ```



* 디버깅 : 에러를 수정하는 것

  

* 진수 표기

  ```
  print(11) #11(10진수)
  print(0b11) #3(2진수)
  print(0o11) #9(8진수)
  print(0x11) #17(16진수)
  ```

  

* float함수 : 정수를 실수로

  ```
  print(float(5)) #5.0
  print(float('3.14')) #3.14
  print(float('3.14'*2)) #error
  print(float('3.14')*2) #6.28
  ```

  

* 문장 출력 팁

  ```
  print("Kim\'s computer") # Kim's computer
  print(r"Kim's computer") # Kim's computer
  
  
  print("안녕!\n반가워요 잘있어요")
  
  # 안녕!
    반가워요 잘있어요
  ```

  

* seperator

  ```
  print("naver", "kakao", "samsung") # naver kakao samsung
  ```

  ```
  print("naver", "kakao", "samsung", sep='$') # naver$kakao$samsung
  ```

  

* end

  ```
  print("안녕")
  print("하세요")
  
  # 안녕
    하세요
    
    
  print("안녕",end="");print("하세요")
  
  # 안녕하세요
  ```

  

* 연산자 우선순위

  ```
  print((1+2)*3) # 9
  ```

  

* 변수를 한번에 많이 설정하는 방법

  ```
  a, b, c = 1, 2, 3 #행렬느낌?
  print(a,b,c)
  # 1 2 3
  
  a=b=c=1
  print(a,b,c)
  
  # 1 1 1 (# d=1 => c=d => b=c => a=b)
  ```

  

* 변수값 바꾸기

  ```
  x,y=1,2
  x,y=y,x
  print(x,y)
  
  #2, 1
  ```

  

* 변수 지정과 삭제

  a변수 설정

  ```
  a=1 #메모리에 a라는 공간을 만들고, 1을 저장해라
  ```

  a변수 삭제

  ```
  del a #메모리에서 a공간 삭제
  ```

  

* 변수만 만들고 값 지정 안하는 경우

  ```
  a=None
  print(a)
  
  # None
  ```

  

* 지정된 변수값의 연산(축약형 연산자)

  ```
  x = 10
  x += 10
  print(x)
  
  # 20
  ```

  

* input함수

  (내용)입력을 받은 뒤 엔터 키를 누르면 다음 문장으로 이동

  ```
  x = input("숫자를 입력하시오")
  print("당신이 입력한 값은 : ", x)
  
  # 숫자를 입력하시오50
    당신이 입력한 값은 :  50
  ```

  ```
  x = input("첫 번째 숫자를 입력하시오")
  y = input("두 번째 숫자를 입력하시오")
  print("덧셈 결과는 :", x+y)
  
  # 첫 번째 숫자를 입력하시오1
    두 번째 숫자를 입력하시오2
    덧셈 결과는 : 12   #(input은 문자로 간주)
  ```

  ```
  x = int(input("첫 번째 숫자를 입력하시오"))
  y = int(input("두 번째 숫자를 입력하시오"))
  print("덧셈 결과는 :", x+y)
  
  # 첫 번째 숫자를 입력하시오1
    두 번째 숫자를 입력하시오2
    덧셈 결과는 : 3 #(int함수로 정수 변환)
  ```

  ```
  x = float(input("첫 번째 숫자를 입력하시오"))
  y = float(input("두 번째 숫자를 입력하시오"))
  print("덧셈 결과는 :", x+y)
  
  # 첫 번째 숫자를 입력하시오3.14
    두 번째 숫자를 입력하시오5
    덧셈 결과는 : 8.14
  ```

  ```
  a,b = input("두 수를 입력하세요").split()          # split은 공백으로 나눠서 저장
  print(a)                                        # 공백으로만 나눠준다면 숫자든 문자든 상관없음
  print(b)
  
  # 두 수를 입력하세요1 2
    1
    2
  ```

  

* split함수

  ```
  print("안 녕 하 세 요".split())
  
  # ['안', '녕', '하', '세', '요']
  ```

  ```
  x1, x2 = map(int,input(" 숫자 두 개 입력 :").split(",")) # 컴마 문자로 입력데이터를 분리
  print(x1+x2)
  
  # 숫자 두 개 입력 :1,2
    3
  ```

* 간단 예제

  
  숫자 두 개 입력 : 1 2 (앤터) 3 출력되도록
  

  ```
  a,b = input("숫자 두 개를 입력하세요 :").split()
  print(int(a)+int(b))
  
  # 숫자 두 개를 입력하세요 :1 2
    3
  ```

  

* map함수

  mapping : 사상  x --> f --> y

  함수출력 = map(함수, 함수입력)

  ```
  x1, x2 = map(int, ['3', '4'])
  print(x1+x2)
  
  # 7
  ```

  ```
  a,b = map(int,input(" 숫자 두 개를 입력하세요 :").split())
  print(a+b)
  
  # 3
  ```

  

* 문자열 입력 방법 """  """

  ```
  y = """인생을 짧다, 그래서 파이썬이 필요하다."""
  print(y)
  
  # 인생을 짧다, 그래서 파이썬이 필요하다.           #문자열을 저장할 떄 여러개의 문장을 저장하는 경우
  
  
  y = """
  인생을 짧다,
  그래서 
  파이썬이 
  필요하다."""
  print(y)
  
  # 인생을 짧다,
    그래서 
    파이썬이 
    필요하다.                  # 여러줄의 문자 데이터를 """ """로 묶어서 저장하면 편함
  ```

  

* len함수 : 문자열 길이를 정수로 출력

  ```
  x = "life is too short"
  print(len(x))
  
  # 17
  ```

  

* 인덱싱 : 변수에 저장된 문자열에 대해 위치를 지정하여 참조하는 행위

  ```
  x = "life is too short"
  print(x[0]) # 위치(인덱스) 는 항상 0부터 시작
  
  # l
  
  
  x = "life is too short"
  print(x[-1])
  
  # t           # (-)기호는 뒤에서부터 참조
  ```

  ```
  x = "life is too short"
  print(x[5]+x[6])
  
  # is
  ```

  ```
  x = "life is too short"
  print(x[5:7])                 # 글자가 2개인데 [5:7]하는이유
                                # 범위 지정하여 슬라이싱할 때는 [시작위치 : 끝위치 +1]
  # is                          # 5 <= x < 7 의미
  ```

  ```
  x = "life is too short"
  print(x[12:17])
  
  # short
  ```
  
  
  ```
  x = "life is too short"
  print(x[12:])
  
  # short
  ```
```
  x = "life is too short"
  print(x[-5:])
  
  # short
```

  ```
  x = "life is too short"
  print(x[:4])
  
  # life
  ```

  ```
  x = "life is too short"
  print(x[8:-3])
  
  # too sh                       # -3 위치는 포함하지 않고 그 앞에까지만 추출
  ```

  

* 슬라이싱의 의미

  데이터 분석할 때 자주 쓰임

  ex)

  ​	"20201229" ==> 년/월/일 단위로 나누고 싶을 떄

  ​	먼저 분리작업을 해야한다.



* 문자 vs 문자열

  문자 : p, y, t, h,o, n

  문자열 : python

  ```
  x = "pithon"
  x[1] = "y"
  
  # 에러                     # 문자열의 요소값은 변경이 안됨
  ```

  ```
  x = "pithon"
  print(x[0:1]+"y"+x[2:])
  
  # python                   # 결론 : 수고스럽지만 찾아가서 바꾸자
  ```

  

* 포매팅

  %s : string

  %d : decimal

  %f : float

  ```
  x = 3
  print("I eat %d eggs" % x)                                 # %d (decimal)
  
  # I eat 3 eggs
  ```

  ```
  x = 'two'
  print("I eat %s eggs" % x)                                # %s (string)
  
  # I eat two eggs
  ```

  ```
  x = 'two'
  d = 3
  per = 30
  print("I eat %s eggs. so I was sick for %d days. %d%%" % (x, d, per))          # % 여러개 쓸 때는 ( , )로 묶는다
  
  # I eat two eggs. so I was sick for 3 days. 30%
  ```

  

## 연습문제

### 1. 첫번째와 세번째 문자를 출력하세요.

```
letters = 'python'
print(letters[0], letters[2])

# p t
```




### 2.뒤에 4자리만 출력하세요.
```
cn ="24가 2210"
print(cn[4:])

# 2210
```



### 3. 문자열에서 '파' 만 출력하세요.

```
s = "파이썬파이썬파이썬"
print(s[0], s[3], s[6])

# 파 파 파
```



### 4.문자열 '720'를 정수형으로 변환해보세요.

```
num_str = "720"
print(int(num_str))

# 720
```



### 5. 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.

```
data = "15.79"
print(float(data))

# 15.79
```



### 6. 에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서

### 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요.
```
mon_pri = 48584
mon_ins = 36
print("총 금액 :", mon_pri*mon_ins,"원")

# 총 금액 : 1749024 원
```