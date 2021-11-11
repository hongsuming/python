# 서버 서비스는 계속 진행
import socket
import sys

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 7777
try:
    serverSock.bind((HOST, PORT)) # ip 주소 안 주면 알아서 자기 ip 찾음
    serverSock.listen(5) # 동시 접속 최대 수 
    print('server start ...')
    
    while True:
        conn, addr = serverSock.accept()
        print('client info : ', addr[0], addr[1]) # addr[0] : 클라이언트 주소 / addr[1] : 클라이언트 포트번호
        # 메세지 수신
        print(conn.recv(1024).decode())
        
        # 메세지 송신
        conn.send('from server : 너도 잘 지내라~'.encode('utf-8'))
                  
except Exception as e:
    print('error : ', e)
    sys.exit()

finally:
    conn.close()
    serverSock.close()
    