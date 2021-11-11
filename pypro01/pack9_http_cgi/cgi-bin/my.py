import cgi

form = cgi.FieldStorage() # 사용자가 전송한 자료를 python에서 받기
name = form['name'].value # request.getParameter("name")
age = form['age'].value # request.getParameter("age")
print('Content-type : text/html; charset=utf-8\n')
print("""
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Insert title here</title>
    </head>
    <body>
        이름은 {0}, 나이는 {1} <br>
        <a href='../index.html'>메인으로</a>
    </body></html>
""" .format(name, age))