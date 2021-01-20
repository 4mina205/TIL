#
#
#
#
#
# # 1.(0~9)의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.
# # 입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
# # 출력 예시: True False False True False
import re
# res=[]
# for i in range(10):
#     res=re.findall(str(i),'num')
#     if len(res)==0 or len(res)>1:
#         print('F')
#         break
# else:
#     print("T")
#
#
#     # print(len(res))
# # print(re.match("01{1}2",'01123224567890'))
# # res=re.search(num5)
# # print(res)
# # print(re.match("do{2}g","doooooooooog"))
#
# # 2.
# # emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
# #           'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
# #           'python.dojang@e-xample.com',                                    # 올바른 형식
# #           '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식
# for i in emails:
#     if re.match("[a-z-.0-_9]+[@][a-z-]+[.][a-z]+[.]*[a-z]", i):
#         print(i,"= 올바른 형식")
#     else:
#         print(i,"= 잘못된 형식")
# # 3.
# # 1)[캐스터]가 캐스팅한 내용만 추출하시오
# # 2)달린 댓글의 개수를 출력하시오
# # 3)대전의 온도를 출력하시오
# # 4)가장 많이 등장한 단어가 무엇인가요?
# # 5)가장 많이 등장한 글자는 무엇이며, 총 몇 번 등장했나요?
#
new="""

연합뉴스TV
[날씨] 추위 대신 미세먼지 말썽…밤까지 중부 중심 눈
기사입력 2021.01.12. 오후 1:40 기사원문 스크랩 본문듣기  설정
화나요 후속기사원해요 좋아요 평가하기9 댓글9
글자 크기 변경하기
 인쇄하기
보내기
동영상 뉴스
[앵커]
오늘은 추위가 풀리는 대신 서쪽 지역의 공기 질이 나쁘겠습니다.
중부지방을 중심으로 눈도 내리겠습니다.
기상캐스터 연결해서 날씨 정보 더 자세히 알아보겠습니다.
김민지 캐스터.

[캐스터]
네, 추위가 한층 풀렸습니다.
어제보다 옷차림을 조금 더 가볍게 하고 나왔는데도 크게 춥지 않습니다.
내륙에 내려졌던 한파특보는 모두 해제가 됐고요.
오늘 한낮에 전국에 영상권으로 올라서겠습니다.
한낮에 서울은 1도, 대전 3도, 대구 5도 등 어제보다 5도 정도 기온이 높겠습니다.
따뜻한 서풍이 불어오면서 추위의 힘이 약해지는 건데요.
이 서풍을 타고 또 미세먼지가 들어오겠습니다.
대기 정체로 먼지가 쌓이면서 오늘은 서쪽 지역을 중심으로 미세먼지 농도 나쁨 수준 보이겠고요.
밤에 중국발 오염물질까지 들어와서 내일은 전국적으로 공기 질 상황이 나쁘겠습니다.
오늘 전국에 구름이 많습니다.
차츰 중부를 중심으로 눈이 내리겠습니다.
수도권과 충남, 전북에 1~3cm, 강원 영서와 충북, 경북과 제주 산지에 최고 5cm의 눈이 내려 쌓이겠습니다.
대부분 오늘 밤이면 그칠 텐데요.
강원 영서 지역은 내일 새벽까지 눈이 이어지겠습니다.
지금은 눈발 정도만 날리고 있습니다.
눈이 쌓이면서 퇴근길 무렵에는 길이 많이 미끄럽겠습니다.
조심히 이동하시기 바랍니다.
날씨 전해 드렸습니다.
"""
#
# a=re.search("\\[캐스터\\]\\n",new)
# print(new[a.end():])
#
# b=re.search("[댓글](?P<num>[0-9]+)",new)
# print('댓글 :',b.group('num'))
#
# c=re.search("[(대전)]\s(?P<deg>[0-9]+)",new)
# print('대전 온도 :',c.group('deg'))

res_list=re.findall("[가-힣][가-힣]+",new)
res_dic={}
for i in res_list:
    res_dic[i]=None
for j in res_dic.keys():
    n=0
    for z in res_list:
        if j==z:
            n+=1
    res_dic.update({j:n})
print([k for k, v in res_dic.items() if v == max(res_dic.values())],":",max(res_dic.values()))




#
# li = new.split()
#
# word_cnt={}
#
# for i in li:
#     cnt = li.count(i)
#
#
#
# li = list(new)
#
# li=' '.join(li).split()
#
# word_cnt={}
#
# for i in li:
#     cnt = li.count(i)
#     word_cnt[i]=cnt
#
# print([(k,v) for k,v in word_cnt.items() if max(word_cnt.values()) == v])