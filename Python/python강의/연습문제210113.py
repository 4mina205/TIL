# 1. IT기업 코딩 테스트문제
# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.
# (1)김씨와 이씨는 각각 몇 명 인가요?
names="이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서," \
      "박민호,전경헌,송정환,김재성,이유덕,전경헌"
namelist=names.split(",")

# (1-1)
print("김씨 :", sum([y[0]=="김" for y in namelist]), "이씨 :", sum([y[0]=="이" for y in namelist]))


# (1-2)
numK=0
numL=0
for i in namelist:
    if i[0]=="김":
        numK+=1
    elif i[0]=="이":
        numL+=1
print("김씨 :", numK, "이씨 :",numL)


# (2)"이재영"이란 이름이 몇 번 반복되나요?
print("이재영 :",sum([i=="이재영" for i in namelist]))


# (3)중복을 제거한 이름을 출력하세요.
nameset=set(namelist)
namelist=list(nameset)
print(",".join(namelist))


# (4)중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
print(sorted(namelist))





# 2. 토지 원고 데이터
from bs4 import BeautifulSoup
import re
toji = open('toji.txt',encoding='utf-16').read()
soup=BeautifulSoup(toji, "html.parser")

# 1) 저자명 추출
print("저자 :",soup.find("author").string)

# 2) 제목 추출
print("제목 :",soup.find("title").string)

# 3) 출판사명 추출
print("출판사 :",soup.find("publisher").string)

# 4) 인용부호(큰 따옴표)로 묶여있는 내용을 모두 추출하여 리스트에 저장
story=str(soup.find("body"))
dquo_list=re.findall('".+"',story)
print(dquo_list)

# 5) 토지 원고 전체에서 한글에 해당되는 내용만 추출하여 저장, 가장 많이 사용된 단어
all_text=re.findall("[가-힣]+",str(soup.find_all("p")))
voc_dict={}
for i in all_text:
    if i in voc_dict:
        voc_dict[i] = voc_dict[i]+1
    else:
        voc_dict[i] = 1
pair=sorted(voc_dict.items(), key=lambda x: x[1], reverse=True)
for i in range(101):
    print(pair[i])

# mostpair=sorted(voc_dict.items(), key=lambda x: x[1], reverse=True)
# for i in range(101):
#     print(mostpair[i])


# 6) 각 장의 제목 저장 및 출력
head=soup.find_all("head")
for i in head:
    print(i.string)

