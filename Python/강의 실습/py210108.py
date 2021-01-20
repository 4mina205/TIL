# ###################   all 함수  ###################
# print(all([1,2,3])) #모두 참이어야 참(모든 숫자에 0이 없으므로 참)
# print(all([1,2,3,0])) #0이 포함되어 있으므로 거짓
#
# ###################   any 함수  ###################
# print(any([1,2,3]))     #참이 하나라도 있으면 참
# print(any([1,2,3,0]))   # 0이 있어도 참 값이 있기 때문에 참 출력
#
# ###################   chr 함수  ###################
# # print(chr('A'))
#
# ###################   enumerate 함수  ###################
# # for문에 index를 나타내고 싶다?
# for idx, i in enumerate(['aaa','bbb','ccc']):
#     print(i)
#
#
# ###################   eval 함수  ###################
# print("10+20")
# print(type("10+20"))
# print(eval("10+20"))
# print(type(eval("10+20")))


###################   filter 함수  ###################
# def pos():
#     res=[]
#     for i in a:
#         if i>0:
#             res.append(i)
#     return res
# print(pos([1,3,-5]))
# #     filter(x>0, pluslist )
# #     print(pos([1,3,-5,-7,9])) # 1,3,9
# # print(type(-1))
# def pos2(a):
#     return a>0
# print(list(filter(pos2,[1,3,-5,-7])))



# ###################   filter 함수 + 람다 함수  ###################
# print(list(filter(lambda a:a>0, [1,3,-5,-7,9])))
#
#
#
# ###################   정수 표현  ###################
# print(int('3'))
# print(float('3.4'))
# print(int('ea',16))

###################   리스트 내포(컴프리헨션)  ###################
# num=[]
# for n in range(11):
#     num.append(n)
# print(num)
#
# print([n*2 for n in range(11)])


###################   1~10까지 짝수만 저장  ###################
# evenNum=[]
# for i in range(11):
#     if i%2==0:
#         evenNum.append(i)
# print(evenNum)
#
#
# eb=[i for i in range(1,11) if i%2==0]
# print(eb)

# menu=["쌈밥", "치킨", "피자"]
# dessert=["사과","아이스크림","커피"]
# comb_menu_des=[]
# for i in ["쌈밥", "치킨", "피자"]:
# print([(x,y) for x in ["쌈밥", "치킨", "피자"] for y in ["사과","아이스크림","커피"]])



###################   0~9까지 수 중에서 5보다 작으면서 2로 나누어 떨어지는 수를 리스트에 저장하시오[0,2,4]  ###################

# print([x for x in range(10) if x <5 if x%2==0])
# print({x+y:"값" for x in range(10) for y in range(10)})


###################   scores  ###################
# scores={'철수':50, "영희":70, "순신":123}
# # print({name:score for name, score in scores.items() if name != '순신'})
# #
# print({name:"pass" if score>=60 else "fail" for name, score in scores.items()})
#
# ## 점수가 60 이상이면 pass, 미만이면 fail
#
# #################   리스트 컴프리헨션  ###################
# words=['Computer','Coke','Bread']
# print([x.lower() for x in words])
#
# #################   리스트 컴프리헨션  ###################
# a=[1,-5,4,2,-2,10]
# print([x if x>0 else 0 for x in a])


#################   리스트 컴프리헨션  ###################
# a=[1,2,3,4,5]
# for i in a:
#     if i==1:
#         print("pass")
#     elif i==2:
#         print("fail")
#     else:
#         print("no")
#
# print(["pass" if i==1 else "fail" if i==2 else "no" for i in a])

#################   딕셔너리 응용  ###################
# x={'a':10, 'b':20, 'c':30}
# print(x)
# x['aa']=40
# print(x)
# x.setdefault('d')
# print(x)
#
# x['a']=100
# print(x)
# x.update(b=200)
# print(x)
#
# x['z']=99
# print(x)
#
# x.update(c=300) # 기존에 키가 존재하면 키를 업데이트, 없으면 추가
# print(x)
#
# x.update(c=300, s=50) # 한번에 추가 가능
# print(x)
#
#
# a=[12,23]
# print(a)
# bb=[555,777,999]
# a.append((bb[0],bb[1]))
# print(a)
# x.update(zip(['aa','c'],[99999,77777]))
# print(x)

