import requests
import pandas as pd

api_url = "https://openaccess-api.clevelandart.org/api/artworks/?female_artists&created_after=2000&limit=1000"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    # df = pd.DataFrame(data)
    df = pd.json_normalize(data)
    df.to_csv('cma_collection_data.csv')
    print(df.head())
else:
    print(f"Failed to fetch data: {response.status_code}")