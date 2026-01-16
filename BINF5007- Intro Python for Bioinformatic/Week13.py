'''
Docstring for Week13
Final Exam
(part 1)
How to build and call functions
using conditional statments
using loops
how to use data structures (dict, list, tuples, strings, int, float, etc)
try/except structure
(part 2)
(part 3)
(part 4)
How to create a regex expression
Biopython, how to call different methods
How to read and write files (JSON, XML, csv, etc.)
'''
#using APIs
import requests
'''
url = "https://statsapi.mlb.com/api/v1/teams/141/roster"

response = requests.get(url)
data = response.json()

print(data)
'''

url = "https://api.restful-api.dev/objects"
payload = {"name":"Apple MacBook Pro 16",
           "date":{
                "year":2019,
                "price":1849.99,
                "CUP model":"Intel Core i9",
                "Hard Drive size": "1 TB"}
            }
response = requests.post(url, json=payload)
print(response.json)
print(response.status_code)