import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
} 
def searchFunc():
    try:
        conn = MySQLdb.connect(**config)
        cur = conn.cursor()
        
        jikwon_jik = input('직원직급을 입력하세요 : ')
        sql = "select jikwon_no, jikwon_name, jikwon_jik, buser_num\
         from jikwon\
         where jikwon_jik = '{}'" .format(jikwon_jik)
        cur.execute(sql)
        datas = cur.fetchall()
   
        for i in datas:
            for j in range(4):
                print(i[j], end = ' ')
            print()
                
    except Exception as e:
        print('error : ', e)

    finally:
        cur.close()
        conn.close()
        
if __name__ == '__main__':
    searchFunc()
    
