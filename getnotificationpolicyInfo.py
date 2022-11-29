import requests
import json

grafana_url = "a5c07bf2eeabc479f99071aaddbac98b-364804466.ap-south-1.elb.amazonaws.com"
username = "admin"
password = "prom-operator"

base_url = "http://{}:{}@{}".format(username, password, grafana_url)

headers = {
    'Authorization': 'Bearer eyJrIjoiMlViUENzNzZUZjVLUnpISjlMb3hrT2NaMXVUbGoxbzQiLCJuIjoiQWRtaW4iLCJpZCI6MX0=',
    'Content-Type': 'application/json',
    'Accept' : 'application/json'
}

# resp = requests.get('http://admin:admin@13.126.211.230:3000/api/admin/stats')
resp = requests.get(base_url + "/api/v1/provisioning/policies",headers=headers)
print(json.dumps(resp.json(), indent=4))

