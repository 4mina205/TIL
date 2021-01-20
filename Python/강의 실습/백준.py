


def connum(text):
    import re
    for i in list(set(text)):
        if len(re.findall("[{0}]+".format(i), text)) == 1:
            continue
        else:
            return False
    return True
print(connum("aba"))

a=int(input())
c=0
for x in range(a):
    text=input()
    if connum(text):
        c+=1
print(c)

