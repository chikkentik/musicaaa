import requests
import argparse

parser= argparse.ArgumentParser(description= "input patient info")
parser.add_argument('--gender')
parser.add_argument('--year')
parser.add_argument('--symptoms')
args= parser.parse_args()


url = "https://priaid-symptom-checker-v1.p.rapidapi.com/diagnosis"
headers = {
    'x-rapidapi-host': "priaid-symptom-checker-v0.p.rapidapi.com",
    'x-rapidapi-key': "e8e82ff66bmsh2353f291af944f0p1f8063jsn60d6c57e9d77"
    }
querystring = {"symptoms": args.symptoms,"gender": args.gender,"year_of_birth": args.year,"language":"en-gb"}
response = requests.request("GET", url, headers=headers, params=querystring)

# sx list
sx_list = response.json()

# passing through list with sx and code AND the sx name that you inputed
# for every item in sx_list

def find_sxcode(sx_list, symp_name):
    for sx in sx_list:
        if sx["Name"] == symp_name:
            print("Found code: ", sx["ID"])

find_sxcode(sx_list, args.symptoms)
for i in response.json():
    print(i["Issue"]["Name"])


