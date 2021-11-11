# 내장된 모듈 읽기
# python은 모듈 단위로 저장, 읽기, 실행을 함
# 멤버 : 전역변수, 명령문(statement), 함수, 클래스, 다른 모듈

print('무언가를 하다가... 외부 모듈 읽기')
import sys
print('경로 : ', sys.path)
# sys.exit(0) # 프로그램 강제 종료
print('프로그램 종료') # 위에서 강제 종료했기 때문에 출력되지 않음

import math
print(math.pi)
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6)
calendar.prmonth(2021, 10)

print()
import os 
print(os.getcwd())
print(os.listdir('./'))

print('난수 출력')
import random
print(random.random()) # 0에서 1 사이의 규칙이 없는 실수 값이 나옴
print(random.randrange(1, 10)) # 1에서 10 사이의 난수가 나옴

print()
from random import *
print(random())
print(randrange(1, 10))