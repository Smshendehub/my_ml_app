import requests

url = "https://httpbin.org/post"
data = {"message": "Hello, API!"}

response = requests.post(url, json=data)
print(response.json())
