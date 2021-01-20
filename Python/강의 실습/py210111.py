# ########### 맵함수 활용 ###########
# def twoTimes(n):
#     return n*2
# res=list(map(twoTimes, [1,2,3]))
# print(res)
# # [2, 4, 6]

# ########### pow함수 활용 ###########
# print(pow(3,2))
# #9

########### round함수 활용 ###########
# print(round(3.141592,4))
# #3.1416

# ########### zip함수 활용 ###########
# print(list(zip([1,2],[3,4],[5,6],[7,8])))
# #[(1, 3, 5, 7), (2, 4, 6, 8)]

# ########### filter함수 활용 ###########
# t=list(range(1,11))
# print(t)
# def isEven(n):
#     return True if n%2==0 else False
# res=[]
# for v in t:
#     if isEven(v):
#         res.append(v)
# print(res)
# print(list(filter(isEven,t)))
# print(list(filter(lambda x: x%2==0, t)))


# ########### os 모듈 ###########
# import os
# print(os.environ) #내pc 환경(사용일 거의 x)
# print(os.getcwd()) #현재 작업 경로 확인
# os.mkdir("sample") #현재 작업 위치에 폴더 생성
# os.rmdir("sample") #폴더 제거
# os.rmdir("sample") #폴더 제거
# os.rename("sample","test") # 폴더명 변경


# import shutil
# shutil.copy("hi.txt", "hicopy.txt")

import glob
print(glob.glob("C:/Users/SAMSUNG/PycharmProjects/*"))







