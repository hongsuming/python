import socket
import threading
import sys

def handleFunc(socket):
    while True:
        data = socket.recv(1024) # 서버가 넘겨주는 데이터
        if not data:
            continue
        print(data.decode('utf-8'))
        
sys.stdout.flush() # 버퍼 비우기

name = input('사용할 아이디를 입력하세요 : ')
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(('127.0.0.1', 5555)) # serverSock.bind(('127.0.0.1', 5555)) 서버와 주소, 포트번호를 같게 함
clientSock.send(name.encode('utf-8'))

th = threading.Thread(target=handleFunc, args=(clientSock,))
th.start()

while True:
    msg = input('msg : ')
    sys.stdout.flush()
    if not msg:
        continue
    else:
        clientSock.send(msg.encode('utf-8'))

clientSock.close()