###############   딕셔너리 팝  ###################


# x={'a':10,'b':20,'c':30,'d':40}
# v=x.pop('a')
# print(v)
#
# x={'a':10,'b':20,'c':30,'d':40}
# del x['b']
# print(x)

#
# x={'a':10,'b':20,'c':30,'d':40}


# ###############   리스트(튜플) -> 딕셔너리  ###################
# li=['a','b','c']
# d=dict.fromkeys(li)
# print(d)
#
# d2=dict.fromkeys(li,10)
# print(d2)


from collections import defaultdict # collections모듈에서 defaultdict 함수 가져옴
# d2=defaultdict(int)
# print(d2['z'])
#
# print(d3.items())
# print(d3.keys())
# print(d3.values())
#
#
# d3={'a':10,'b':20}
# for k in d3.keys():
#     print(k)
# for k,v in d3.items():
#     print(k,v)
#
# keys=['a','b','c','d']
# for key, value in dict.fromkeys(keys).items():
#     print(key, value)
#
# d4={key:value for key, value in dict.fromkeys(keys).items()}
# print(d4)


###############   예제  ###################
#newx는 x에 저장된 데이터에서 'b'를 뺀 나머지를 저장하고 싶음
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# newx.pop('b')
# print(x)

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# newx={k:v for k,v in x.items() if k !='b'}
# print(newx)
#
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# newx={k:v for k,v in x.items() if v !=20}
# print(newx)


# x={'BTS':{'머큐리':4.5,'매트릭스':4.0},"소녀시대":{'머큐리':3.5,'매트릭스':3.0}}
# x['BTS']['매트릭스']=5
# print(x['BTS']['매트릭스'])



# x={'a':0,'b':1}
# y=x
# print(x)
#
# x['a']=2
# y=x.copy()
# print(x is y)

##################################################################
################         중첩 딕셔너       리#######################
##################################################################
# x={'a':{'python':'3.8'}, 'b':{'python':'2.7'}}
# y=x.copy()
# y['a']['python']='2.7777'
# print(y) # {'a': {'python': '2.7777'}, 'b': {'python': '2.7'}}
# print(x) # {'a': {'python': '2.7777'}, 'b': {'python': '2.7'}} # 원래 안바뀌어야 하는데 같이 바뀜 # 중첩 딕셔너리에서는 copy메서드 대신 copy모듈의 deepcopy 함수를 사용
#
#
# x={'a':{'python':'3.8'}, 'b':{'python':'2.7'}}
# import copy
# y=copy.deepcopy(x)
# y['a']['python']='2.78788'
# print(y) #{'a': {'python': '2.78788'}, 'b': {'python': '2.7'}}
# print(x) #{'a': {'python': '3.8'}, 'b': {'python': '2.7'}} # 안바뀜 --> 중첩 딕셔너리의 카피는 deepcopy함수를 사용해야한다.





##############################################################################################
#################                     연습문제                    #############################
##############################################################################################
# 1.
# 다음입사문제
# 1차원의 점들이 주어졌을 떄, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다)
# 예를들어 s={1,3,4,8,13,17,20}이 주어졌다면, 결과값은 (3,4)가 될 것이다.
######################################################
######################################################
# s={1,3,4,20,21}
# num=list(s)
# min1=[num[1]-num[0]]
# # print(min1)
# for i in range(1, len(num)-1):
#     if num[i]-num[i-1]<min(min1):
#         min1.append(num[i]-num[i-1])
#         print(min1)
#     print(num[i],num[i-1])
######################################################
######################################################


