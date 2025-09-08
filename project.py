import requests
import pandas as pd
import os

# Collection script for full CMA dataset.
""" csv_url = "https://media.githubusercontent.com/media/ClevelandMuseumArt/openaccess/refs/heads/master/data.csv"

response = requests.get(csv_url)

if response.status_code == 200:
    with open("full_cma_collection_data.csv", "wb") as f:
        f.write(response.content)
    print("CSV successfully written.")
else:
    print(f"Failed to write CSV. Status code: {response.status_code}") """

# Write full CMA dataset to CSV, convert CSV to DataFrame, modify DataFrame in place (drop columns), and use the os module to delete files.
csv_url = "https://media.githubusercontent.com/media/ClevelandMuseumArt/openaccess/refs/heads/master/data.csv"

response = requests.get(csv_url)

if response.status_code == 200:
    with open("full_cma_collection_data.csv", "wb") as f:
        f.write(response.content)
    print("CSV successfully written.")
else:
    print(f"Failed to write CSV. Status code: {response.status_code}")

df = pd.read_csv('full_cma_collection_data.csv')
# print(df.head)
df.to_csv('full_cma_collection_data_as_dataframe.csv')
# Get just the artists_tags field.
# df_modified = df.drop(['id', 'accession_number' ,'share_license_status','tombstone', 'current_location', 'title', 'title_in_original_language', 'series', 'series_in_original_language','creation_date','creation_date_earliest', 'creation_date_latest', 'culture', 'technique', 'support_materials', 'department', 'collection', 'type', 'measurements', 'state_of_the_work', 'edition_of_the_work', 'copyright', 'inscriptions', 'exhibitions', 'provenance', 'find_spot', 'related_works', 'former_accession_numbers', 'did_you_know', 'description', 'external_resources', 'citations', 'catalogue_raisonne', 'url', 'alternate_images', 'creditline', 'sketchfab_id','sketchfab_url', 'gallery_donor_text', 'creators', 'image_web', 'image_print', 'image_full', 'updated_at'], axis = 1)
# Get the title and artists_tags fields. (Requires backspace on CSV line 13001 for data cleaning.)
df_modified = df.drop(['id', 'accession_number' ,'share_license_status','tombstone', 'current_location', 'title_in_original_language', 'series', 'series_in_original_language','creation_date','creation_date_earliest', 'creation_date_latest', 'culture', 'technique', 'support_materials', 'department', 'collection', 'type', 'measurements', 'state_of_the_work', 'edition_of_the_work', 'copyright', 'inscriptions', 'exhibitions', 'provenance', 'find_spot', 'related_works', 'former_accession_numbers', 'did_you_know', 'description', 'external_resources', 'citations', 'catalogue_raisonne', 'url', 'alternate_images', 'creditline', 'sketchfab_id','sketchfab_url', 'gallery_donor_text', 'creators', 'image_web', 'image_print', 'image_full', 'updated_at'], axis = 1)

df_modified.to_csv('cma_collection_data_dropped_columns.csv', index="False")
print("Modified DataFrame in place, dropped columns.")

# Delete CSV files not in use.
file_to_delete_1 = "full_cma_collection_data.csv"
file_to_delete_2 = "full_cma_collection_data_as_dataframe.csv"

if os.path.exists(file_to_delete_1):
    try:
        os.remove(file_to_delete_1)
        print(f"File '{file_to_delete_1}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting file '{file_to_delete_1}': {e}")
else:
    print(f"File '{file_to_delete_1}' does not exist.")

if os.path.exists(file_to_delete_2):
    try:
        os.remove(file_to_delete_2)
        print(f"File '{file_to_delete_2}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting file '{file_to_delete_2}': {e}")
else:
    print(f"File '{file_to_delete_2}' does not exist.")
