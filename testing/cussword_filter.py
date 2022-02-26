import requests
import json

str = "ass boobs"
response = requests.get("http://patrika-api.herokuapp.com/cussword-filter/"+str)
print(response.json())

