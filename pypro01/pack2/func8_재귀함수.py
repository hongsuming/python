# 재귀함수(recursive function) : 함수가 자기 자신을 호출 - 반복처리 가능
def countDown(n):
    if n == 0:
        print('완료')
    else:
        print(n, end = ' ')
        countDown(n-1)
        
countDown(5)

print('1 ~ 10까지의 정수의 합')
def totFunc(num):
    if num == 1:
        print('그만하자')
        return 1 # True 역할
    return num + totFunc(num - 1)

result = totFunc(997)
print('합은 ', result) # 합은  55

print()
# 5! : 5*4*3*2*1
def factFunc(a):
    if a == 1 : 
        return 1
    print(a)
    return a * factFunc(a-1)

print('5! = ', factFunc(5)) # 5! =  120