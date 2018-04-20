from flask import Flask
from flask import jsonify
from flask import request
import http.server
import socketserver
import json
app = Flask(__name__)
print (app)
empDB="""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>OpenFDA-project</title>
</head>
<body>

<form action = "/listDrugs" method="get">
  <input type="submit" value="Listar fármacos">
    Limite: <input type="text" name="limit" value="1">
</form>

<form action = "/ListCompanies" method="get">
  <input type="submit" value="Listar empresas">
</form>

<form action = "/SearchDrug" method="get">
  <input type="submit" value="Buscar fármaco">
    Campo: <input type="text" name="Principio activo" value="">
</form>

<form action = "/SearchCompany" method="get">
  <input type="submit" value="Buscar empresas">
    Campo: <input type="text" name="Nombre empresaa" value="">
</form>

</body>
</html>"""

@app.route("/")
def hello():
    return empDB
@app.route("/ListCompanies",methods=['GET'])
def getCompanies():
    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET","/drug/label.json?limit=10", None,headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    archivo = """
                <!doctype html>
                <html>
                    <body style='background-color: green' >
                     <p>nombres. tags.</p>
                    </body>
                </html>
                """
    for i in range(0, 10):
        try:
            name=repos["results"][i]["openfda"]["manufacturer_name"]
        except:
            name="desconocido"
        archivo+= "<li>{}.<li>\n".format(name)
    return archivo
@app.route("/listDrugs")
def getDrugs():
    limite = request.args.get('limit')
    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?limit="+limite, None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    archivo = """
                    <!doctype html>
                    <html>
                        <body style='background-color: green' >
                         <p>nombres. tags.</p>
                        </body>
                    </html>
                    """
    for i in range(0, repos["meta"]["results"]["limit"]):
        try:
            name = repos["results"][i]["openfda"]["generic_name"]
        except:
            name = "desconocido"
        archivo += "<li>{}.<li>\n".format(name)
    return archivo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
