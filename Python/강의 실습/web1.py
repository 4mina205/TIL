# # 정규표현식 : 복잡한 문자열 처리 (퇴근시간을 대폿 단축)
# jumin="""
# park 940b07-1212121
# kang 151515-9797979
# """
#
# for line in jumin.split("\n"):
#     for word in line.split(" "):
#         if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
#             word=word[:6]+"-"+"*******"
#             print(word)
#
#
# d="1234"
# print(d.isdigit())



############# 정규표현식 #############
# jumin="""
# park 940b07-1212121
# kang 151515-9797979
# """
# import re # regular expression(정규표현식 모듈)
# p=re.compile("(\d{6})[-]\d{7}")#정규식 작성 #\d는 디짓의 의미 [-]는 반드시 한글자가 등장해야함
# print(p.sub("\g<1>-*******",jumin))
# # 주민번호가 정상인경우 변환되지만, 정상적이지 않은경우는 변환이 안됩
# # 정상적인 주민번호에 대한 일반적인 규칙을 정의


############# match를 이용해서 정규표현식 #############
# re.match("패턴","문자열")
# '문자열'이 '패턴'에 부합되나요?
# 패턴에 대한 정의를 잘 해야함
# print(re.match("hello","hello, world"))
# "hello, world" #문자열에 hello 문자열이 있는지 판단
# <re.Match object; span=(0, 5), match='hello'>

# print(re.match("hi","hello, world"))
# None

# if re.match("hello","hello, world"):
#     print("주어진 hello, world 문자열은 hello(문자열)패턴에 매치가 되었습니다.")
# else:
#     print("매치 x")
# 주어진 hello, world 문자열은 hello(문자열)패턴에 매치가 되었습니다.
# print("hello, world".find("world"))

# print(re.search("^hello","hello, world")) #hello로 시작하는지 확인
# print(re.match("hi|world","hello"))

# 정규표현식 메타문자 (메타 : 정보의 정보, 데이터(전화번호부)의 데이터(색인) )
# 메타문자 종류 : (), {}, [], \, |, ?, +, *, $, ^
# [] 메타문자 : 대괄호 안에는 어떤 문자도 올 수 있음
# * ex) [abcdef] 의미? a,b,...,f 중에서 어떤 한 개의 문자와 매치
# 'a' 문자는 정규표현식에 매치됨
import re
# print(re.match("[abcdef]","a"))
# print(re.match("[abcdef]","g"))
# print(re.match("[abcdef]","abc"))
# print(re.match("[abcdef]","c"))
# print(re.match("[abcdef]","g"))

#[from-to]
#[a-d] 정규식 의미:[abcd],[a-f]==[abcdef]
#[0-r]==[012345]
# print(re.match("[0-9]","1234")) # 1234는 0~9까지 숫자에 해당
# print(re.match("[0-9]*","1234")) # *은 문자(솟자)가 0개 이상 있는지 확인
# print(re.match("[0-9]*","a1234")) # a1234에서 a는 [0-9]범위가 아님. 원래는 none가 나와야 하지만 *이 있기 떄문에  0개 매칭 된걸로 나옴
#
#
# print(re.match("[0-9]+","1234")) # 1개 이상 있는지 확인
# print(re.match("[0-9]+","12a34"))
# print(re.match("[0-9]+","a1234"))

# print(re.search("^hi", "hello, hi")) # 여기서 ^는 ^()로 시작을 해야 함 (시작하지 않으므로 none
# print(re.search("hi", "hello, hi"))
# print(re.match("hi", "hello, hi"))
# print(re.match("hi|hello|good", "hello, hi"))
# print(re.match("hi|hello|good", "goodhello, hi"))
# print(re.match("[0-9]","12a34"))
# print(re.match("[0-9]*","12a34"))#숫자가 0개 이상 있는지 판단
# print(re.match("[0-9]+","12a34"))#숫자가 1개 이상 있는지 판단
# print(re.match("[0-9]*","a12a34"))#숫자가 0개 이상 있는지 판단
# print(re.match("[0-9]+","a12a34"))#숫자가 1개 이상 있는지 판단
#
#
# print(re.match("[a-z]*","12a34")) #알파벳 문자가 0개 이상 있는지 판단
# print(re.match("[a-z]+","12a34"))
# print(re.match("[a-z]*","aabb12a34")) #알파벳 문자가 0개 이상 있는지 판단
# print(re.match("[a-z]+","aabb12a34"))
#
# print(re.match("ab","abc"))
# print(re.match("ba","abacba"))
#
# print(re.search("ab","abc"))
# print(re.search("ba","abcba"))

# print(re.match("a*","b"))   # *은 *앞에 있는 문자가 0개 이상 나왔을 때 매치
# print(re.match("a+","b"))
# print(re.match("b*","b"))
# print(re.match("a*b","b")) # a문자가 0개 이상 있고 b가 나오면 매치
# print(re.match("a*b","bb"))

print(re.match("a+b","b"))  #a문자가 1개 이상 나와야하고 반드시 b가 그 뒤로 나와야 함
print(re.match("a+b","ab"))
print(re.match("a+b","aaabb")) # aaab까지만 매치
print(re.match("a+b","aaaaaaaaabbbbbb")) #aaaaaaaaab까지만 매치
print(re.match("a+b+","aaaaaaaaabbbbbb")) #aaaaaaaaabbbbbb까지 매치

print(re.match("[a-z]+","aaaa1aaaaasdfewaqrfzxvxzcvabbbbbb"))