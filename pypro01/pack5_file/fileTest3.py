# 키보드로 통이름을 입력해 해당 자료 읽기
try:
    dong = input('찾는 동네의 이름을 입력하세요 : ')
    with open('zipcode.txt', mode = 'r', encoding = 'euc-kr') as f1:
        line = f1.readline()
        while line: # 자료가 있으면 true
            # lines = line.split('\t')
            lines = line.split(chr(9)) # tab을 '\t'으로 표현해도 되지만, 아스키코드로 표현해도 됨
            # print(lines) ['135-806', '서울', '강남구', '개포1동 경남아파트', '', '1\n']
            
            if lines[3].startswith(dong):
                # print(lines)
                print('[' + lines[0] + ']' + ' ' + lines[1] + \
                      ' ' + lines[2] + ' ' + lines[3] + ' ' + lines[4])
                
            line = f1.readline()
    
except Exception as e:
    print('error : ', e)