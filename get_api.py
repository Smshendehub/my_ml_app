import requests

response = requests.get("https://api.agify.io?name=saurabh")
print(response.json())
