import requests
import json

grafana_url = "a5c07bf2eeabc479f99071aaddbac98b-364804466.ap-south-1.elb.amazonaws.com"
username = "admin"
password = "prom-operator"

base_url = "http://{}:{}@{}".format(username, password, grafana_url)

headers = {
    'Authorization': 'Bearer eyJrIjoiN0xNM1V4UWpMUkVoZXRKaWh2bVJya3IzZGNqb0dvTGkiLCJuIjoiQWRtaW4iLCJpZCI6MX0=',
    'Content-Type': 'application/json',
    'Accept': "application/json"
}

json_data = {
  "GroupByStr": [
                "grafana_folder",
                "alertname"
  ],  
  "Receiver":  "grafana-default-email",
  "routes" : [
    {
            "receiver": "slack-alerts",
            "group_by": [
                "grafana_folder",
                "alertname"
            ],
            "object_matchers": [
                [
                    "severity",
                    "=",
                    "warning"
                ]
            ],
            "continue": True,
            "group_wait": "10s",
            "group_interval": "10s",
            "repeat_interval": "10s"
        }
  ],
}

# objectmatchers type is written as ["name","type","value"]
# where type means operator and has following inputs: 
# 0 = MatchEqual, 1 = MatchNotEqual, 2 = MatchRegexp, 3 = MatchNotRegexp


resp = requests.put(base_url + "/api/v1/provisioning/policies",headers=headers, json=json_data, verify=False)
# resp = requests.post(base_url + "/api/alert-notifications",headers=headers, json=json_data, verify=False) this is for legacy
print(json.dumps(resp.json(), indent=4))

