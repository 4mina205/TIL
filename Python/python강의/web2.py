# \d : 숫자([0-9])dh krkxdma
# \D : not \d의미, [^0-9]와 같음
#
# \s : 공백문자, 탭문자, 엔터문자 등
# \S : not 공백문자, 탭문자, 엔터문자 의미
#
# \w : 문자 + 숫자를 의미, [a-zA-Z_]와 같음
# \W : not 문자 + 숫자를 의미, [^a-zA-Z0-9_]어ㅣ같음
# #
# ? 또는 . : 문자가 1개만 있는지 판단
# ?는 문자가 0개 또는 1개인지 판단
# .은 문자가 1개인지 판단
# ab?c --> a + b가 있어도 없어도 됨 + c
import re
# print(re.match('h?','h'))
# print(re.match('h?','he'))
# print(re.match('h?','his'))
# print(re.match('h.','hello'))
#
# print(re.match('ab?c','abc'))
# print(re.match('ab?c','ac'))
# print(re.match('ab?c','abbc'))
#
# print(re.match('a.b','abb'))
# print(re.match('a[.]b','abb'))
# print("***************************")
# print(re.match("[123]","3"))
# print(re.match("[123]","32"))
# print(re.match("[123]","32321"))
# print(re.match("[123]+","32321"))
# print(re.match("[123]+","3232341"))
# print(re.match("[123]+","3232142"))
# print(re.match("[1-7]+","3232142"))
# print(re.match("\d+","3232142"))
#
# print("***************************"*3)
#
# print(re.match('a.b','abb'))
# print(re.match('a[.]b','abb')) # 대괄호 안에있는 문자가 반드시 나와야함
#
# print(re.match("do*g","dog"))
# print(re.match("do*g","dooog"))
# print(re.match("do*g","dooooooooog"))
# print(re.match("do*g","doooookg"))
#
# # 반복
# # {최소, 최대} : 최소 횟수 이상, 최대 횟수 이하 반복
# # {최소,} : 최소 횟수 이상 반복
# # {, 최대} : 최대 횟수 이하 반복
# # {숫자} : 숫자 만큼 반드시 반복
# print("*"*59)
# print(re.match("do{2}g","dog"))   #o문자가 반드시 2번 반복
# print(re.match("do{2}g","doog"))    #o문자가 반드시 2번 반복
print(re.match("do{2}g","doooooooooog"))    #o문자가 너무 많이 반복
# print(re.match("do{2,5}g","dog"))  #o문자가 2번 이상 5번 이하 반복
# print(re.match("do{2,5}g","doog"))   #o문자가 2번 이상 5번 이하 반복
# print(re.match("do{2,5}g","doooooooooog"))   #o문자가 너무 많이 반복
#
# print("*"*59)
# print(re.match("do{2,}g","dog"))   #o문자가 반드시 2번 반복
# print(re.match("do{,2}g","doog"))    #o문자가 반드시 2번 반복
# print(re.match("do{,2}g","doooooooooog"))    #o문자가 너무 많이 반복
#
# #휴대폰 전화번호
# # 010-5512-2624
# print(re.match("[0-9]{3}[-][0-9]{4}[-][0-9]{4}","010-1234-5678"))
#
# print(" "*50)
# print(" "*50)
# print(" "*50)
# print(" "*50)
# print(" "*50)
# print(" "*50)
# print(" "*50)
# print(" "*50)
#
# print(re.match("[a-z]+","python"))
# #위는 아래와 같다
# pat = re.compile("[a-z]+") #정의한 패턴을 pat에 저장
# res = pat.match("python")
# print(res)#패턴객체가 가지고 있는 match함수를 이용하여 주어진 문자열이 패턴에 매치되는지 확인
#
#
#
# print(" "*50)
# print(" "*50)
# print(" "*50)
# print(" "*50)
# print(" "*50)
# print(" "*50)
# print(" "*50)
#
# print(re.match("[a-z]+","python"))
# print(re.search("[a-z]+","python"))
#
# print(re.match("[a-z]+","7python"))
# print(re.search("[a-z]+","7python"))  #내가 원하는 키워드가 있는지 찾는 느낌? #search 결과는 1개으 ㅣ매치 객체가 리턴
#
# print(re.findall("[a-z]+","7python8java8cpp"))
# pat = re.compile("[a-z]+") #정의한 패턴을 pat에 저장
# res = pat.findall("7python8java8cpp")
# print(res)

