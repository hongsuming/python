# client source

from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 7777)) # 서버에서 바인딩한 주소로 접속 시도 (connect가 있어야 server가 accept()를 실행)
clientSock.send('하이 반가워!!! 잘지내!!'.encode(encoding='utf-8', errors='static'))
re_msg = clientSock.recv(1024).decode()
print('수신된 자료 : ', re_msg)
clientSock.close()