# 자동차를 생산 : 여러 개의 부품(클래스로 구성)들을 조합
from pack4.handle_module import PohamHandle
print('자동차 클래스 설계 및 생성')
class PohamCar:
    turnShow = '정지'
    
    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle() # 클래스의 포함관계
        
    def turnHandle(self, q): # 운전을 하며 핸들을 움직임
        if q > 0 :
            self.turnShow = self.handle.leftTurn(q) # 포함 관계는 .이 2개 나옴
        elif q < 0 :
            self.turnShow = self.handle.rightTurn(q)
        elif q == 0 :
            self.turnShow = '직진'
            self.handle.quantity = 0
    
if __name__ == '__main__':
    tom = PohamCar('톰')
    tom.turnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity)) # 톰의 회전량은 좌회전10
    tom.turnHandle(0)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity)) # 톰의 회전량은 직진0
    
    print()
    gildong = PohamCar('길동')
    gildong.turnHandle(-15)
    print(gildong.ownerName + '의 회전량은 ' + gildong.turnShow + str(gildong.handle.quantity)) # 길동의 회전량은 우회전-15
    