import http.client
import json

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", '/drug/label.json?search=openfda.substance_name:"SALICYLIC ACID"&skip=1000&limit=100', None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()

repos = json.loads(repos_raw)
fabricates = ["lista de fabricantes"]
for i in range(0,99):
    print(repos['results'][i]['openfda']['manufacturer_name'])
#Corregir los nombres de los arrays pues son diferentes para cada numero