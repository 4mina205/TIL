
######################################################################################
######################################################################################

# def seperate1(text):
#     import re
#     print(("".join(re.findall("\d",text))))
#     print(("".join(re.findall("\D",text))))
# seperate1("c910m6ia 1ho")
#
#
def seperate2(text):
    num=str()
    for i in list(text):
        if i in list(map(str,range(10))):
            num+=i
            text=text.replace(i,"")
    print(num)
    print(text)
seperate2("c910m6ia 1ho")


######################################################################################
######################################################################################

# def ivscom(me):
#     import random as r
#     rsp=['가위','바위','보']
#     computer=r.choice(rsp)
#     if me==computer:
#         print("비겼습니다.")
#     elif rsp.index(me)-rsp.index(computer) in [1, -2]:
#         print("이겼습니다.")
#     else:
#         print("아쉽...")
# ivscom("가위")

######################################################################################
######################################################################################

# def golotto():
#     import random as r
#     a=int(input("진행 회차 입력"))
#     lottopot=range(1,46)
#     outset=["꽝", "꽝", "꽝", "4등", "3등", "2등", "1등"]
#     result=[]
#     for j in range(1,a+1):
#         lucknum=r.sample(lottopot,6)
#         print("# {}회차".format(j))
#         for i in range(int(input("구매 개수 입력"))):
#             if i==0:
#                 print("이번주 당첨번호 :",lucknum)
#             yournum=r.sample(lottopot,6)
#             correct=len(list(set(lucknum) & set(yournum)))
#             result.append(outset[correct])
#             print("{}.{} ==> {}개 일치 {}".format(i+1,yournum,correct,outset[correct]))
#         print("="*40)
#     print("전체 결과")
#     for i in ["1등","2등","3등","4등","꽝"]:
#         print(i,result.count(i),"개")
# golotto()


######################################################################################
######################################################################################

# def daebak():
#     import random as r
#     lottopot=range(1,46)
#     outset=["꽝", "꽝", "꽝", "5등", "4등", "3등", "1등"]
#     result=list()
#     a = int(input("진행 회차 입력"))
#     for j in range(a):
#         allnum=r.sample(lottopot,7)
#         lucknum=allnum[:6]
#         bonus=allnum[-1]
#         print("# {}회차".format(j+1))
#         for i in range(int(input("구매 개수 입력"))):
#             if i==0:
#                 print("이번주 당첨번호 : {}+[{}]".format(lucknum,bonus))
#             yournum=r.sample(lottopot,6)
#             correct=len(list(set(lucknum) & set(yournum)))
#             if correct==5 and bonus in yournum:
#                 result.append("2등")
#                 print("{}.{} ==> {}개 + 보너스 일치 2등".format(i+1,yournum,correct))
#             else:
#                 result.append(outset[correct])
#                 print("{}.{} ==> {}개 일치 {}".format(i+1,yournum,correct,outset[correct]))
#         print("="*40)
#     print("전체 결과")
#     for i in ["1등","2등","3등","4등", "5등", "꽝"]:
#         print(i,result.count(i),"개")
# daebak()




# def daebak():
#     import random as r
#     lottopot=range(1,46)
#     outset=["꽝","꽝", "꽝", "꽝", "4등", "3등", "1등"]  #나중에 결과 출력할 때 사용 2등은 따로 판별
#     result=list()                                          #전체 결과 합산을 위한 빈 리스트
#     a = int(input("진행 회차 입력"))
#     for j in range(a):              #회차 돌리기 위한 for문
#         allnum=r.sample(lottopot,7) #보너스 포함 7개 뽑기
#         mainnum=allnum[:6]             #앞에 6개는 메인
#         bonus=allnum[-1]            #뒤에 1개는 보너스
#         print("# {}회차".format(j+1))
#         for i in range(int(input("구매 개수 입력"))):     #회차당 구매 개수를 위한 for문
#             if i==0:                                    #각 회차의 첫 번째 줄에는 당첨번호 출력
#                 print("이번주 당첨번호 : {}+[{}]".format(mainnum,bonus))
#             yournum=r.sample(lottopot,6)
#             correct=len(list(set(mainnum) & set(yournum))) #메인번호와 내번호의 교집합 개수
#             if correct==5 and bonus in yournum:         #맞은 개수가 5개라면 보너스 번호로 2등 선별
#                 result.append("2등")
#                 print("{}.{} ==> {}개 + 보너스 일치 2등".format(i+1,yournum,correct))
#             else:
#                 result.append(outset[correct])    #맞은 개수에 해당하는 결과를 전체 결과 리스트에 저장
#                 print("{}.{} ==> {}개 일치 {}".format(i+1,yournum,correct,outset[correct]))
#         print("="*40)
#     print("전체 결과")
#     for i in ["1등","2등","3등","4등","꽝"]:
#         print(i,result.count(i),"개")
# daebak()



# def golotto():
#     import random as r
#     a=int(input("진행 회차 입력"))
#     lottopot=range(1,46)
#     outset=["꽝", "꽝", "꽝", "4등", "3등", "2등", "1등"]       #나중에 결과 출력할 때 사용
#     result=[]                                                #전체 결과 합산을 위한 빈 리스트
#     for j in range(1,a+1):                                   #회차 돌리기 위한 for문
#         lucknum=r.sample(lottopot,6)                         #해당 회차의 당첨번호
#         print("# {}회차".format(j))
#         for i in range(int(input("구매 개수 입력"))):          #로또 구매 개수를 위한 for문
#             if i==0:                                         #각 회차의 첫 번째 줄에는 당첨번호 출력
#                 print("이번주 당첨번호 :",lucknum)
#             yournum=r.sample(lottopot,6)
#             correct=len(list(set(lucknum) & set(yournum)))   #당첨번호와 추첨번호의 교집합 개수
#             result.append(outset[correct])           #맞은 개수에 해당하는 결과를 전체 결과 리스트에 저장
#             print("{}.{} ==> {}개 일치 {}".format(i+1,yournum,correct,outset[correct]))
#         print("="*40)
#     print("전체 결과")
#     for i in ["1등","2등","3등","4등","꽝"]:
#         print(i,result.count(i),"개")
# golotto()










# import random
# def game(y):
#     pc = random.choice(["가위", "바위", "보"])
#     if y == pc:
#         res = "비겼습니다 한번더?"
#     elif (y == "가위" and pc == "보") or (y=="바위" and pc=="가위") or (y=="보" and pc=="바위"):
#         res = "이겼습니다 가위바위보에 소질이 있으시네요!"
#     else:
#         res = "안타깝네요 게임에서 패배하셨습니다"
#     return res
#
#
# prompt = """
# 1. 게임을 시작합니다
# 2. 게임을 종료합니다"""
# num = 0
# while num != 2:
#     print(prompt)
#     num = int(input())
#     if num == 1:
#         y = input("가위, 바위, 보 중 어떤 것을 내시겠습니까? : ")
#         print(game(y))
# print("게임이 종료되었습니다")
