# 네트워크를 위한 통신 채널 - socket(TCP/IP 프로토콜의 프로그래머 인터페이스)으로 제공
import socket

print('기본적인 포트 번호')
print(socket.getservbyname('http', 'tcp')) # 80
print(socket.getservbyname('telnet', 'tcp')) # 23
print(socket.getservbyname('ftp', 'tcp')) # 21
print(socket.getservbyname('smtp', 'tcp')) # 25
print(socket.getservbyname('pop3', 'tcp')) # 110

print()
print(socket.getaddrinfo('www.naver.com', 80, proto = socket.SOL_TCP)) # [(<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.195.95', 80)), (<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.195.200', 80))]
