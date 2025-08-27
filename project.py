import requests

# response = requests.get("http://randomfox.ca/floof")
# print(response.status_code)
# print(response.text)
# print(response.json())
# fox = response.json()
# print(fox['image'])

# response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
# print(response.status_code)
# collection = response.json()
# print(collection['objectID'])

response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/437133")
print(response.status_code)
collection = response.json()
# print(collection['title'])
# print(collection['artistDisplayName'])
# print(collection['acessionYear'])

title = collection['title']
artistDisplayName = collection['artistDisplayName']
accessionYear = collection['accessionYear']

print("The accession year for " + artistDisplayName + "'s \"" + title + "\" is " + accessionYear + ".")