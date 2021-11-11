a1 = '자료1'
a2 = '두번째 자료'
a3 = 123

print('Content-type : text/html; charset=utf-8\n')
print("""
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Insert title here</title>
    </head>
    <body>
        <img src="../images/logo.png"><br>
        <hr>
        <h2>world.py 입니다.</h2><br>
        자료 출력 : {0}, {1}, {2}<br>
        <a href='../index.html'>메인으로</a>
    </body></html>
""" .format(a1, a2, a3))