import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cma_collection_data_dropped_columns.csv')

target_array = df.loc[1, 'artist_tags']
print(f'The arrray in the first row is: {target_array}')

specific_element = target_array[1]
print(f'The second element of that array is: {specific_element}')