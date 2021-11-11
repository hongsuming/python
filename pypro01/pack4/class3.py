# 클래스 기본 이해
kor = 100 # 전역변수

def abc():
    print("이건 함수")

class My:
    kor = 90 # 클래스 변수

    def abc(self):
        print("이것은 메소드입니다.")
    
    def show(self):
        # kor = 80 # 지역변수
        print(kor)
        print(self.kor)
        self.abc()
        abc()

my = My()
my.show()

print('**' * 20)

class Our:
    a = 1

print(Our.a) # 1
our1 = Our()
print(our1.a) # 1

our1.a = 2
print(our1.a) # 2

print()
our2 = Our()
print(our2.a) # 1
our2.kbs = 9
print(our2.kbs) # 9

print()
Our.a = 11
print(our1.a) # 2
print(our2.a) # 11