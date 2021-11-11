# 정규 표현식
import re

ss = "1234 abc가나다ABC_555_6'Python is fun.123123"
print(ss)
print(re.findall('123', ss)) # ['123', '123', '123']
print(re.findall('가나', ss)) # ['가나']
print(re.findall('5', ss)) # ['5', '5', '5']
print(re.findall('[0-9]', ss)) # ['1', '2', '3', '4', '5', '5', '5', '6', '1', '2', '3', '1', '2', '3']
print(re.findall('[0-9]+', ss)) # ['1234', '555', '6', '123123']
print(re.findall('[a-z]+', ss)) # ['abc', 'ython', 'is', 'fun']
print(re.findall('[A-Z]+', ss)) # ['ABC', 'P']
print(re.findall('[a-zA-Z0-9]+', ss)) # ['1234', 'abc', 'ABC', '555', '6', 'Python', 'is', 'fun', '123123']
print(re.findall('[가-힝 ]+', ss)) # 한 칸 띄우면 공백도 나오게 함 ['가나다']
print(re.findall('[^가-힝 ]+', ss)) # 부정을 할 땐 ^ 붙이면 됨 ['1234', 'abc', "ABC_555_6'Python", 'is', 'fun.123123']
print(re.findall('^1+', ss)) # 시작되는 데이터 찾을 때도 ^ 붙임 ['1']
print(re.findall('3$', ss))
print()
# 이스케이프 문자 아니라고 r 붙여줌
print(re.findall(r'\d', ss)) # ['1', '2', '3', '4', '5', '5', '5', '6', '1', '2', '3', '1', '2', '3']
print(re.findall(r'\d+', ss)) # ['1234', '555', '6', '123123']
print(re.findall(r'\d{1,3}', ss)) # 1~3글자 사이 출력 ['123', '4', '555', '6', '123', '123']
print(re.findall(r'\d{2}', ss)) # 2글자 데이터 출력 ['12', '34', '55', '12', '31', '23']