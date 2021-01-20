area=set()
for i in range(4):
    sq=list(map(int, input().split()))
    for x in range(sq[0],sq[2]):
        for y in range(sq[1],sq[3]):
            area.add((x,y))
print(len(area))
#
# #1 2 4 4 2 3 5 7 3 1 6 5 7 3 8 6
#
#
#
#
# print(lambda x,y : , [3,5,7,8])
#
#
# area=set()
# for i in range(4):
#     sq=list(map(int, input().split()))
#     area.add(lambda )
#
#
#     for x in range(sq[0],sq[2]):
#         for y in range(sq[1],sq[3]):
#             area.add((x,y))
# print(len(area))

sq=[1, 2, 4, 4]
# [2, 3, 5, 7]
# [3, 1, 6, 5]
# [7, 3, 8, 6]


qq=[3,5,7,8]
aa=[]
a=list(map(lambda x, y: (x for x in range(4) y for y in range(5)),qq))
print(a)
