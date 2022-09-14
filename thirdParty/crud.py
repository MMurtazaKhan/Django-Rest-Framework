import requests
import json


# URL = 'http://127.0.0.1:8000/api/stuget/' 
# URL = 'http://127.0.0.1:8000/api/stuAPI/'
# URL = 'http://127.0.0.1:8000/api/stuModelAPI/'
# URL = 'http://127.0.0.1:8000/api_two/stuAPIView/'
URL = 'http://127.0.0.1:8000/api_two/studentAPI'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
        json_data = json.dumps(data)
        headers = {'content-Type': 'application/json'}
        req = requests.get(url=URL,headers=headers, data=json_data)
        data = req.json()

        print(data)

# get_data()

def create_data():
    data = {
        'name': 'Khan',
        'roll': 40,
        'city': 'Lahore'
    }

    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    req = requests.post(url=URL, headers=headers, data=json_data)
    data = req.json()
    print(data) 

# create_data()

def update_data():
    data = {
        'id': 2,
        'name': 'Zahid',
        'roll': 100
    }

    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    req = requests.put(url=URL, data=json_data, headers=headers)
    data = req.json()
    print(data)


# update_data()

def delete_data(id = None):
    data = {}

    if id is not None:
        data = {'id': id}
        headers = {'content-Type': 'application/json'}
        json_data = json.dumps(data)
        req = requests.delete(url=URL, data=json_data, headers=headers)
        data = req.json()
        print(data)

delete_data(4)