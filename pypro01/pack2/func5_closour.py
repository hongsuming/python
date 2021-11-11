# 클로저(closure) : scope에 제약을 받지 않는 변수들을 포함하고 있는 코드 블록이다.
# 함수 내의 지역변수를 함수 밖에서 참조를 가능하게 함
from pack1.test11_for import aa

# 선행학습
def funcTimes(a, b):
    c = a*b
    return c 

print(funcTimes(2, 3)) # 6
kbs = funcTimes(2, 3)
print(kbs) # 6

kbs = funcTimes
print(kbs) # <function funcTimes at 0x00000206A2B071F0>
print(kbs(2, 3)) # 6
print(id(funcTimes), id(kbs)) # 2219332497904 2219332497904

del funcTimes # 객체의 주소를 기억하고 있는 변수를 지워버림
# print(funcTimes(2, 3)) NameError: name 'funcTimes' is not defined
print(kbs(2, 3)) # 6

"""
aa = 10
print(aa, id(aa))
del aa
# print(aa) NameError: name 'aa' is not defined
"""

mbc = sbs = kbs
print(mbc(3, 4)) # 12
print(sbs(3, 4)) # 12

print()
print('클로저를 사용하지 않은 경우')
def out():
    count = 0 # out의 멤버
    def inn(): # out의 멤버
        nonlocal count # out, inn의 멤버
        count += 1 # out ,inn의 멤버
        return count 
    print('inn() = ', inn())
out() # inn() =  1
out() # inn() =  1
out() # inn() =  1

print('클로저를 사용한 경우')
def outer():
    count = 0 # out의 멤버
    def inner(): # out의 멤버
        nonlocal count # out, inn의 멤버
        count += 1 # out ,inn의 멤버
        return count 
    return inner # 클로저 : 내부 함수의 주소를 반환

print(outer()) # ('inner = ', <function outer.<locals>.inner at 0x0000013FA0C4E4C0>)
var1 = outer()
print(var1()) # 1
print(var1()) # 2
print()
var2 = outer()
print(var2()) # 1
print(var2()) # 2

print('수량 * 단가 * 세금을 출력하는 함수 작성')
def outer2(tax): # tex는 지역변수
    aa = tax
    def inner2(su, dan):
        amount = su*dan*tax
        return amount
    return inner2 # 클로저

# 1분기에는 tax(세금)가 0.1로 부과
q1 = outer2(0.1)
result1 = q1(5, 50000)
print('result1 : ', result1)
result2 = q1(2, 10000)
print('result2 : ', result2)
        
print()
# 2분기에는 tax(세금)가 0.5로 부과
q2 = outer2(0.05)
result3 = q2(5, 50000)
print('result3 : ', result3)
result4 = q2(2, 10000)
print('result4 : ', result4)
    