import requests
import argparse

parser= argparse.ArgumentParser(description= "input patient info")
parder.add_argument('--symptoms')

url = "https://priaid-symptom-checker-v1.p.rapidapi.com/diagnosis"


querystring = {"symptoms":"[59]","gender":"male","year_of_birth":"1984","language":"en-gb"}

headers = {
    'x-rapidapi-host': "priaid-symptom-checker-v1.p.rapidapi.com",
    'x-rapidapi-key': "e9e82ff66bmsh2353f291af944f0p1f8063jsn60d6c57e9d77"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

import json
print (json.dumps(response.json(), indent=2)

for i in response.json():
    print(i["Issue"]["Name"])
