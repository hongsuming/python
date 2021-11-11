# with 구문을 사용하면 close() 자동 지원
try:
    print('파일 저장')
    with open('fTest3.txt', mode = 'w', encoding = 'utf-8') as f1:
        f1.write('요즘 날씨가 계속 흐려\n')
        f1.write('몸이 찌뿌둥하다\n')
        f1.write('close() 자동으로 지원해줌\n')
    print('저장 완료')
    
    print('파일 읽기')
    with open('fTest3.txt', 'r', encoding = 'utf-8') as f2:
        print(f2.read())
except Exception as e:
    print('error : ', e)
    
print('\n피클링(객체를 저장하고 읽기)')
import pickle

try:
    dictData = {'tom':'1111-1111', '진석':'22'}
    listData = ['박소영', '박정수']
    tupleData = (dictData, listData)
    
    with open('hello.dat', 'wb') as f3: # 객체는 보통 wb(바이너리) 형식으로 저장
        pickle.dump(tupleData, f3) # 객체를 저장
        pickle.dump(listData, f3)
    print('객체를 파일로 저장 완료')
    
    with open('hello.dat', 'rb') as f4:
        a, b = pickle.load(f4) # 피클로 저장된 객체 읽기
        print(a)
        print(b)
        c = pickle.load(f4)
        print(c)
        
except Exception as e:
    print('error2 : ', e)