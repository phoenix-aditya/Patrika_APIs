import requests

str = "ass boobs"
response = requests.get("https://patrika-api.herokuapp.com/"+"cussword-filter/"+str)
print(response)
