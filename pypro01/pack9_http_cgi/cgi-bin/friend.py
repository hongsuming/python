import cgi

dto = cgi.FieldStorage()
name = dto['name'].value
phone = dto['phone'].value
gender = dto['gender'].value

if gender == '남':
    gender = 'M'
else:
    gender = 'F'

print('Content-type : text/html; charset=utf-8\n')
print("""
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Insert title here</title>
    </head>
    <body>
        <h2>친구 정보</h2>
        이름은 {0} <br> 전화번호는 {1} <br> 성별은 {2} <br>
        <a href='../index.html'>메인으로</a>
    </body></html>
""" .format(name, phone, gender))