########### min 값 구하기 ###########
# s={1,3,4,20,21,25,28,56,100,101}          #김윤호님꺼 참고함(제일 작은 값이 한 쌍이 아니라면 어떡할 것인가?)
# num=list(s)       # len(num)=5            #김윤호님 감사합니다
# num.sort()                                #왠지는 모르겠지만 .sort 안하면 리스트 순서가 뒤바뀜...?
# minval=[]
# for i in range(len(num)-1):
#     minval.append(num[i+1]-num[i])        # 뺀 값들을 다 집어 넣자
# small=min(minval)                         # 그 중 가장 작은 값이 뭔지 구해보자
#
# ########### min 값과 비교하기 #########     # 이제부터 가장 작은 값과 비교할거임
# minpair=[]
# for i in range(len(num)-1):               # 다시 똑같은 for문...?
#     if num[i+1]-num[i]==small:            # 한 쌍의 차가 가장 작은값과 같을때
#         minpair.append((num[i],num[i+1])) # 그 쌍을 추가해라
# print(minpair)                            # 뽑아라
###############################################
###########   step.1 min 값 구하기  ############
###############################################
# s={1,3,4,20,21,25,28,56,100,101}          #김윤호님꺼 참고함(제일 작은 값이 한 쌍이 아니라면 어떡할 것인가?)
# num=list(s)                               #김윤호님 감사합니다
# num.sort()                                #왠지는 모르겠지만 .sort 안하면 리스트 순서가 뒤바뀜...?
# minval=[]
# minpair=[]
# for i in range(len(num)-1):
#     minval.append(num[i+1]-num[i])        # 뺀 값들을 리스트에 추가
#     small=min(minval)                         # 그 중 가장 작은 값
#     if num[i + 1] - num[i] == small:  # 한 쌍의 차가 가장 작은값과 같을 때
#         minpair.append((num[i], num[i + 1]))  # 그 쌍을 추가
# print(minpair)
#
#
# ###############################################
# ###########   step.2 min 값과 비교하기 #########     # 이제부터 가장 작은 값과 비교
# ###############################################
# minpair=[]
# for i in range(len(num)-1):               # 다시 똑같은 for문...?
#     if num[i+1]-num[i]==small:            # 한 쌍의 차가 가장 작은값과 같을 때
#         minpair.append((num[i],num[i+1])) # 그 쌍을 추가
# print(minpair)


s={1,3,4,20,21,25,28,56,100,101}          #김윤호님꺼 참고(거리가 가장 짧은 쌍이 한 쌍이 아니라면 어떡할 것인가?)
num=list(s)                               #김윤호님 감사합니다
num.sort()                                #왠지는 모르겠지만 .sort 안하면 리스트 순서가 뒤바뀜...?
minval=[]
minpair=[]
for i in range(len(num)-1):
    minval.append(num[i+1]-num[i])        # 뺀 값들을 리스트에 추가
small=min(minval)                         # 그 중 가장 작은 값
for j in range(len(num)-1):               # 다시 똑같은 for문...?
    if num[j+1]-num[j]==small:            # 한 쌍의 차가 가장 작은값과 같을 때
        minpair.append((num[j],num[j+1])) # 그 쌍을 추가
print(minpair)






# print(list(range(len(num)-1)))
# print(num[0],num[4])
# for i in range(1,len(num)):

#
#
#
# print(len(list(range(1,len(num1)))))
# for i in num:
#     for j in

# print(num[1],num[2])














#2.
# 회문(palindrome)은 순서를 거꾸로 해서 읽어도 제대로 읽을때와 같은 단어 or 문장
# ex) rotator, sos, "nurses run"공백을 빼고 읽으면 같음
# 문제는 임의의 단어(문장)을 입력받아 회문 여부를 출력
# true or false
# input_str=input("단어(문장) 입력하시오!") #단어문자입력
# del_blank=input_str.replace(" ","")    #공백제거
# list_input_str=list(del_blank)         #리스트로 변환
# rev_input_str=list_input_str.copy()    #리스트 복사
# list_input_str.reverse()               #복사한곳에 리스트 뒤집에서 저장
# if list_input_str==rev_input_str:      #같은지 다른지 비교
#     print("True")                      #같으면 true
# else:
#     print('False')                     #틀리면 false
# print(rev_input_str)
# print(list_input_str)

#############################################################################
# def palindrome(string):
#     del_blank=string.replace(" ","")
#     list_input_str = list(del_blank)
#     rev_input_str = list_input_str.copy()
#     list_input_str.reverse()
#     if list_input_str == rev_input_str:
#         print("True")
#     else:
#         print('False')
# palindrome("nurses run")
# #############################################################################
#
# def palindrome(string):
#     forstr=string.replace(" ","")
#     revstr=forstr[::-1]
#     if forstr == revstr:
#         print("True")
#     else:
#         print('False')
# palindrome("sos")
# palindrome("bigdata")
# palindrome("nurse run")


