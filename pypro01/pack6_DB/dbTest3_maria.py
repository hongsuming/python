# 원격 데이터베이스 연동 프로그래밍 : MariaDB
import MySQLdb

"""
conn = MySQLdb.connect(host='127.0.0.1', user = 'root', password='123', database='test', port=3306)
print(conn)
conn.close
"""

# dict 타입으로 연결 정보 만들기
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
} 

try: 
    conn = MySQLdb.connect(**config) # dict 타입은 ** 써줘야 데이터들 다 넘어감
    cur = conn.cursor()
    
    # tuple이라 그냥 $s, '5'로 삭제가 안 되면 cur.execute(sql, (sql_delete_data,))로 해주면 됨
    
    """
    # 자료 삭제
    sql = "delete from sangdata where code=%s"
    sql_delete_data = '5'
    result = cur.execute(sql, sql_delete_data)
    if result == 0:
        print('삭제된 자료가 없습니다.')
    else:
        print(result, '개 행이 삭제되었습니다.')
    conn.commit()
    
    
    # 자료 수정
    sql = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"
    sql_update_data = ('가죽목도리', 7, 10000, 5) 
    result = cur.execute(sql, sql_update_data)
    print(result, '개 행이 수정되었습니다.')
    conn.commit()
    
    # 자료 추가
    sql = "insert into sangdata values(%s, %s, %s, %s)"
    sql_input_data = ('5', '목도리', '15', '7000') # 숫자는 ''안에 써도 되고 안 써도 됨
    cur.execute(sql, sql_input_data)
    conn.commit()
    """
    
    # 자료 읽기
    sql = "select * from sangdata"
    cur.execute(sql)
    for i in cur.fetchall():
        print('%s %s %s %s' %i)
        
    # for i in cur:
    #     print(i[0], i[1], i[2], i[3])
        
    # for (code, sang, su, dan) in cur:
    #     print(code, sang, su, dan)
    
    # for (a, b, c, d) in cur:
    #     print(a, b, c, d)
        
except Exception as e:
    print('error : ', e)
    conn.rollback()
    
finally:
    cur.close()
    conn.close()