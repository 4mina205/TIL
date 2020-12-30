# for a in range(1,51):                    # for in range
#     if (a % 10 == 0):                    # a 가 10의 배수으면
#         print("+", end="")               # + 출력하고 붙이고
#     else:                                # 아니면
#         print("-", end="")               # - 출력하고 붙여

# ---------+---------+---------+---------+---------+

for a in range(1,51):                    # for in range
    if (a % 10):                         # a 가 10의 배수으면
        print("-", end="")               # + 출력하고 붙이고
    else:                                # 아니면
        print("+", end="")               # - 출력하고 붙여
print(2%10)