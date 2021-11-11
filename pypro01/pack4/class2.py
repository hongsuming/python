class Car: # 클래스의 이름은 대문자로 시작 (권장)
    handle = 0 # 멤버 변수 - prototype
    speed = 0 

    def __init__(self, name, speed): # 지역변수
        self.speed = speed
        self.name = name

    def showData(self):
        km = '킬로미터' # 메소드 내에서 유효한 지역변수
        msg = '속도 ' + str(self.speed) + km + ', handle 수 : ' + str(self.handle) 
        return msg
    
print(id(Car), Car.handle, Car.speed) # 원형 클래스 멤버 출력
car1 = Car('benz', 10) # 생성자(인수 3개) 호출
print(car1.handle, car1.name, car1.speed)
car1.color = '파랑' # 멤버변수 그냥 만들어도 됨
print(car1.color)
print()
car2 = Car('bmw', 20)
print(car2.handle, car2.name, car2.speed)
# print(car2.color) car2에는 color를 만들어주지 않았기 때문에 에러남 AttributeError: 'Car' object has no attribute 'color'

print('주소 출력 : ', id(Car), id(car1), id(car2)) # 주소 출력 :  1889204971440 1889212146880 1889212146928
print(Car, car1, car2) # <class '__main__.Car'> <__main__.Car object at 0x0000018C0727A4C0> <__main__.Car object at 0x0000018C0727A4F0>
# .__dict__ : 각 객체의 멤버를 확인하는 명령
print(Car.__dict__) # {'__module__': '__main__', 'handle': 0, 'speed': 0, '__init__': <function Car.__init__ at 0x0000021BA4CAB280>, 'showData': <function Car.showData at 0x0000021BA4CAB5E0>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
print(car1.__dict__) # {'speed': 10, 'name': 'benz', 'color': '파랑'}
print(car2.__dict__) # {'speed': 20, 'name': 'bmw'}

print('\n메소드 호출')
print('car1 메소드 : ', car1.showData()) # car1 메소드 :  속도 10킬로미터, handle 수 : 0
print('car2 메소드 : ', car2.showData()) # car2 메소드 :  속도 20킬로미터, handle 수 : 0
car1.speed = 100
car2.speed = 120
print('car1 메소드 : ', car1.showData()) # car1 메소드 :  속도 100킬로미터, handle 수 : 0
print('car2 메소드 : ', car2.showData()) # car2 메소드 :  속도 120킬로미터, handle 수 : 0
print()
print(Car.speed) # 0
print(car1.speed) # 100
print(car2.speed) # 120