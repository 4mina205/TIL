n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    z=divmod(c,a)
    if z[1] == 0:
        print(((z[1] + 1) * 100) + a)
    else:
        print(((z[1]) * 100) + (z[0] + 1))



# a=1
# c=5
# z=divmod(c,a)
# if z[1]==0:
#     print(((z[1]+1) * 100) + (z[0]))
# else:
#     print(((z[1]) * 100) + (z[0] + 1))
#
# # print(((z[1]) * 100) + (z[0] + 1))

