import requests

# response = requests.get("http://randomfox.ca/floof")
# print(response.status_code)
# print(response.text)
# print(response.json())
# fox = response.json()
# print(fox['image'])

response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
print(response.status_code)