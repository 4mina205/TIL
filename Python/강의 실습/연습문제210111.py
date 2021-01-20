# -*- coding: utf-8 -*-
#
# # 1. 문자열 바꾸기
# # # 다음과 같은 문자열이 있다.
# # # a:b:c:d
# # # 문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오.
# # # a#b#c#d
# str1 = "a:b:c:d"
# print(str1.replace(":","#"))
#
#
#
# # # 2. 리스트 총합 구하기
# # # 다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 60점 이상 점수의 평균을 구하시오.
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# all_num=0
# n=0
# for score in A:
#     if score>=60:
#         all_num+=score
#         n+=1
# print(all_num/n)
#
# # # 3. 평균값 구하기
# # # 다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후
# # # 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.
# with open("sample.txt","r") as a:
#     sample=a.read().split("\n")
# with open("result.txt","w") as f:
#     f.write(str(sum(list(map(int, sample))) / len(sample)))
#
#
# # 4. 모스 부호 해독
# # 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.
# # 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# # 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
# m= '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
# zzz=""
# mos=m.split(' ')
# code={".-":'A'      ,"-.":'N'   ,
#       "-...":'B'    ,"---":'O'  ,
#       "-.-.":'C'    ,".--.":'P' ,
#       "-..":'D'     ,"--.-":'Q' ,
#       ".":'E'       ,".-.":'R'  ,
#       "..-.":'F'    ,"...":'S'  ,
#       "--.":'G'     ,"-":'T'    ,
#       "....":'H'    ,"..-":'U'  ,
#       "..":'I'      ,"...-":'V' ,
#       ".---":'J'    ,".--":'W'  ,
#       "-.-":'K'     ,"-..-":'X' ,
#       ".-..":'L'    ,"-.--":'Y' ,
#       "--":'M'      ,"--..":'Z' ,
#       '':' '}
# for i in mos:
#     zzz+=code[i]
# print(zzz)
#


# eng = 'Right way to Python'
# print(eng.strip('goPniR'))

# 5. ngram

a = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다."
b = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다."
aset=[]
bset=[]
for i in range(len(a)-1):
    aset.append(a[i] + a[i + 1])
aset=set(aset)
for j in range(len(b) - 1):
    bset.append(b[j] + b[j + 1])
bset=set(bset)
if len(aset) >= len(bset):
    print(100-(len(aset-bset) / len(aset)) * 100, "%", sep='')
else:
    print(100-(len(bset-aset) / len(bset)) * 100, "%", sep='')








