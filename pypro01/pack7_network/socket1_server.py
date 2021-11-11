# 단순한 서버 구축 : 클라이언트의 요청에 1회만 반응
from socket import *

serverSock = socket(AF_INET, SOCK_STREAM) # socket(소켓종류, 소켓유형)
serverSock.bind(('127.0.0.1', 8888)) # 소켓을 컴퓨터 주소에 바인딩
serverSock.listen(1) # 1~5까지 가능 (클라이언트와의 연결 정보 수)
print('서버 서비스 시작..')

conn, addr = serverSock.accept()
print('client address : ', addr)

print('from client msg : ', conn.recv(1024).decode())

conn.close()
serverSock.close()