import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"
data = {
    'name':'Zuyairia Nazi',
    'roll':1,
    'city':'Barishal'
}

json_data = json.dumps(data)
r = requests.post(url = URL,data = json_data)

data = r.json()
print(data)
