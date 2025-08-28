import requests
import pandas as pd

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

""" count = 1
while count < 20:
    response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(count))
    object = response.json()
    print("Title: " + object['title'])
    count += 1; """

# api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

# try: 
#     response = requests.get(api_url)
#     response.raise_for_status()
#     data = response.json()
#     print("Successfully retrieved data!")
#     print(data)
# except requests.exceptions.RequestException as e:
#     print(f"Error fetching data: {e}")

api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print(df.head())
else:
    print(f"Failed to fetch data: {response.status_code}")
