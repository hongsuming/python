# sqlite 사용
import sqlite3

def dbProcess(dbName):
    # print(dbName)
    try:
        conn = sqlite3.connect(dbName)
        cur = conn.cursor()
        
        cur.execute('drop table if exists jikwons') # 있는 테이블이면 삭제
        cur.execute('create table if not exists jikwons(id integer primary key, name text)') # 정수 : integer / 실수 : real
        
        # insert
        cur.execute('insert into jikwons values(1, "홍길동")')
        
        data = (2, '고길동') # tuple
        cur.execute('insert into jikwons values(?, ?)', data)
        
        listdata = [3, '둘리'] # list //// set type은 안 됨
        cur.execute('insert into jikwons values(?, ?)', listdata)
        
        dictdata = {'id':4, 'name':'또치'}
        cur.execute('insert into jikwons values(:id, :name)', dictdata) # dict는 순서가 없기 때문에 values에 key를 걸어줘야 함
        
        dictdata2 = {'sabun':5, 'irum':'도우너'}
        cur.execute('insert into jikwons values(:sabun, :irum)', dictdata2) # key가 컬럼명과 동일하지 않아도 됨
        
        conn.commit()
        
        # select
        cur.execute('select * from jikwons')
        for i in cur:
            print(str(i[0]) + ' ' + i[1])
            
        # cur.execute('select * from jikwons where id<=2')
        inputid = int(input('아이디를 입력하세요. : '))
        cur.execute('select * from jikwons where id=%d' %inputid)
        for i in cur.fetchall():
            print(str(i[0]) + ' ' + i[1])
            
        inputname = input('이름을 입력하세요. : ')
        cur.execute('select * from jikwons where name="%s"' %inputname)
        for i in cur.fetchall():
            print(str(i[0]) + ' ' + i[1])
            
        cur.execute('select count(*) from jikwons')
        # print('건수 : ' + str(cur.fetchone())) # 건수 : (5,)
        print('건수 : ' + str(cur.fetchone()[0])) # 건수 : 5
            
    except Exception as e:
        print('error : ', e)
        conn.rollback()
    
    finally:
        cur.close()
        conn.close()
    
if __name__ == '__main__':
    dbProcess('test.db')