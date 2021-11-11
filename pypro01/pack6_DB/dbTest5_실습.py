# 키보드에서 직원번호와 이름을 각각 입력 받아 해당 직원이 있으면 로그인이 되었다 가정하고 직원번호, 직원명, 부서명, 부서전화, 직급, 성별을 출력하고
# 해당 직원이 없으면 로그인 실패라는 에러 메시지 출력
import MySQLdb
import pickle

with open('mariaDB.dat', 'rb') as obj:
    config = pickle.load(obj)

def searchFunc():
    try:
        conn = MySQLdb.connect(**config) # dict 타입은 ** 써줘야 데이터들 다 넘어감
        cur = conn.cursor()
        
        jikwon_no = input('직원번호를 입력하세요 : ')
        jikwon_name = input('이름을 입력하세요 : ')
        sql = "select jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_jik, jikwon_gen\
         from jikwon, buser\
         where jikwon.buser_num=buser.buser_no and jikwon_no = {} and jikwon_name = '{}'" .format(jikwon_no, jikwon_name)
        cur.execute(sql)
        datas = cur.fetchall()
        
        if len(datas) == 0:
            print('로그인에 실패하였습니다. 다시 정확한 정보를 입력하세요.')
        
        for i in datas:
            for j in range(6):
                print(i[j], end = ' ')
            print()
                
    except Exception as e:
        print('error : ', e)

    finally:
        cur.close()
        conn.close()
        
if __name__ == '__main__':
    searchFunc()
    
