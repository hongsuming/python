# 추상 클래스
from abc import *
class Friend(metaclass = ABCMeta): # 추상클래스
    def __init__(self, name): # 추상클래스도 생성자 존재 가능
        self.name = name
        
    @abstractmethod
    def hobby(self): # 추상메소드
        pass
    
    def printName(self): # 일반메소드
        print('이름은 : ', self.name)
        
class John(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr
        
    def hobby(self): # 오버라이딩
        print(self.addr + ' 거리를 걸어다님')
    
    def printAddr(self):
        print('주소는 ' + self.addr)

class Chris(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr
        
    def hobby(self): # 오버라이딩
        print(self.addr + ' 동네를 뛰어다님')
        print(self.addr + '에 살고 있다')

j = John('존', '미국')
j.printName()
j.printAddr()
j.hobby()
c = Chris('크리스', '영국')
c.printName()
c.hobby()

print()
z = j 
z.printName()
z.hobby()
z = c 
z.printName()
z.hobby()