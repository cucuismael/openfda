import http.server
import socketserver
import json

PORT = 8000

conn = http.client.HTTPConnection('localhost', PORT)
print (conn)
path= input()
conn.request("GET","/" + path)

r1 = conn.getresponse()
print (r1)
print(r1.status, r1.reason)

data1 = r1.read().decode("utf-8")
print(data1)
