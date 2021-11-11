# 클래스로 새로운 타입 선언하기 : 가수 클래스 (설계도) --> 객체 생성
class Singer:
    title_song = '화이팅 코리아'
    
    def sing(self):
        msg = '노래는 '
        print(msg + self.title_song + ' 랄랄라~~')
        
bts = Singer()
print(type(bts)) # <class '__main__.Singer'>

bts.sing() # 노래는 화이팅 코리아 랄랄라~~
bts.title_song = '버터'
bts.sing() # 노래는 버터 랄랄라~~
bts.co = '빅히트엔터테인먼트'
print('소속사 : ', bts.co) # 소속사 :  빅히트엔터테인먼트

print()
blackpink = Singer()
print(type(blackpink)) # <class '__main__.Singer'>
blackpink.sing() # 노래는 화이팅 코리아 랄랄라~~
# print('소속사 : ', blackpink.co) AttributeError: 'Singer' object has no attribute 'co'

print(id(bts)) # 2299069497200
print(id(blackpink)) # 2299075994096
