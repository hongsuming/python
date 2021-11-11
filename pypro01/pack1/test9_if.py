# 조건 판단문 if
var = 5

if var >= 3:
    print('크구나')
    print('참일 때')
    #pass
else:
    print('거짓일 때')

print('end1')

print()
money = 300
age = 23
if money >= 500:
    item = '사과'
    if age <= 30:
        msg = '와우 젊다'
    else:
        msg = '허걱 나이 좀 있네'
else:
    item = '감'
    if age >= 20:
        msg = '성인'
    else:
        msg = '미성년'
print(item, msg)
print('end2')

print()
jumsu = 85
if jumsu >= 90:
    print('우수')
else:
    if jumsu >= 70:
        print('보통')
    else:
        print('저조')

if jumsu >= 90:
    print('우수2')
elif jumsu >= 70:
    print('보통2')
else:
    print('저조2')
print('end3')

print()
# input으로 받으면 str이기 때문에 int로 형 변환
#jum = int(input('점수 입력:')) 
jum = 88
print(jum, type(jum))
if jum >= 90:
    print('good')
elif jum >= 70:
    print('nice')
else:
    print('normal')
    
print()
if 90 <= jum <= 100:
    print('good2')
elif 70 <= jum < 90:
    print('nice2')
else:
    print('normal2')
    
print()
names = ['홍수민', '김진석', '홍재훈'] # list
if '고길동' not in names:
    print('맞아 그게 나야')
else:
    print('뉘구?')
    
print()
a = 'kbs'
b = 9 if a == 'kbs' else 11
print(b)

a =  11
b = 'mbc' if a == 9 else 'kbs'
print(b)

print()
a = 3
if a < 5:
    print(0)
elif a < 10:
    print(1)
else:
    print(2)

# 위 코드를 한 줄로
print(0 if a < 5 else 1 if a < 10 else 2)

print()
a = 5
result = a * 2 if a > 3 else a + 2
print('result: '+str(result))