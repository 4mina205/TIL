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


# def gorotto():
#     a=int(input("몇 회차 까지 진행하시겠습니까?"))
#     import random as r
#     rottopot=range(1,46)
#     resset=["꽝", "꽝", "꽝", "4등", "3등", "2등", "1등"]
#     perfect=[]
#     for j in range(1,a+1):
#         lucknum=r.sample(rottopot,6)
#         print("#",j," 회차",sep="")
#         for i in range(int(input("로또를 몇개 구매하시겠습니까?"))):
#             if i==0:
#                 print("이번주 당첨번호 :",lucknum)
#             yournum=r.sample(rottopot,6)
#             good=len(list(set(lucknum) & set(yournum)))
#             perfect.append(resset[good])
#             print("추첨번호는",yournum,"입니다.",good,"개 일치",resset[good])
#         print("="*10)
#     print("전체 결과")
#     for i in ["1등","2등","3등","4등","꽝"]:
#         print(i,perfect.count(i),"개")
# gorotto()



# def seperate1(text):
#     import re
#     print(("".join(re.findall("\d",text))))
#     print(("".join(re.findall("\D",text))))
# seperate1("c910m6ia 1ho")
#
#
# def seperate2(text):
#     num=str()
#     for i in list(text):
#         if i in list(map(str,range(10))):
#             num+=i
#             text=text.replace(i,"")
#     print(num)
#     print(text)
# seperate2("c910m6ia 1ho")


#
#
def golotto():
    import random as r
    a=int(input("진행 회차 입력"))
    lottopot=range(1,46)
    outset=["꽝", "꽝", "꽝", "4등", "3등", "2등", "1등"]
    result=[]
    for j in range(1,a+1):
        lucknum=r.sample(lottopot,6)
        print("# {}회차".format(j))
        for i in range(int(input("구매 개수 입력"))):
            # if i==0:
            #     print("이번주 당첨번호 :",lucknum)
            yournum=r.sample(lottopot,6)
            correct=len(list(set(lucknum) & set(yournum)))
            result.append(outset[correct])
        #     print("{}.{} ==> {}개 일치 {}".format(i+1,yournum,correct,outset[correct]))
        # print("="*40)
    print("전체 결과")
    for i in ["1등","2등","3등","4등","꽝"]:
        print(i,result.count(i),"개")
golotto()
















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
