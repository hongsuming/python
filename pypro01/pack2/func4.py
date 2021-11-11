# 함수 : 인수(argument)와 매개변수(parameter) 키워드로 매칭
def showGugu(start, end = 5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')

showGugu(2, 9) # 순서로 매칭
print()
showGugu(3) # end가 초기값이 있기 때문에 인수 1개만 써도 3, 5로 인식
print()
showGugu(start = 7, end = 8)
print()
showGugu(end = 8, start = 7) # 이름으로 매칭
print()
showGugu(5, end = 6)
print()
# showGugu(start = 5, 6) SyntaxError: positional argument follows keyword argument
print()
# showGugu(end = 6, 5) SyntaxError: positional argument follows keyword argument

print('가변인수 처리----')
def func1(*ar): # tuple type으로 처리
    print(ar)

# func1() TypeError: func1() missing 1 required positional argument: 'ar'
#func1('공기밥', '김밥') TypeError: func1() takes 1 positional argument but 2 were given

func1() # 매개변수에 *을 달아주면 오류나지 않음
func1('공기밥', '김밥') # 매개변수에 *을 달아주면 오류나지 않음

print()
def func2(a, *ar):
    print(a)
    print(ar)
    
func2('비빔밥')
func2('비빔밥', '김밥', '공기밥')

print()
def selectProcess(choice, *ar):
    if choice == 'add':
        imsi = 0
        for i in ar:
            imsi += i
    elif choice == 'mul':
        imsi = 1
        for i in ar:
            imsi *= i
    return imsi

print(selectProcess('add', 1,2,3,4,5)) # 15
print(selectProcess('mul', 1,2,3,4,5)) # 120

print()
def func3(w, h, **other): # **는 dict type
    print('몸무게 : {}, 키 : {}' .format(w, h))
    print(other)
    
func3(54, 160, irum='홍수민', nai=24)

print()
def func4(a, b, *c, **d):
    print(a, b)
    print(c)
    print(d)

func4(1, 2)
func4(1, 2, 3, 4, 5)
func4(1, 2, 3, 4, 5, m = 6, n = 7, z = 8)