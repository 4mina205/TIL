# def plnum(a):
#     import math
#     a=a+2
#     d=math.ceil(a/6)
#     b=0
#     c=0
#     while c<d:
#         b += 1
#         c += b
#     print(b+1)
#     # return (b)
#
# plnum(61)
#


# def plnum(a):
#     import math
#     a=a-2
#     d=math.ceil(a/6)
#     b=0
#     c=0
#     while True:
#         if c>d:
#             break
#         else:
#             b += 1
#             c += b
#     print(b+1)
#     return (b)
#
# plnum(70)



def samgak(a):
    if len(a)==3 and sum(a)==180 and 0 not in a:
        if max(a)>90:
            print("둔각삼각형")
        elif max(a)==90:
            print("직각삼각형")
        else:
            print("예각삼각형")
    else:
        print("삼각형 아님")

a=[30,80,70]
samgak(a)

#####################################


# def gwalho(gwalhodle):
#     print(gwalhodle.count("("))
#     if gwalhodle[0] != ")" and gwalhodle[-1] != "(":
#         if gwalhodle.count("(")==gwalhodle.count(")"):
#             print("정상")
#     else:
#         print("비정상")
# gwalho("(()")

#
# def gwalho(a):
#     print(a.count("("))
#     if a[0]=="(" and a[-1]==")" and a.count("(")==a.count(")"):
#         print("정상")
#     else:
#         print("비정상")
# gwalho("(())")