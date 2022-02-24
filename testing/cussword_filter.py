import requests
import json

str = "ass boobs"
response = requests.get("http://patrika-api.herokuapp.com/cussword-filter/{article: str}?article=there%20is%20boobs%20and%20ass%20here")
print(response.json())
