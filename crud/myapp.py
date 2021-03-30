import requests
import json

url = "http://127.0.0.1:8000/stucrt/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    return data


# print(get_data())

def post_data():
    data = {
        'name': "Ali Baba",
        'roll': 40,
        'city': "Iran",
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    data = r.json()
    return data


# post_data()


def update_data():
    data = {
        'id': 2,
        'name': "Rakib",
        'roll': 99,
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    return data


update_data()

# print(update_data())
