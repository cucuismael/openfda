import http.client
import json

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov")
conn.request("GET", "/drug/label.json?search=_exists_:purpose+AND+_exists_:openfda.manufacturer_name&limit=10", None, headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8")
conn.close()

repos = json.loads(repos_raw)

for i in range(0,10):
    print ("los datos del medicamento", i,"Son: Su id es: ",repos['results'][i]['id'],"usado en: ",repos['results'][i]['purpose'],"fabricado por:",repos['results'][i]['openfda']['manufacturer_name'])

