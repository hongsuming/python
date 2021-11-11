# 함수 작성
"""
def 함수명([매개변수...]):
    수행문
    ...
    [return 반환값]

함수명([인자...])
"""
from conda.cli.common import arg2spec

# 파이썬은 모듈 단위로 처리하고 파일로 저장
a = 1 # 모듈의 멤버
print(a)

def doFunc1(): # 모듈(라이브러리)의 멤버
    print('doFunc1')
    
def doFunc2(arg1, arg2):
    result = arg1 + arg2
    print(result)
    # return None 기본값이며 일반적으로 생략

print('뭔가를 하다가 함수 호출')
doFunc1()
print('뭔가를 하다가 함수 호출2')
doFunc1()
print('뭔가를 하다가 함수 호출3')
# doFunc2() 인자 적지 않으면 에러 TypeError: doFunc2() missing 2 required positional arguments: 'arg1' and 'arg2'
doFunc2(10, 20) # 30
doFunc2('파이썬', '만세') # 파이썬만세
# doFunc2('파이썬', 7) TypeError: can only concatenate str (not "int") to str
doFunc2('파이썬', str(7)) # 파이썬7
print(doFunc2('파이썬', str(7))) # None

print()
def doFunc3(arg1, arg2):
    imsi = arg1 + arg2
    if imsi %2 == 1:
        return # 빈손으로 함수 탈출
    else:
        return imsi
    print('처리') # 수행되지 않음 return 만나면 함수 탈출하기 때문
    
print(doFunc3(5, 6)) # None
print(doFunc3(5, 3)) # 8
bb = doFunc3(5, 3)
print('bb의 결과는 ', bb)

print()
def area_tri(a, b):
    c = a*b/2
    area_print(c)

def area_print(c):
    print('삼각형의 면적은 ', c)

area_tri(10, 20) # 100.0

print()
def swap(a, b):
    return b, a # return (b, a)와 동일 => tuple

a = 10; b = 20
cc = swap(a, b)
print(cc) # (20, 10)

print()
def isOdd(arg):
    return arg %2 == 1

print(isOdd(11)) # True

# if 조건식에서 함수 사용
myDict = {x : x*x for x in range(11) if isOdd(x)}
print(myDict)