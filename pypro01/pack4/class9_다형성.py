# 메소드 오버라이드를 이용해 다형성 구사
class Parent:
    def printData(self):
        pass

class Child1(Parent):
    def printData(self):
        print('child1에서 override')
        
class Child2(Parent):
    def printData(self):
        print('child2에서 재정의')
        print('부모 메소드와 동일한 이름을 가지나 기능은 다르다.')
        
    def aa(self):
        print('child2 고유 메소드')
        
c1 = Child1()
c1.printData()
c2 = Child2()
c2.printData()

print('다형성 : 동일한 명령문이나 기능은 다름')
# par = Parent() 굳이 부모 객체를 만들고 자식 객체를 치환하지 않아도 됨
par = c1 # 자식의 객체변수를 치환할 때 꼭 부모 객체 변수에 치환할 필요가 없음. 일반 변수에도 치환 가능
par.printData() # child1에서 override
par = c2
par.printData() # child2에서 재정의
                # 부모 메소드와 동일한 이름을 가지나 기능은 다르다.
par.aa() # child2 고유 메소드

print()
plist = [c1, c2]
for i in plist:
    i.printData()
    print()