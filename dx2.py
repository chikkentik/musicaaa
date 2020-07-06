import requests
import argparse
import json

#defining arguments
parser= argparse.ArgumentParser(description= "input patient info")
parser.add_argument('--gender')
parser.add_argument('--year')
parser.add_argument('--symptoms')
args= parser.parse_args()

#getting sx code
url = "https://priaid-symptom-checker-v1.p.rapidapi.com/symptoms"
querystring = {"format":"json","language":"en-gb"}
headers = {
    'x-rapidapi-host': "priaid-symptom-checker-v1.p.rapidapi.com",
    'x-rapidapi-key': "e9e82ff66bmsh2353f291af944f0p1f8063jsn60d6c57e9d77"
    }
response = requests.request("GET", url, headers=headers, params=querystring)

# sx list
sx_list = response.json()

# passing through list with sx and code AND the sx name that you inputed
#for every item in sx_list

def find_sxcode(sx_list,symp_name ):
    for sx  in sx_list:
        if sx ["Name"]==symp_name:
            #print("Found code: ", sx["ID"])
            return sx["ID"]

sxid = find_sxcode(sx_list, args.symptoms)


#part two, get DDx

url = "https://priaid-symptom-checker-v1.p.rapidapi.com/diagnosis"

querystring = {"symptoms": "[{}]".format(sxid),"gender":"male","year_of_birth":"1984","language":"en-gb"}

headers = {
    'x-rapidapi-host': "priaid-symptom-checker-v1.p.rapidapi.com",
    'x-rapidapi-key': "e9e82ff66bmsh2353f291af944f0p1f8063jsn60d6c57e9d77"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
import json
u = response.json()
for i in u:
  print(i["Issue"]["Name"])

