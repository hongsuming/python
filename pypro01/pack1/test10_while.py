# 반복문 while
a = 1
while a <= 5:
    print(a, end=' ')
    a += 1
print('\n탈출 후 a :', a)

print()
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i:'+str(i) + ', j:'+str(j))
        j += 1
    i += 1

print('1~100 사이의 정수 중 3의 배수의 합 출력')
i = 1; hap = 0; count = 0
while i <= 100:
    if i %3 == 0:
        hap += i
        count += 1
    i += 1
print('합은', hap)
print('건수는', count)

print()
colors = ['red', 'green', 'blue', 'yellow', 'black']
index = 0
while index < len(colors):
    print(colors[index], end = ' ')
    index += 1
    
print()
print('수행 전 : ', len(colors))
while colors: # colors에 데이터가 있기 때문에 true
    print(colors.pop())

print('수행 후 : ', len(colors))

print('별 찍기')
i = 1
while i <= 10:
    j = 1
    str = ''
    while j <= i:
        str += '*'
        j += 1
    print(str)
    i += 1
    
print('폭탄 터트리기')
import time
print(time.localtime().tm_year)
# time.sleep(3)
# print('종료')
sw = input('폭탄 스위치를 누를까요 [y/n]')
if sw == 'y' or sw == 'Y':
    count = 5
    while 1 <= count:
        print('%d초 남았습니다.' %count)
        time.sleep(1)
        count -= 1
    print('펑!!!!!!!!!!!!!!!')
elif sw == 'n' or sw == 'N':
    print('작업 취소')
else:
    print('y 또는 n만을 입력하세요')