# print(re.finditer("[a-z]+","7python8java8cpp"))
# pat = re.compile("[a-z]+") #정의한 패턴을 pat에 저장
# res = re.finditer("[a-z]+","7python8java8cpp")
# for i in res:
    # print(i)
    # print(i.start())
    # print(i.end())
    # print(i.group())
    # print(i.span())
# print(res)

# print(re.match("a.b","a0b"))


# pat = re.compile("a.b", re.DOTALL) # 역슬래시를 포함 하겠다!
# print(pat.match("a\nb"))

# pat=re.compile("[a-z]")
# print(pat.match("python"))
# pat=re.compile("[a-z]")
# pat=re.compile("[a-z]",re.I) #I=ignorecase(대문자인지 소문자인지 무시하겠다)
# print(pat.match("Python"))
#
# pat=re.compile("[a-z]",re.I) #I=ignorecase(대문자인지 소문자인지 무시하겠다)

# print(re.search("\\sec", "asdfkdgjsdf/sec sadfasdf"))
# print(re.search(r"\\sec", "asdfkdgjsdf\sec sadfasdf"))




# print(re.match("ab[0-9]?c","abc"))
# # print(re.match("ab[0-9]?c","ab9c"))
# # print(re.match("ab.c","ab9c"))
# # print(re.match("h{3}","hhhiiiii"))
# # print(re.match("(hi){3,5}","hihihihelloworld"))
# # print(re.match("[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}","02-555-7777"))
# # print(re.findall("[ㄱ-ㅎ가-힣]+","ㅋ캬캬ㅋsdfㅋㅋㅋㅋㅋㅋㅋㅋ123ㅋㅋㅋㅋㅋㅋㅋㅋ"))
# print(re.findall("[^ㄱ-ㅎ가-힣]+","ㅋ캬캬ㅋsdfㅋㅋㅋㅋㅋㅋㅋㅋ123ㅋㅋㅋㅋㅋㅋㅋㅋ"))

news="""
(서울=연합뉴스) 신선미 기자 = 국내 신종 코로나바이러스 감염증(코로나19) '3차 대유행'이 완만한 감소세로 접어든 가운데 이번 주 신규 확진자 발생 추이가 주목된다.

신규 확진자 감소세 지속이냐 재확산이냐의 흐름을 가늠해 볼 수 있기 때문이다.

지난달 말까지만 해도 연일 1천명 안팎으로 발생하던 신규 확진자는 새해 들어 600명대로 줄었다가 11일 400명대 중반까지 더 떨어진 뒤 12일에는 500명대로 소폭 증가한 상태다.

큰 틀의 통계만 보면 확실한 감소 내지 안정국면으로 접어드는 것 아니냐는 관측이 나온다.

하지만 신규 확진자가 400명∼500명대까지 낮아진 데는 주말과 휴일 검사건수 감소 영향도 있어 아직 상황을 낙관하기에는 이르다는 게 감염병 전문가들의 공통된 의견이다.

방역당국 역시 긴장의 끈을 풀기에는 위험 요인이 너무 많다며 국민 개개인의 지속적인 방역 협조를 당부하고 있다.
"""
#
# print(re.findall("[ㄱ-ㅎ가-힣]+",news))
# print(re.findall("[ㄱ-ㅎ가-힣]+[0-9]+",news))
# print(re.findall("[0-9]+[ㄱ-ㅎ가-힣]+",news))

# print(re.match("[^A-Z]+","Hello"))
# print(re.match("[^A-Z]+","hello"))
# print(re.match("[0-9]+"," hello119"))
# print(re.match("[0-9]+"," hello119"))
#
# print(re.search("[0-9]+$"," hello119"))


# print(re.search("[*]","3*5"))
# print(re.search("[*]+","3**5"))
#
# print(re.search("\*","3*5"))
# print(re.search("\*+","3**5"))


# print(re.search("\$\([a-z]+\)","$(document)"))
# print(re.search("[$(a-z)]+","$(document)"))



#"asdasdasd ok"# 라는 문자열이 있을 때 asd가 있는지 조사
# s=asd
# print(re.search("(asd)+","asdasdasd ok"))
# print(re.search("\w+\s+\d+[-]\d+[-]\d+","kim 010-1234-5867"))


# res=re.search("(\w+)\s+\d+[-]\d+[-]\d+","kim 010-1234-5867")
# print(res.group())
# print(res.group().split()[1])
# print(res.group(1))


res=re.search("(?P<name>\w+)\s+(?P<num>\d+[-]\d+[-]\d+)","kim 010-1234-5867") #작성형식 : (?P<그룹명>)
print(res.group('num'))








































