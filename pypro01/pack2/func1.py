#python은 멀티 패러다임이 가능한 언어
# 함수 : 내장 함수 경험
print(sum([3, 6, 8, 100]))
a = sum({1, 2})
print(a)

print()
print('python')
print(bin(8))
print(int(2.3), float(5), str(5)+'오')

a = 10
b = eval('a + 5')
print(b)

print(round(1.2), round(123.456)) # 반올림

import math
print(math.ceil(1.2), math.ceil(1.6)) # 올림
print(math.floor(1.2), math.floor(1.6)) # 버림

print()
b_list = [True, 1, False]
print(all(b_list)) # 모든 값이 참이면 참
print(any(b_list)) # 하나라도 참이면 참

print()
x = [19, 29, 30]
y = ['a', 'b']
for i in zip(x, y):
    print(i)