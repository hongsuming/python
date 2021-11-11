# 파이썬은 일급 함수를 지원
# 함수 안에 함수 선언 가능, 인자로 함수 전달, 반환 값으로 함수 가능
def func1(a, b):
    return a + b

func2 = func1 
print(func1(2, 3)) # 5
print(func2(2, 3)) # 5
print()
def func3(fun): # 인자로 함수 전달
    def func4(): # 함수 안에 함수 선언
        print('나는 내부 함수야')
    func4()
    return fun # 반환 값으로 함수

mbc = func3(func1)
print('mbc(3,4) = ', mbc(3, 4)) # mbc(3,4) =  7

print()
print('축약함수 (Lambda - 이름이 없는 한 줄짜리 함수)')
# 형식 - lambda 인자,,, : 표현식
def hap(x, y):
    return x+y 
print(hap(2, 3))
print()
print('위 소스를 람다로 표현')
print((lambda x, y : x + y)(2, 3)) # 5

gg = lambda x, y : x + y * 2
print(gg) # <function <lambda> at 0x00000205218FA700>
print(gg(5, 5)) # 15

print()
kbs = lambda a, su = 10 : a + su
print('kbs(9) = ', kbs(9)) # kbs(9) =  19
print('kbs(9, 2) = ', kbs(9, 2)) # kbs(9, 2) =  11

print()
sbs = lambda a, *tu, **di : print(a, tu, di)
sbs(1, 2, 3, 3, 4, 6, 첫째 = '홍지연', 둘째 = '홍수민', 막내 = '홍재훈')

print()
li = [lambda a, b : a + b, lambda a, b : a * b, lambda : 20]
print(li[0], li[1]) # <function <lambda> at 0x000002B02BFAA8B0> <function <lambda> at 0x000002B02BFAA940>
print(li[0](3, 4)) # 7
print(li[1](3, 4)) # 12
print(li[2]()) # 20

print('함수 인자로 람다 사용')
# filter(함수, sequence 자료)
print(list(filter(lambda a : a < 5, range(10)))) # [0, 1, 2, 3, 4]
print(list(filter(lambda a : a % 2, range(10)))) # [1, 3, 5, 7, 9] 0 : False / 1 : True