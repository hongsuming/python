# 로또 번호 생성 : 클래스의 포함 연습
import random

class LottoBall: # LottoUIUX의 부품으로 사용
    def __init__(self, num):
        self.num = num
        
class LottoMachine: # LottoUIUX의 부품으로 사용
    def __init__(self):
        self.ballList = [] # 로또 볼이 기억될 리스트
        for i in range(1, 46):
            self.ballList.append(LottoBall(i)) # 클래스의 포함
            
    def selectBall(self):
        for i in range(45): # 공을 섞기 전에 확인하기
            print(self.ballList[i].num, end = ' ')
            
        random.shuffle(self.ballList)
    
        print()
        for i in range(45): # 공을 섞은 후에 확인하기
            print(self.ballList[i].num, end = ' ')
            
        return self.ballList[0:6]
            
class LottoUIUX:
    def __init__(self):
        self.machine = LottoMachine() # 클래스의 포함 관계

    def playLotto(self):
        input('로또번호를 생성하려면 엔터키를 누르세요.')
        selectBalls = self.machine.selectBall()
        print("\n행운의 번호 : ")
        for i in selectBalls:
            print('%d' %i.num, end = ' ')
        
if __name__ == '__main__':
    # LottoUIUX().playLotto() Unbound method call
    user = LottoUIUX()
    LottoUIUX.playLotto(user)