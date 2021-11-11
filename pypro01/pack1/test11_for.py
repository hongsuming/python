# 반복문 for
for i in [1,2,3,4,5]:
    print(i, end = ' ')

print()
print("list")
colors_list = ['red', 'green', 'blue']
for c in colors_list:
    print('색은 %s' %c, end = ' ')

print()
print("tuple")
colors_tuple = ['red', 'green', 'blue']
for c in colors_tuple:
    print('색은 %s' %c, end = ' ')
    
print()
print("set")
colors_set = {'red', 'green', 'blue'}
for c in colors_set:
    print('색은 %s' %c, end = ' ')
    
print()
print("dict")
colors_dict = {'빨간색':'red', '초록색':'green', '파란색':'blue'}
for c in colors_dict.items():
    print(c)

print()
for k in colors_dict.keys():
    print(k, end=' ')

print()
for v in colors_dict.values():
    print(v, end=' ')
    
print()
for a, b in colors_dict.items():
    print(a, ', ', b)

print()
print('평균, 분산, 표준편차 구하기')
jum = [6, 5, 4, 7, 3.5]
tot = 0
for i in jum:
    tot += i

avg = tot / len(jum)
print('avg = ', avg) # 평균

tot = 0
for i in jum:
    tot += (i-avg) ** 2 
var = tot / len(jum)
print('var : ', var) # 분산
import math
print('std : ', math.sqrt(var)) # 표준 편차

print()
for n in [2, 3]:
    print('{}단'.format(n))
    for num in [1,2,3,4,5,6,7,8,9]:
        print('{} * {} = {}'.format(n, num, n*num))
        
print()
li = ['a', 'b', 'c']
for idx, data in enumerate(li):
    print(idx, ' ', data)
    
print('continue & break')
datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 2 : 
        continue
    if i == 4 :
        break
    print(i, end=' ')
else:
    print('정상 처리')
    
print()
li1 = [3, 4, 5]
li2 = [0.5, 1, 2]
for a in li1:
    for b in li2 :
        print(a + b, end = ' ')
print()
results = [a + b for a in li1 for b in li2]
for d in results:
    print(d, end = ' ')

print()
print('정규 표현식, for 사용 : 다량의 문자열을 분리해 건수 출력')
import re
# 웹에서 스크래핑 했다고 가정
# '''는 주석 처리도 가능하고, 문자열 처리도 가능
ss = '''
20대 남성이 한 상가 건물 화장실에서 몰카(몰래카메라)를 찍다가 덜미를 잡혔다. 그의 휴대폰에는 음란물을 비롯해 레깅스 등을 입은 여성의 뒤태를 몰래 촬영한 사진 수백장이 저장되어 있었다.
30일 한경닷컴 취재를 종합하면 A 씨는 전날 오후 4시께 서울 관악구 봉천동의 한 상가 화장실에서 몰카 촬영을 당했다는 시민의 신고를 받고 출동한 경찰에 체포됐다. A 씨는 성폭력범죄의 처벌 등에 관한 특례법(카메라 등을 이용한 촬영) 위반 혐의를 받는다. 
서울 소재의 한 대학교의 학생인 A 씨는 스터디카페에서 공부를 하던 중 상가내 남녀 화장실의 열쇠가 공용이라는 점을 알게된 후 범죄를 저질렀다. 40대 여성 B 씨가 여자 화장실로 들어가 용변을 보자 A 씨는 화장실 칸 아래로 휴대폰을 밀어 넣어 촬영을 시도했다.
칸막이 아래로 들어온 핸드폰을 발견한 B 씨는 "몰카 촬영을 당했다"라며 경찰에 신고했다. 신고를 접수한 경찰은 A 씨가 몰카를 촬영한 상가 화장실로 출동했고, 현행범 체포했다.
관계자에 따르면 A 씨의 휴대폰에는 직접 촬영한 몰카 등 수백 개의 음란물이 저장돼 있었다. 레깅스와 같은 신체에 밀착된 의상을 입은 여성의 뒷모습을 몰래 촬영한 사진이 많았으며 주로 지하철에서 범행을 저지른 것으로 파악됐다.
이번 범행 외에도 다른 여성을 찍은 몰카 여러 장이 발견되자 A 씨는 경찰에 "용변보는 몰카를 촬영하기 시작한 건 2~3일밖에 지나지 않았다"라고 진술했다. 
서울 관악경찰서 관계자는 "A 씨를 입건했으며 현재까지는 불구속 상태로 조사할 계획"이라며 "압수한 휴대폰으로는 포렌식을 진행할 방침"이라고 말했다. 
경찰은 A 씨가 과거에도 비슷한 유형의 범죄를 저지른 것으로 보고 수사를 진행할 예정이다. 
'''
ss2 = re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
ss3 = ss2.split(' ')
print(ss3)
cou = {} # 단어 횟수를 dict로 저장

for i in ss3:
    if i in cou:
        cou[i] += 1 # 같은 단어가 있을 때 누적
    else:
        cou[i] = 1
print(cou)

print()
print('dict type(사전형)의 변수로 과일 값 계산')
price = {'사과' : 2000, '감' : 500, '배' : 3000} # 개 당 가격
gogek_tom = {'사과' : 2, '배' : 3} # 손님이 구매한 과일 갯수
bill = sum(price[f]*gogek_tom[f] for f in gogek_tom)
print('과일 값 총액 : {}원' .format(bill))

print('\nfor문 한 줄로 표현')
a = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
li = []
for i in a:
    if i%2 == 0:
        li.append(i)
print(li)
# 위 코드를 한 줄로 표현
print(list(i for i in a if i%2 == 0))

print()
datas = [1, 2, 'a', True, 3.5]
li = [i*i for i in datas if type(i) == int]
print(li)

print()
datas = {1, 1, 2, 2, 3} # set type 중복 불가
li2 = [i*i for i in datas]
print(li2)

print()
id_name = {1:'tom', 2:'james'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print()
aa = [(1,2), (3,4), (5,6)]
for a,b in aa:
    print(a + b, end = ' ')
