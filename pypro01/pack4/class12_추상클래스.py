# 추상클래스 : 추상 메소드를 가지고 있는 클래스, 추상 클래스를 상속 받은 자식 클래스는 반드시 추상 메소드를 오버라이드 해야 함
from abc import *
class TestClass(metaclass = ABCMeta): # 추상클래스가 됨. TestClass 타입의 객체 생성 불가
    @abstractmethod
    def abcMethod(self): # 추상메소드
        pass

    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드')
        
# parent = TestClass() 추상클래스는 스스로 인스턴스 할 수 없음 TypeError: Can't instantiate abstract class TestClass with abstract methods abcMethod

class Child1(TestClass): # 반드시 추상클래스의 추상메소드를 오버라이딩 해야 됨 안 하면 에러
    name = '난 Child1 멤버 변수 입니다.'
    
    def abcMethod(self): # 추상 메소드 오버라이드 강요 받음
        print('추상 메소드를 오버라이드 함')

c1 = Child1()
print(c1.name) # 난 Child1 멤버 변수 입니다.
c1.abcMethod() # 추상 메소드를 오버라이드 함
c1.normalMethod() # 추상 클래스 내의 일반 메소드

class Child2(TestClass):
    def abcMethod(self): # 강요
        print('추상 메소드를 Child2에서도 오버라이드 함')
        
    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드는 오버라이드 해도 되고 안 해도 됨')

c2 = Child2()
c2.abcMethod()
c2.normalMethod()

sss = c1
sss.abcMethod() # 추상 메소드를 오버라이드 함
sss = c2
sss.abcMethod() # 추상 메소드를 Child2에서도 오버라이드 함