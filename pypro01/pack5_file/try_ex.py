# 예외처리 : 파일, 네트워크, 키보드, DB 연동, 나누기

def divide(a, b):
    return a / b

c = divide(5, 2) # 2.5
# c = divide(5, 0) ZeroDivisionError: division by zero
print(c)

# 에러에 대한 대처 작업 : try ~ except

try:
    kbs = 9
    c = divide(5, 2)
    # c = divide(5, 0) # 에러가 발생하면 바로 except로 이동
    print(c)
    
    aa = [1, 2]
    print(aa[0])
    # print(aa[5]) # IndexError: list index out of range
    
    f = open('c:/work/abc.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'c:/work/abc.txt'
    
except ZeroDivisionError:
    print('두 번째 숫자는 0을 주면 안 돼!!')
    
except IndexError as e:
    print('참조 범위 오류 : ', e)
    
except Exception as e:
    print('에러 발생 : ', e)

finally:
    print('에러가 있든 없든 꼭 수행됨')
    del kbs

print('다음 작업 계속')
# print(kbs) finally에서 del했기 때문에 에러 남 NameError: name 'kbs' is not defined