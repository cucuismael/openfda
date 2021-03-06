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
    Limite: <input type="text" name="limit" value="1">
</form>

<form action = "/SearchDrug" method="get">
  <input type="submit" value="Buscar fármaco">
    Campo: <input type="text" name="active_ingredient" value="">
    Limite: <input type="text" name="limit" value="1">
</form>

<form action = "/SearchCompany" method="get">
  <input type="submit" value="Buscar empresas">
    Campo: <input type="text" name="company" value="">
    Limite: <input type="text" name="limit" value="1">
</form>

</body>
</html>"""

@app.route("/")
def hello():
    return empDB
@app.route("/ListCompanies",methods=['GET'])
def getAllCompanies():
    limite = request.args.get('limit')
    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET","/drug/label.json?limit="+limite, None,headers)
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
            name=repos["results"][i]["openfda"]["manufacturer_name"]
        except:
            name="desconocido"
        archivo+= "<li>{}.<li>\n".format(name)
    return archivo
@app.route("/listDrugs")
def getAllDrugs():
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
@app.route("/SearchDrug")
def getDrugs():
    droga= request.args.get('active_ingredient')
    limite = request.args.get('limit')
    headers = {'User-Agent': 'http-client'}
    print(droga, limite)
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?search=active_ingredient:"+droga+"&limit=1", None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()
    repos = json.loads(repos_raw)
    archivo = """
                        <!doctype html>
                        <html>
                            <body style='background-color: green' >
                             <p>id. purpose.</p>
                            </body>
                        </html>
                        """
    for i in range(0, repos["meta"]["results"]["limit"]):
        id= repos["results"][i]["id"]
        try:
            proposito = repos["results"][i]["openfda"]["generic_name"]
        except:
            name = "desconocido"
        archivo += "<li>{}. {}.<li>\n".format(id,proposito)
    return archivo
@app.route("/SearchCompany")
def getCompanies():
    company = request.args.get('company')
    limite = request.args.get('limit')
    headers = {'User-Agent': 'http-client'}
    print(company, limite)
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?search=openfda.manufacturer_name:"+company+"&limit="+limite, None, headers)
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
def getWarnings():
    limite = request.args.get('limit')
    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET","/drug/label.json?limit="+limite, None,headers)
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
            name=repos["results"][i]["openfda"]["manufacturer_name"]
        except:
            name="desconocido"
        archivo+= "<li>{}.<li>\n".format(name)
    return archivo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
