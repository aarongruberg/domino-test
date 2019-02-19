# Example of kicking off a run in cloud prod from Domino API
# This starts a run of a script 'knowledgeGraphAPI.py' which calls
# a google api to find the url for a given company.  This script
# lives in an imported repo in my project 'repo-from-api-46093'
# This is a python 2 example

import requests

values = {
    "command": [
      "/repos/Google_Knowledge_Graph_SearchAPI/knowledgeGraphAPI.py"
    ],
     "isDirect": False
  }

headers = {
    'Content-Type': 'application/json',
    'X-Domino-Api-Key': 'API-KEY'  
    } 

r = requests.post('https://app.dominodatalab.com/v1/projects/domino-aaron/repo-from-api-46093/runs', json = values, headers=headers)
print r.json()




# This request will start a file 'test.py' in my quick-start project
# The value for "command" should be the filepath, in this example
# the file is in the root of the project files folder

from urllib2 import Request, urlopen

values = """{
    "command": [
      "test.py"
    ],
     "isDirect": false
  }"""

headers = {
    'Content-Type': 'application/json',
  'X-Domino-Api-Key': 'API-KEY'
}

request = Request('https://app.dominodatalab.com/v1/projects/domino-aaron/quick-start/runs', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body