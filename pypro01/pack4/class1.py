# 클래스 : 자원의 재활용, 다형성을 구사
# 자바와 차이점 : 생성자의 모양이 다름, 메소드 오버로딩 없음, 다중 상속 가능, 멤버는 public, 모듈의 멤버는 중 하나
from future.builtins.misc import isinstance
print('뭔가를 하다가 클래스를 선언')
class TestClass: # 원형 클래스로 메모리를 확보 (기억 공간을 갖음)
    aa = 1 # 멤버 변수, 멤버 필드, 클래스 변수
    
    def __init__(self):
        print('생성자')
    
    def __del__(self):
        print('소멸자')
        
    def printMsg(self):
        print('메소드')
        name = '홍길동' # 메소드 내에서만 유효한 지역 변수
        print(name)
        print(self.aa) # 클래스의 멤버는 self.변수명
        
print(TestClass.aa)
# TestClass.printMsg(self) self 값을 매칭을 못 해서 에러 남 NameError: name 'self' is not defined

test = TestClass() # 생성자를 호출하고 TestClass 타입의 객체 생성
print(test.aa)
test.printMsg() # Bound method call (자동으로 파라미터로 들어감)
TestClass.printMsg(test) # UnBound method call (파라미터 직접 써야 됨)

print('클래스 타입은 ', isinstance(test, TestClass)) # test 객체 변수는 TestClass 타입이냐? True

print(type(test)) # <class '__main__.TestClass'>
print(id(TestClass)) # 2256122775216
print(id(test)) # 2256119822176

del test # 객체 변수 삭제