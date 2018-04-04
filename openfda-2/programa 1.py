import http.client
import json

headers = {'User-Agent': 'http-client'}

i=0
controlador= True
nombres=[]
while controlador:
    conn = http.client.HTTPSConnection("api.fda.gov")

    conn.request("GET", "/drug/label.json?search=openfda.substance_name:\"SALICYLIC ACID\"&skip="+ str(i) + "&limit=100", None, headers)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    repos_raw = r1.read().decode("utf-8")
    conn.close()

    repos = json.loads(repos_raw)
    for f in range(0,100):
        i+=1
        nombres.array(repos['results'][f]['openfda']['manufacturer_name'])
        if i == int(repos['meta']['results']['total']):
            controlador= False
            break

print(nombres)