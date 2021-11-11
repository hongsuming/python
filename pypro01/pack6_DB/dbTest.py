# 데이터베이스 연동 프로그래밍
# 개인용 DBMS : sqlLite (파이썬 설치시 자동 등록. 기본 모듈(라이브러리)로 제공)
import sqlite3
print(sqlite3.sqlite_version)

print()
# conn = sqlite3.connect('exam.db') # db 파일 생성
conn = sqlite3.connect(':memory:') # ram 파일 생성 - 테스트용 

try:
    cur = conn.cursor() # SQL 처리 가능 객체 (자바에서 preparestatement와 동일)
    
    cur.execute('create table if not exists friends(name text, phone text, addr text)')
    cur.execute('insert into friends values("한국인", "111-1111-1111", "서울 강남구 역삼동")')
    cur.execute('insert into friends values("홍수민", "010-9456-9803", "서울 천호동")')
    inputData = ('김진석', '010-8353-9803', '인천 용현동')
    cur.execute('insert into friends values(?, ?, ?)', inputData)
    conn.commit()
    
    # select
    cur.execute('select * from friends') # select의 결과를 커서가 기억함
    # print(cur.fetchone()) # 결과 하나만 받기
    print(cur.fetchall())
    
except Exception as e:
    print('error : ', e)

finally:
    cur.close()
    conn.close()