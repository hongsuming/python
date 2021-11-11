# 연산자
v1 = 3 # 치환
v1 = v2 = v3 = 5
print(v1, v2, v3) # 5 5 5
print('출력1', end = ' ')
print('출력2')
v1 = 1, 2, 3 # 집합형
print(v1)
v1, v2 = 10, 20
print(v1, v2)
v1, v2 = v2, v1
print(v1, v2)

"""
print()
v1, v2 = 1,2,3,4,5 # 에러
print(v1, v2)
"""
print()
v1, *v2 = 1,2,3,4,5 # packing 연산
print(v1, v2)

print('성공') # 인터프리터 방식이기 때문에 16라인에서 에러가 떨어지면 거기서 바로 멈춤
"""
print()
*v1, *v2, v3 = 1,2,3,4,5 # packing 연산은 한 곳에만 줄 수 있음
print(v1, v2, v3)
"""
print()
*v1, v2, v3 = 1,2,3,4,5 # packing 연산
print(v1, v2, v3)

print('----------산술 연산-----------')
print(5 + 3, 5 - 3, 5 * 3, 5 / 3) # 8 2 15 1.6666666666666667
print(5 // 3, 5 % 3) # 몫, 나머지 1 2
print(5 ** 2) # 25
print(divmod(5, 3)) # 몫, 나머지(1, 2)

print('연산자 우선 순위 : ', 3 + 4 * 5, (3 + 4) * 5) # 연산자 우선 순위 :  23 35

print('----------관계 연산-----------')
print(5 > 3, 5 <= 3, 5 == 3, 5 != 3) # True False False True

print('----------논리 연산-----------')
print(5 > 3 and 4 < 3, 5 > 3 or 4 < 3, not(5 >= 3)) # False True False

print('----------문자열 연산-----------')
print('한' + "국인" + ' 만세') # 한국인 만세
print('한국' + '한국' + '한국' + '한국' + '한국') # 한국한국한국한국한국
print('한국' * 5) # 한국한국한국한국한국
print('***' * 20) # ************************************************************

print('----------누적-----------')
a = 10
print(a) # 10
a = a + 1
a += 1
# a++ 파이썬에서 증감 연산자는 쓸 수 없음
# ++a 파이썬에서 부호 변경으로 쓰임
print(a) # 12

print('----------부호 변경-----------')
print(a, a * -1, -a, +a, --a) # 12 -12 -12 12 12

print('----------boolean-----------')
print(True, False) # True False
print(bool(1), bool(3.5), bool('ok')) # True True True
print(bool(0), bool(0.0), bool(''), bool(None), bool([]), bool({}), bool(set())) # False False False False False False False

print('----------이스케이프 문자-----------')
print('aa\bb')
print('mbc\nbc')
print('c:\tbc\nbc')
# r(raw string)를 붙이면 이스케이프 문자로 취급하지 않고 순수 값을 출력
print(r'aa\bb')
print(r'mbc\nbc')
print(r'c:\tbc\nbc')

print('----------출력 서식 연습-----------')
print(1.5678)
print(format(1.5678, '10.3f')) # 전체 10자리 중 소수는 3자리만 표현

print('나는 나이가 %d살이다.' %24)
print('나는 나이가 %s살이다.' %'스물넷')
print('나는 나이가 %f살이다.' %24.9)
print('나는 나이가 %d살이고 이름은 %s, 키는 %f이다.' %(24, '홍수민', 160.2))
print('이름은 {}, 나이는 {}'.format('홍수민', 24))
print('이름은 {0}, 나이는 {1}'.format('홍수민', 24))
print('이름은 {1}, 나이는 {0}'.format('홍수민', 24))
print('이름은 {0}, 나이는 {1} {0}'.format('홍수민', 24))
