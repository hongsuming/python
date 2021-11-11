# @함수명 = 함수 장식자(function decorator) : 어떠한 기능(meta)을 발휘

print('함수 장식자 연습1')
def make2(fn):
    return lambda : '안녕 ' + fn()

def make1(fn): 
    return lambda : "반가워 " + fn()

def hello():
    return '홍수민'

hi = make2(make1(hello)) # 주소
print(hi()) # 안녕 반가워 홍수민

print()

@make2
@make1
def hello2():
    return "김진또"

hi2 = hello2()
print(hi2)

hi3 = hello2 # 주소
print(hi3())

print('---------------')
def deco1(f):
    return lambda : f() + 5 # 주소

def deco2(f):
    def print_f():
        print('f() = ', f()) # f() =  12
    return print_f # 주소 리턴

def func():
    return 7

ff = deco2(deco1(func))
ff() # 12

print()
@deco2
@deco1
def func2():
    return 7

func2() # f() =  12