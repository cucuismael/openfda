import http.server
import socketserver
import json
PORT = 8000

class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        filename = ""
        if self.path == "/":
            filename = "green.html"
        else:
            if (self.path == "/blue"):
                filename = "blue.html"
            elif self.path == "/json":
                filename = "json.txt"
            else:
                filename = "pink.html"

        print("Fichero a servir: {}".format(filename))
        with open(filename, "r") as f:
            contenido = f.read()

        message = contenido

        self.wfile.write(bytes(message, "utf8"))
        print("File served!")
        return



Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("")
    print("Interrumpido por el usuario")

print("")
print("Servidor parado")
httpd.close()

# https://github.com/joshmaker/simple-python-webserver/blob/master/server.py