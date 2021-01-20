# # # print("8128".count('8'))
# #
# # sum=0
# # for i in range(10001):
# #     sum+=str(i).count('8')
# # print(sum)
# #
# # print(str(list(range(1,10000))).count('8'))
# #
# # f=open("hello.txt","w")
# # f.write('hello world')
# # f.close
# #
# # f=open("hello.txt","r")
# # s=f.read()
# # print(s)
# # f.close()
# #
# # # with open("hello.txt","r") as f:
# #     s=f.read()
# #     print(s)
# #
# # with open("hello.txt","w") as f:
# #     f.write("hello world 1\n") # w모드로 열게되면 기존에 작성되어 있던 내용은 사라짐(덮어쓰기)
# #     f.write("hello world 2\n")
# #     f.write("hello world 3\n")
# #
# #
# # with open("hello.txt","w") as f:
# #     for i in range(10):
# #         f.write("hello world {0}\n".format(i+1))
# # #
# #
# # # lines=['hello\n','nicetomeetyou\n','bye\n']
# # # with open("hello.txt","w")  as f:
# # #     f.writelines(lines)
# #
# #
# # #
# # # with open("hello.txt","r") as f:
#     line=None
#     while line !="":
#         line=f.readline()   # read line 함수는 한줄씩 읽어들임
#         print(line.strip("\n"))
# #
# # #
# with open("hello.txt","r") as f:
#     line = f.readlines()
#     for i in line:
#         print(i.strip("\n"))
# #
# # import pickle
# # 내용물 = "단팥"
# # 색상 = "파랑"
# # 너비 = "20cm"
# # 높이 = "10cm"
# # 가족명단 = {"잉어":30, "꽃게":10, "상어":40}
# #
# # with open("myfish.p","wb") as f:            # 객체 저장할때는 wb모드로 파일 열기
# #     pickle.dump(내용물, f)
# #     pickle.dump(색상, f)
# #     pickle.dump(너비, f)
# #     pickle.dump(높이, f)
# #     pickle.dump(가족명단, f)
# #
# # import pickle
# # with open("myfish.p","rb") as f:
# #     내용물 = pickle.load(f)
# #     색상 = pickle.load(f)
# #     너비 = pickle.load(f)
# #     높이 = pickle.load(f)
# #     가족명단 = pickle.load(f)
# #
# #     print(내용물)
# #     print(색상)
# #     print(너비)
# #     print(높이)
# #     print(가족명단)
# #
# #
# # # 엑셀 작업 --> 객체 저장(xls, binary) -->
# #
# #
# #
# # f=open("hello.txt", "a")
# # for i in range(3):
# #     f.write("%d sssss\n" % (i+1))
# #     f. close
# #
# #
# #
# #
# #
#
#
# # res=0
# # def add(n):
# #     global res    # n에 전달된 값을 res에 저장
# #     res+=n
# #
# # add(3)
# # print(res)
# # add(4)
# # print(res)
#
# # res1=0 # 전역변수 함수 바깥에 있는 변수
# # res2=0
# # def add1(n):
# #     global res1    # n에 전달된 값을 res에 저장
# # #     res1+=n
# # #     return res1
# # # print(add1(3000))
# # # print(add1(5000))
# # #
# # # def add2(n):
# # #     global res2    # n에 전달된 값을 res에 저장
# # #     res2+=n
# # #     return res2
# # # print(add2(1500))
# # # print(add2(2000))
# #
# #
# # class Calculator: # 클래스명 대문자로 시작하는게 관례임
# #     def __init__(self):
# #         self.res=0
# #         print("init함수가 호출됐네?")
# #     def add(self, n):
# #             self.res+=n
# #             #여기서 할인율 적용
# #             return self.res
# # # 붕어빵 기계에서 붕어빵을 제작 => __init__ 자동호출 -> res(내용물)=msg
# # cal1=Calculator() # 클래스로부터 객체를 생성(init함수 자동 호출, res=0으로 초기화. 계산대(클래스)로부터 계산대1(객체==cal1)을 생성
# # cal2=Calculator()
# #
# # print(cal1.add(3000))
# # print(cal1.add(5000))
# #
# # print(cal2.add(1500))
# # print(cal2.add(2000))
# #
# # # 모듈? 파이선 파일
#
# # import mod1
# # print(mod1.madd(1,2))
#
# #
# # import mod1 as m
# # print(m.madd(1,2))
# #
# # import pandas as pd
# # import numpy as np
# # import  matplotlib.pyplot as plt
# #
# #
# # from mod1 import msub
# # print(msub(2,1))
# #
# #from mod1 import msub,madd

# 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
# def is_odd(a):
#     if a%2==1:
#         print("홀수")
#     else:
#         print("짝수")


# 2. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
# with open("test.txt","a") as test:
#     test.write("life is too short\n") # w모드로 열게되면 기존에 작성되어 있던 내용은 사라짐(덮어쓰기)
# with open("test.txt","r") as test:
#     line=None
#     while line !="":
#         line=test.readline()   # read line 함수는 한줄씩 읽어들임
#         print(line.strip("\n"))


# 3. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# Life is too short
# you need java
# with open("test.txt","a") as test1:






# 4. "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
# def print_coin():
#     print("비트코인")


# 5. 4에서 정의한 함수를 호출하라.
# print_coin()

# 6. 4에서 정의한 print_coin 함수를 100번호출하라.
# for i in range(100):
#     print_coin()

# 7. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
# def print_coins():
#     for i in range(100):
#         print_coin()


# 8. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일  문자열을 이어 붙여 출력하는 print_with_smile 함수를정의하라.
# def print_with_smile(a):
#     print(a,":D")



# 9. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
# def print_upper_price(price):
#     price+=0.3*price
#     print("상한가 :",int(price),"원")



# 10. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# def print_even(numlist):
#     for x in numlist:
#         if x%2 == 0:
#             print(x)



# 11. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# def print_keys(dic):
#     print(dic.keys())


# 12. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.

# def print_mxn(string, num):
#     print(string[:num])


# 13. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지
# 급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)
# def calc_monthly_salary(annual_salary):
#     print(int(annual_salary/12))

# 14. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# def make_url(homepage):
#     print("www."+homepage+".com")
# make_url("naver")

# 15. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']

# def make_list(string):
#     print(list(string))





# 16. 게임 기업 입사문제
# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# 예를 들어
# d(91) = 9 + 1 + 91 = 101
# # 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# # 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다. 그런데 반대로, 제네레이터가
# 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다. 예를 들어 1,3,5,7,9,20,31 은
# 셀프 넘버 들이다. # 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.

# set_allnum=set(range(1,5001))
# list_nselfnum=[]
# for i in range(1,5001):
#     list_nselfnum.append(i + sum(map(int, str(i))))
# set_nselfnum=set(list_nselfnum)
# set_sum_selfnum=sum(set_allnum-set_nselfnum)
# print(set_sum_selfnum)










# 17. 최대낙차


# first_box=[7,4,2,0,0,6,0,7,0]
# mid_box=list(range(1,10))
# box=[]
# for y in [7,4,2,0,0,6,0,7,0]:
#     sum=0
#     for x in [1,2,3,4,5,6,7,8,9]:
#         if y>=x:
#             sum+=1
#             print(sum)
#         print(sum)
first_box=[7,4,2,0,0,6,0,7,0]
second_box=[]
for x in range(1,10):
    sum=0
    for y in first_box:
        if y>=x:
            sum+=1
    second_box.append(sum)              # 90도 회전했을 때 [5, 5, 4, 4, 3, 3, 2, 0, 0]
print(second_box)


