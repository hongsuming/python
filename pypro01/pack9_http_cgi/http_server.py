# SimpleHttpRequestHandler를 확장한 CGIHTTPRequestHandler 클래스 사용
# 클라이언트의 정보를 받아 처리하고, py 파일을 호출 가능
from http.server import CGIHTTPRequestHandler, HTTPServer

port = 7878

class Handler(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin']
    
server = HTTPServer(('127.0.0.1', port), Handler)

print('web service start...')
server.serve_forever()