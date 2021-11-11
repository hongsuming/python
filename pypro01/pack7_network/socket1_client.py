# client 소스
from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8888)) # 서버에서 바인딩한 주소로 접속 시도 (connect가 있어야 server가 accept()를 실행)
clientSock.send('안녕 반가워!!!'.encode(encoding='utf-8', errors='static'))
clientSock.close()