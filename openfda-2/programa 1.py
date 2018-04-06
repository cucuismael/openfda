import http.client
import json

headers = {'User-Agent': 'http-client'}

i=0
controlador= True
nombres=[]

conn = http.client.HTTPSConnection("api.fda.gov")

conn.request("GET", '/drug/label.json?search=active_ingredient:acetylsalicylic&limit=100', None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()

repos = json.loads(repos_raw)
limite= int(repos['meta']['results']['total'])
print(limite)
for f in range(0, limite):
    if repos['results'][i]['openfda']['manufacturer_name'] not in nombres:
        nombres.append(repos['results'][i]['openfda']['manufacturer_name'])



print(nombres)