#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler
import socketserver
import re

PORT = 8080

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = re.sub(r'^/([a-z]+)/$', r'\1.html', self.path)
        SimpleHTTPRequestHandler.do_GET(self)

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
