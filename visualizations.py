import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cma_collection_data_cleaned.csv')

target_array = df.loc[0, 'artists_tags']
print(f'The arrray in the first row is: {target_array}')

specific_element = target_array[0]
print(f'The first element of that array is: {specific_element}')