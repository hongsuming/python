# HttpServer : 기본적인 소켓 연결을 관리
# SimpleHttpRequestHandler : 요청을 처리
from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 7777

handler = SimpleHTTPRequestHandler
server = HTTPServer(('127.0.0.1', port), handler)
print('web service start...')
server.serve_forever()
