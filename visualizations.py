import pandas as pd
import matplotlib.pyplot as plt

total_art_pieces = 68076

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
print(f"Black American artist count: {black_american_artist_count}")

# Bar chart displaying info for all artist identities.
""" tag_names = ["Male",
             "Female",
             "Gender Unkown",
             "Asian",
             "Asian American",
             "Jewish",
             "Latine and Hispanic",
             "LGBTQ+",
             "Black American"]

tag_counts = [male_artist_count,
              female_artist_count,
              gender_unknown_artist_count,
              asian_artist_count,
              asian_american_artist_count,
              jewish_artist_count,
              latine_and_hispanic_artist_count,
              lgbtq_artist_count,
              black_american_artist_count]

plt.bar(tag_names, tag_counts)
plt.xlabel("Identity")
plt.ylabel("Artist Count")
plt.title("Artist Identity vs. Number of Artists")
plt.show() """

# Bar chart displaying info for artist genders.
gender_tag_names = ["Male",
                    "Female",
                    "Gender Unkown"]

gender_tag_counts = [male_artist_count,
                     female_artist_count,
                     gender_unknown_artist_count]

with plt.style.context('Solarize_Light2'):
    plt.bar(gender_tag_names, gender_tag_counts)
    plt.xlabel("Gender", labelpad = 20, fontsize = 14)
    plt.xticks(fontsize = 10)
    plt.ylabel("Artist Count", labelpad = 20, fontsize = 14)
    plt.yticks(fontsize = 10)
    plt.title("Artist Gender vs. Number of Artists", fontsize = 14)
    plt.tight_layout()
    plt.show()

# Bar chart displaying info for artist ethnicity.
""" ethnicity_tag_names = ["Asian",
                       "Asian American",
                       "Latine and Hispanic",
                       "Black American",
                       "Other"]

other_ethnicity_count = total_art_pieces - asian_artist_count - asian_american_artist_count - latine_and_hispanic_artist_count - black_american_artist_count

ethnicity_tag_counts = [asian_artist_count,
                        asian_american_artist_count,
                        latine_and_hispanic_artist_count,
                        black_american_artist_count,
                        other_ethnicity_count]

plt.bar(ethnicity_tag_names, ethnicity_tag_counts)
plt.xlabel("Ethnicity")
plt.ylabel("Artist Count")
plt.title("Artist Ethnicity vs. Number of Artists")
plt.show() """

# Bar chart displaying info for LGBTQ+ artists.
""" lgbtq_tag_names = ["LGBTQ+ (After 1900)",
                   "Not LGBTQ+"]

not_lgbtq_count = total_art_pieces - lgbtq_artist_count

lgbtq_tag_counts = [lgbtq_artist_count,
                    not_lgbtq_count]

plt.bar(lgbtq_tag_names, lgbtq_tag_counts)
plt.xlabel("LGBTQ+")
plt.ylabel("Artist Count")
plt.title("LQBTQ+ Artists vs. Number of Artists")
plt.show() """

# Bar chart displaying info for Jewish artists.
""" jewish_tag_names = ["Jewish",
                   "Not Jewish"]

not_jewish_count = total_art_pieces - jewish_artist_count

jewish_tag_counts = [jewish_artist_count,
                    not_jewish_count]

plt.bar(jewish_tag_names, jewish_tag_counts)
plt.xlabel("Jewish")
plt.ylabel("Artist Count")
plt.title("Jewish Artists vs. Number of Artists")
plt.show() """