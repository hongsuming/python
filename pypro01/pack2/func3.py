# 변수의 생존 범위 (scope rule)
# 접근 순서 : Local > Enclosing function > Global

player = '전국대표' # 전역변수(Global)

def funcSoccer():
    name = '신기해' # 지역변수 (Local)
    player = '조기 축구 선수대표'
    print(name, player) 

# 참고
aa = funcSoccer # 함수의 주소 치환
print('1번', aa) # 1번 <function funcSoccer at 0x0000028EF5CD71F0>
print('2번', aa()) # 2번 None
aa2 = funcSoccer() # 신기해 조기 축구 선수대표
print('3번', aa2) # 3번 None

print('--------')
funcSoccer() # 신기해 조기 축구 선수대표

# print(name) NameError: name 'name' is not defined
print(player) # 전국대표

print('***' * 10)
a = 10; b = 20; c = 30
print('처리 1 => a:{}, b:{}, c:{}' .format(a, b, c))
def foo(): # Enclosing function
    a = 40
    b = 50
    def bar(): # 함수 내에 함수 선언
        global c
        nonlocal b
        print('처리 2 => a:{}, b:{}, c:{}' .format(a, b, c))
        c = 60
        b = 70
    bar()
    print('처리 3 => a:{}, b:{}, c:{}' .format(a, b, c))
foo()
print('처리 4 => a:{}, b:{}, c:{}' .format(a, b, c))