import pandas as pd
import matplotlib.pyplot as plt

male_artist_count = 0
female_artist_count = 0
gender_unknown_artist_count = 0
asian_artist_count = 0
asian_american_artist_count = 0
jewish_artist_count = 0
latine_and_hispanic_artist_count = 0
lgbtq_artist_count = 0
black_american_artist_count = 0

df = pd.read_csv('cma_collection_data_cleaned.csv')

row = 0
while row < 68075:
    artist_tag_array = df.loc[row, 'artists_tags']
    #print(f'The array in row {row} is: {artist_tag_array}')
    separated_array = artist_tag_array.split(",")

    if any("male" in item for item in separated_array):
        male_artist_count = male_artist_count + 1
    if any("female" in item for item in separated_array):
        female_artist_count = female_artist_count + 1
    if any("gender unknown" in item for item in separated_array):
        gender_unknown_artist_count = gender_unknown_artist_count + 1
    if any("Asian (from 1900 to present)" in item for item in separated_array):
        asian_artist_count = asian_artist_count + 1
    if any("Asian American" in item for item in separated_array):
        asian_artist_count = asian_artist_count + 1
    if any("Jewish" in item for item in separated_array):
        jewish_artist_count = jewish_artist_count + 1
    if any("Latine and Hispanic Artists" in item for item in separated_array):
        latine_and_hispanic_artist_count = latine_and_hispanic_artist_count + 1
    if any("LGBTQ+ (after 1900)" in item for item in separated_array):
        lgbtq_artist_count = lgbtq_artist_count + 1
    if any("Black American Artists" in item for item in separated_array):
        black_american_artist_count = black_american_artist_count + 1

    row = row + 1

print(f"Male artist count: {male_artist_count}")
print(f"Female artist count: {female_artist_count}")
print(f"Gender unknown artist count: {gender_unknown_artist_count}")
print(f"Asian artist count: {asian_artist_count}")
print(f"Asian American artist count: {asian_american_artist_count}")
print(f"Jewish artist count: {jewish_artist_count}")
print(f"Latine and Hispanic artist count: {latine_and_hispanic_artist_count}")
print(f"LGBTQ+ artist count: {lgbtq_artist_count}")
print(f"Black Americna artist count: {black_american_artist_count}")
