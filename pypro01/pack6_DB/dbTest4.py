# 키보드에서 부서번호를 입력 받아 해당 부서 직원 자료 출력
import MySQLdb
import pickle

with open('mariaDB.dat', 'rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config) # dict 타입은 ** 써줘야 데이터들 다 넘어감
        cur = conn.cursor()
        
        buser_no = input('부서번호를 입력하세요 : ')
        sql = "select * from jikwon where buser_num = {}" .format(buser_no)
        cur.execute(sql)
        datas = cur.fetchall()
        
        if len(datas) == 0:
            print(str(buser_no) + '번 부서는 존재하지 않습니다.')
        
        for i in datas:
            for j in range(8):
                print(i[j], end = ' ')
            print()
        
        print('인원 수 : ', len(datas))
                
    except Exception as e:
        print('error : ', e)

    finally:
        cur.close()
        conn.close()
        
if __name__ == '__main__':
    chulbal()
    
