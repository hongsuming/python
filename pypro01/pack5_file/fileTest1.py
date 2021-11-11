# file io
import os 
from astropy.table._column_mixins import sys
print(os.getcwd()) # 현재 작업 경로를 알 수 있음 .getcwd()

try:
    print('파일 읽기')
    # f1 = open(r'C:\work\psou\pypro01\pack5_file\fTest', mode = 'r', encoding = 'utf-8')
    # f1 = open(os.getcwd() + r'\fTest', mode = 'r', encoding = 'utf-8')
    f1 = open('fTest.txt', mode = 'r', encoding = 'utf-8')
    print(f1)
    print(f1.read())
    f1.close()
except Exception as e:
    print('파일 처리 오류 : ', e)
    sys.exit(0)
    
print()

try:
    print('파일 저장')
    f2 = open('fTest2.txt', mode = 'w', encoding = 'utf-8')
    f2.write('My Friends\n')
    f2.write('kim jin seok, 23')
    f2.close()
    print('저장 성공')
    
    f2_1 = open('fTest2.txt', mode = 'a', encoding = 'utf-8') # a = append 파일의 내용 추가
    f2_1.write('\nhong jae hoon, 22')
    f2_1.write('\nhong ji yeon, 28')
    f2_1.close()
    
    f3 = open('fTest2.txt', mode = 'r', encoding = 'utf-8')
    print(f3.read())
    f3.close()
    
    print('한 줄씩 읽기')
    f4 = open('fTest2.txt', mode = 'r', encoding = 'utf-8')
    print(f4.readline())
    print(f4.readline())
    f4.close()
except Exception as e:
    print('파일 오류 : ', e)