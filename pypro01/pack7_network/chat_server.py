# 채팅 서버 : 여러 개의 클라이언트와 소켓 통신을 스레드로 운영
import socket
import threading

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(('127.0.0.1', 5555))
serverSock.listen(5)
print('chatting service start ...')
users = [] # 채팅에 참여하는 클라이언트 기억 장소

def chatUser(conn):
    name = conn.recv(1024) # 채팅 아이디 받기
    data = '^^ ' + name.decode('utf-8') + '님 입장 ^^;' # 입장
    print(data) # 서버에 출력 (확인용)
    
    try:
        for i in users:
            i.send(data.encode('utf-8')) # 보낼 땐 encode
            
        while True: # 접속 상태에서 수다 떨기
            msg = conn.recv(1024) # 채팅 메세지 받기
            data = name.decode('utf-8') + '님 메세지 : ' + msg.decode('utf-8')
            print('메세지 내용 : ', data) # 서버에 출력 (확인용)
            for i in users:
                i.send(data.encode('utf-8')) # 보낼 땐 encode
            
    except:
        users.remove(conn)
        data = 'TT ' + name.decode('utf-8') + '님 퇴장 TT;' # 퇴장
        print(data) # 서버에 출력 (확인용)
        if users:
            for i in users:
                i.send(data.encode('utf-8')) # 보낼 땐 encode
        else:
            print('exit')
            
while True:
    conn, addr = serverSock.accept() # client가 connect 하면 aceept() 실행 됨
    users.append(conn)
    th = threading.Thread(target=chatUser, args=(conn,))
    th.start()