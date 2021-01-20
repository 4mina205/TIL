# with open("inandout.txt","r") as f:
#     a=f.read()
# inout=a.split("\n")
# inout=[a[i].split() for i in range(len(inout))]
# num=0
# time=input()
# for i in range(len(inout)):
#     inout[i].append(time)
#     inout[i].sort(key=lambda x:x)
#     if inout[i][1]==str(time):
#         num+=1
# print(num)

#########################################################
#
def readtext(worklist):
    with open(worklist,"r") as f:
        a = f.read()
    a = a.split("\n")
    people = len(a)
    inout = [a[i].split() for i in range(people)]
    return inout

def workman(worklist,nowtime):
    a=readtext(worklist)
    b=len(a)
    num=0
    for i in range(b):
        a[i].append(nowtime)
        a[i].sort()
        if a[i][1]==str(nowtime):
            num+=1
    print(num)

workman("inandout.txt","09:00:00")


def readtext(worklist):
    with open(worklist,"r") as f:
        a = f.read()
    a = a.split("\n")
    people = len(a)
    inout = [a[i].split() for i in range(people)]
    return inout

def workman(worklist,nowtime):
    a=readtext(worklist)
    num=0
    for i in a:
        if i[0]<=str(nowtime) and str(nowtime)<=i[1]:
            num+=1
    print(num)

workman("inandout.txt","09:12:23")