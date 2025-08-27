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

# response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/437133")
# print(response.status_code)
# collection = response.json()

# title = collection['title']
# artistDisplayName = collection['artistDisplayName']
# accessionYear = collection['accessionYear']

# print("The accession year for " + artistDisplayName + "'s \"" + title + "\" is " + accessionYear + ".")

count = 1
while count < 20:
    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(count))
    object = response.json()
    print("Title: " + object['title'])
    count += 1;