#!/usr/bin/python3
#python version 3.7+  (run from the web/ folder: python https.py)
#Then open https://localhost:8088/ and accept the self-signed certificate.
import http.server
import ssl

server_address = ('0.0.0.0', 8088)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
# ssl.wrap_socket() was removed in Python 3.12; use SSLContext instead.
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('localhost.pem')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()