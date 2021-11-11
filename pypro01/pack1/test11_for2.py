# range 함수 : 수열 생성
print(list(range(1, 6)))
print(list(range(6)))
print(list(range(1, 6, 1)))
print(list(range(1, 6, 2)))
print(tuple(range(1, 6)))
print(set(range(1, 6)))

print()
for i in range(6):
    print(i, end=' ')
    
print('\n')
for _ in range(6): # 로컬변수가 쓰이지 않으면 _(underbar)로 표시 가능
    print('hi', end = ' ')
    
print('\n1 ~ 10까지의 합')
tot = 0 
for i in range(1, 11):
    tot += i
print(tot)
print(sum(range(1, 11)))

print()
for i in range(2, 10):
    for j in range(1, 10):
        print('{} * {} = {}' .format(i, j, i*j), end = ' ')
    print()

# 실습1) 반복문 for를 이용 : 1~100 사이의 정수 중 3의 배수이면서 5의 배수의 합, 건수 구하기
sum1 = 0
count = 0
for i in range(1, 101):
    if i %3 == 0 and i %5 == 0:
        sum1+=i
        count+=1
print('sum=', sum1, ', count=', count)

# 실습2) 주사위를 두 번 던져서 숫자들의 합이 4의 배수가 되는 경우만 출력
sum2 = 0
for i in range(1, 7):
    for j in range(1, 7):
        sum2 = i+j
        if sum2 %4 == 0:
            print('{} + {} = {}' .format(i, j, sum2))