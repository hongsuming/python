# while 계속
a = 0

while a < 10:
    a += 1
    if a == 5 or a == 7 : continue # continue를 만나면 조건으로 올라감
    if a == 8 : break # 반복문 무조건 탈출
    print(a)
else:
    print('while 정상 수행')
    
print('while 수행 후 %d' %a)
"""
print('홀수 짝수 확인하기')
while True:
    num = int(input('정수를 입력해주세요.'))
    if num == 0:
        print('프로그램 종료')
        break
    elif num %2 == 0:
        print('%d는 짝수입니다.' %num)
    elif num %2 == 1:
        print('%d는 홀수입니다.' %num)
"""

print('임의의 숫자 알아내기')
import random # 난수 발생 모듈
# random.seed(1) 난수가 필요하긴 한데 매번 같은 값을 받을 수 있음
# print(random.random()) # 0~1 사이의 난수 발생
# print(random.randint(1, 10)) # 1~10 사이의 난수 발생
num = int(random.randint(1, 10))
while True:
    print('1 ~ 10 사이의 컴이 가진 예상 숫자 입력 : ')
    guess = input()
    num2 = int(guess)
    if num2 == num:
        print('성공~~~')
        break
    elif num2 < num:
        print('더 큰 수를 입력하세요.')
    elif num2 > num:
        print('더 작은 수를 입력하세요.')