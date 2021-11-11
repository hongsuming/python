import pickle
import MySQLdb

with open('mariaDB.dat', 'rb') as obj:
    config = pickle.load(obj)
    
print('Content-Type:text/html;charset=utf-8\n')
print('<html><body>')
print('<h2>상품 정보</h2>')
print('<table border="1">')
print('<tr><th>코드</th><th>상품명</th><th>수량</th><th>단가</th></tr>')
try:
    conn = MySQLdb.connect(**config)
    cur = conn.cursor()
    cur.execute("select * from sangdata")
    datas = cur.fetchall()
    for code, sang, su, dan in datas:
        print("""
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            """ .format(str(code), sang, su, dan))
except Exception as e:
    print('error : ', e)
finally:
    cur.close()
    conn.close()
print('</table>')
print('</body></html>')