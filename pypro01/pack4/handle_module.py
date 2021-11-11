# 부품을 별도의 클래스로 작성
# 핸들: 방향을 움직이는 기계 부품
class PohamHandle:
    # 음수 : 좌회전 / 정수 : 우회전
    quantity = 0 # 회전량
     
    def leftTurn(self, quantity):
        self.quantity = quantity
        return '좌회전'
    
    def rightTurn(self, quantity):
        self.quantity = quantity
        return '우회전'
    