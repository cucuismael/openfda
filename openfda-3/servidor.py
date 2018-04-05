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
        if "api" in self.path:
            headers = {'User-Agent': 'http-client'}

            conn = http.client.HTTPSConnection("api.fda.gov")
            conn.request("GET","/drug/label.json?search=_exists_:openfda.generic_name+AND+_exists_:openfda.brand_name&limit=10", None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)
            tag=[]
            name=[]
            for i in range(0,10):
                tag.array(repos['results'][i]['openfda']['brand_name'])
                name.array(repos['results'][i]['openfda']['generic_name'])

            filename="""
            """
        else:
            try:
                if self.path=="/":
                    filename = "green.html"
                else:
                    with open(self.path, "r") as f :
                        filename = f.read()
            except:
                filename="error.html"
        print("Fichero a servir: {}".format(filename))
        with open(filename, "r") as f:
            contenido = f.read()

        message = contenido

        self.wfile.write(bytes(message, "utf8"))
        print("File served!")
        return



Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
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