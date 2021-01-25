def jeongryeol(text):
    import re
    b=re.findall("-[\d]",text)
    c=re.findall("\s[\d]",text)
    print((" ".join(b))+("".join(c)))

jeongryeol('-1 1 3 -2 2')
#
#
# def getpage():
#     import math
#     m,n=map(int,input().split())
#     print(math.ceil(m/n))
#
# getpage()



# def liro(a):
#     a=list(a.split())
#     n=int(a[0])
#     text=a[1:]
#     print(' '.join(text[-n:]+text[:-n]))
# liro('0 똘기 떵이 호치 새초미')