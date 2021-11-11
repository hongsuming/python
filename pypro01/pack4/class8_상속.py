# 상속
from boto.gs.lifecycle import AGE
class Person:
    say = "person say 안녕 난 사람이야"
    age = 20
    __abc = 'good' # private 멤버변수
    
    def __init__(self, age):
        print("person 생성자")
        self.age = age
        
    def printInfo(self):
        print("person printInfo 나이 : {}, 이야기 : {}" .format(self.age, self.say))

    def hello(self):
        print("person hello 안녕하세영")
        print("person private 변수", self.__abc)
        
print(Person.say, Person.age)
p = Person(24)
p.printInfo()
p.hello()
# p.__abc AttributeError: 'Person' object has no attribute '__abc'
 
print('**' * 10)
class Employee(Person): # Person의 자식 클래스
    say = "일하는 동물"
    subject = "근로자"
    
    def __init__(self):
        print("employee 생성자")
        
    def printInfo(self): # 메소드 오버라이드
        print("employee 클래스에서 오버라이드한 printInfo")
        
    def e_printInfo(self):
        self.printInfo()
        super().printInfo() # 부모 메소드 호출
        print(self.say, super().say)
        
e = Employee()
print(e.say, e.age, e.subject)
e.e_printInfo()

print('**' * 10)
class Worker(Person):
    def __init__(self, age):
        print("worker 생성자")
        super().__init__(age) # 부모 클래스의 생성자 호출 bound method call
        
    def w_printInfo(self):
        self.printInfo()
        
w = Worker(22)
print(w.say, w.age)
w.w_printInfo()

print('**' * 10)
class Programmer(Worker):
    def __init__(self, age):
        print("programmer 생성자")
        # super().__init__(age)
        Worker.__init__(self, age) # super()과 동일함 unbound mthod call
        
    def p_printInfo(self):
        self.printInfo()
        
pr = Programmer(15)
print(pr.say, pr.age)
pr.p_printInfo()

print('\n클래스 타입 확인')
a = 10; print(type(a)) # <class 'int'>
print(type(pr), type(w), type(p)) # <class '__main__.Programmer'> <class '__main__.Worker'> <class '__main__.Person'>
print(Programmer.__bases__) # (<class '__main__.Worker'>,)
print(Worker.__bases__) # (<class '__main__.Person'>,)
print(Person.__bases__) # (<class 'object'>,)