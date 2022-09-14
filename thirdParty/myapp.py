import requests
import json

URL = 'http://127.0.0.1:8000/stuinfo/'

req = requests.get(url=URL)

data = req.json()

print(data)

URL_SEND = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name': 'Murtaza',
    'roll': 60,
    'city':'lahore'
}

json_data = json.dumps(data)

req = requests.post(url=URL_SEND, data=json_data)