from flask import Flask, abort
from flask import request
import http.server
import json
app = Flask(__name__)
print (app)
empDB= "index.html"

@app.route("/")
@app.route("/index")
def hello():
    with open(empDB, "r") as f:
        archivo = f.read()
    return archivo
@app.route("/listCompanies",methods=['GET'])
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
        archivo+= "<li>{}.".format(name)
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
                         <p>nombres.</p>
                        </body>
                    </html>
                    """
    limit = repos["meta"]["results"]["limit"]
    print(limit)
    for i in range(0, limit ):
        try:
            name = repos["results"][i]["openfda"]["generic_name"]
        except:
            name = "desconocido"
        archivo += "<li>{}.\n".format(name)
    return archivo
@app.route("/searchDrug")
def getDrugs():
    droga= request.args.get('active_ingredient')
    if request.args.get('limit'):
        limite = request.args.get('limit')
    else:
        limite= 10
    headers = {'User-Agent': 'http-client'}
    print(droga)
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?search=active_ingredient:"+droga+"&limit="+str(limite), None, headers)
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
            proposito = repos["results"][i]["purpose"]
        except:
            name = "desconocido"
        archivo += "<li>{}. {}.\n".format(id,proposito)
    return archivo
@app.route("/searchCompany")
def getCompanies():
    company = request.args.get('company')
    if request.args.get('limit'):
        limite = request.args.get('limit')
    else:
        limite= 10
    headers = {'User-Agent': 'http-client'}
    print(company, limite)
    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET", "/drug/label.json?search=openfda.manufacturer_name:"+company+"&limit="+str(limite), None, headers)
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
        archivo += "<li>{}.\n".format(name)
    return archivo
@app.route("/listWarnings")
def listWarnings():
    limite = request.args.get('limit')
    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection("api.fda.gov")
    conn.request("GET","/drug/label.json?limit="+str(limite), None,headers)
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
            nombre = repos["results"][i]["openfda"]["generic_name"]
        except:
            nombre = "medicamento desconocido"
        try:
            advertencia = repos["results"][i]["warnings"]
        except:
            advertencia= "advertencia desconocida"
        archivo+= "<li>{}. {}.\n".format(nombre ,advertencia)
    return archivo
    # Esta línea no se ejecuta
# Esta funcion evita la entrada del cliente al servidor, parando la comunicación


@app.route("/secret")
def secret():
    abort(401)
@app.route("/redirect")
def redirect():
    return "", 302, {'location': 'http://localhost:8000'}#te devuelve a la url propuesta
# Te redirige a la url puesta
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
