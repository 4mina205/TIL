# t1=(1,2,3)
# # print(t1)
# # print(type(t1))
# # del t1[1]
#
# print(t1[2])   # 인덱싱
#
# print(t1[1:]) # 슬라이싱
#
# t2=('a',3,4)      # 덧셈 가능
# print(t1+t2)
#
# t3=(5,6)          #곱셈도 가능
# # print(t3*5)
#
# person=('kim',20,60.5,True)
# print(person)

# t4=(7,)
# print(type(t4))



#
# x=(tuple(range(5,20)))
# print(list(x))
#
# tempx=list(x)
# print(tempx)
# tempx[4]=50
# print(tempx)

# y=[1,2,3]
# tempy=tuple(y)
# print(type(tempy))

# s="hello"
# print(list(s))
# print(tuple(s))
#



#
# a,b,c=1,2,3
# print(a)
# print(type(a))
#
# k=(1,2,3)
# a,b,c=k
# print(a)
# print(type(a))

#
# a=list(range(0,91,10))
# print(a)
# print( 30 in a)
# print(45 in a)
#
#
# print("5가 있나요?", 5 in a)


# a=[1,2]
# b=[3,4]
# print(a+b)

# print(range(0,3)+range(3,6))   # 에러 레인지 객체들을 연결할 수 없으므로, range를 list로  변경한 다음 연결

# print(list(range(0,4))+list(range(4,6)))
# print("hi"+"hello")

#
#
# print("hi"+str(100))
#
#
# print([1,2,3]*5)
# print(5*[1,2,3])
#
#
# print(list(range(0,5,1))*3)
#
# print("ㅋ"*100)
#

    #
    # a=[10,20,30,40]
    # print(len(a))
#
# # print(len(b))
# # b=(1,21,54,7)
#
#
# print(len("hello"))
# print(len("안녕하세요"))
#


#
#
# s="안녕하세요"
# print(len(s.encode('utf-8')))
#
# a
#
# a=[5,6,7,8,9]
# print(a[3])
#
#
# a=(5,6,7,8,9)
# print(a[3])
#
#
# r=range(1,10,2)
# # print(r[2])
# #
# #
# # s='hello'
# # print(s[2])
#
#
# print(r[-10])
#
#



# del 시퀀스객체[인덱스] : 튜플, range, 문자열은 삭제 안됨
# b=[10,20,30,40]
# del b[1]
# print(b)
#
# h="hello"
# del h[2]
# print(h)
#

# a=[10,20,30,40]
# print(a[0:3])
# print(a[0:0])
# print(a[0:1])
# print(a[1:-1:1])
# # print(a[3:1:-1])
# # print(a[0:len(a)])
# # print(a[:3:2]) # a[0]부터 a[2], 2칸씩 건너뛰기
#
# r=range(20)
# print(r[3:8])
# # print(list(r[:15:3]))
#
#
# s="hello python"
# print(s[:10])
# print(s[:10:2])
#

#
# print(range(20)[slice(3,9,2)])
# print(list(range(5, 20)[slice(3,9,2)]))

# a=list(range(10))
# print(a)
# a[1:4]='a'
# print(a)
# a[1:4]=['a','b','c']
# print(a)

# a[2:7:2]=['x','y','z']
# print(a)
#
# a=list(range(10))
# print(a)
# del a[2:5]
# print(a)


# d= {'name':'kim', 'addr':'seoul', 'age':25, 'nn':['별명1','별명2']}   # {키:값,...}, 키는 따옴표로 묶어서 표현, 값은 수치는 그대로, 문자는 따옴표로
#
# myname='lee'
# myname='park'
#
# d2={1:"hi"}
# print(d2)


# 연관 데이터를 저장하기 위한 용도의 자료형

# dic={'아이디':'홍길동', '레벨':10}
# print(dic)
# a={}
# print(a)
# b=dict()
# print(b)


#
# dic={'아이디':'홍길동', '레벨':10, '체력':100, '공격력':200}
# print(dic)
# print(dict(zip(['a','b'],[1,2])))
# print(list(zip(['a','b'],[1,2])))
#
#
#
# 리스트 내부에 (키, 값)형식의 튜플로 표현




# c1=dict(아이디='홍길동', 레벨=10, 체력=100, 공격력=200)
# print(c1)
# c2=dict(zip(['아이디','레벨','체력','공격력'],['홍길동',10,100,200]))
# print(c2)
# c3=dict([('아이디','홍길동'), ('레벨',10), ('체력',100), ('공격력',200)])
# print(c3)
# c4=dict({'아이디':'홍길동', '레벨':10, '체력':100, '공격력':200})
# print(c4)
#
# # 딕셔너리 데이터 추가/삭제
# a={'nn':'bear'}
# # 딕셔너리 a에 데이터 추가하기
# a['addr']='seoul'
# a[100]=300
# print(a)
# # 딕셔너리변수명 [키이름]=값
#
#
# a['hobby']=['a','b','c']                    # {'nn': 'bear', 'addr': 'seoul', 100: 300, 'hobby': ['a', 'b', 'c']}
# print(a)
# del a[100]
# print(a)



# dic={'아이디':'홍길동', '레벨':10, '체력':100, '공격력':200}
# print(dic)
# print(dic.keys())
# print(dic.values())
# # print(dic.items())
#
# print("="*50)
# # mykey=(dic.keys())
# # print(mykey)
# # # print(mykey(0))
# # listmykey=list(mykey)
# # print(listmykey)
#
#
#
#
# dic={'아이디':'홍길동', '레벨':10, '체력':100, '공격력':200}
# dic['저항력']=100
# print(dic)
#
# print('민첩성' in dic)
#
#
# print(len(dic))
#
#
# 1. 리스트 생성 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 순위	영화
# 1	    닥터 스트레인지
# 2	    스플릿
# 3	    럭키
movie_rank=['닥터 스트레인지','스플릿', '럭키']
print(movie_rank)

# 2. movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append('배트맨')
print(movie_rank)

# 3. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)

# 4. movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# 5. movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:4]
print(movie_rank)

# 6. price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
# 출력 예시:[100, 130, 140, 150, 160, 170]
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[slice(1,7)])

# 7.슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[slice(0,9,2)])

# 8.슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# 실행 예:[5, 4, 3, 2, 1]
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 9.interest 리스트에는 아래의 데이터가 저장되어 있다. interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:삼성전자 Naver
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

# 10. interest 리스트에는 아래의 데이터가 바인딩되어 있다. interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest[0],interest[1],interest[3],interest[4])

# 11. interest 리스트에는 아래의 데이터가 바인딩되어 있다. join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

# 12. 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# 13. 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자. 문자열 슬라이싱 기법을 사용해 보자.
idn='881120-1068234'
print(idn[0:6],idn[7:13])

# 14. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자. 더하기(+)를 사용해 보자.
tttu=(1,2,3)
print(tttu+(4,))

# 15. 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
a[[1]] = 'python' # 리스트를 키로 설정하면 안됨
a[250] = 'python'

# 16. 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자. 딕셔너리의 pop 함수를 사용해 보자.
a = {'A':90, 'B':80, 'C':70}
print(a['B'])





































































