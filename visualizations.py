import pandas as pd
import matplotlib.pyplot as plt
import colorama 
from colorama import Fore

colorama.init(autoreset = True)

# The current total count of artwork records in the CMA's collection. 
total_art_pieces = 68076

# Counts of artworks belonging to various "artists_tags" (identities).
male_artist_count = 0
female_artist_count = 0
gender_unknown_artist_count = 0
asian_artist_count = 0
asian_american_artist_count = 0
jewish_artist_count = 0
latine_and_hispanic_artist_count = 0
lgbtq_artist_count = 0
black_american_artist_count = 0

# Read cleaned CMA CSV to a DataFrame for use.
df = pd.read_csv("cma_collection_data_cleaned.csv")

# Traverse DataFrame and tally instances of each artists_tags. 
row = 0
while row < 68075:
    # Access artists_tags to save to an array.
    artist_tag_array = df.loc[row, "artists_tags"]
    # Split artists_tags array to obtain each tag.
    separated_array = artist_tag_array.split(",")

    # Increase counts of any applicable categories. 
    if any("male" in item for item in separated_array):
        male_artist_count += 1
    if any("female" in item for item in separated_array):
        female_artist_count += 1
    if any("gender unknown" in item for item in separated_array):
        gender_unknown_artist_count += 1
    if any("Asian (from 1900 to present)" in item for item in separated_array):
        asian_artist_count += 1
    if any("Asian American" in item for item in separated_array):
        asian_artist_count += 1
    if any("Jewish" in item for item in separated_array):
        jewish_artist_count += 1
    if any("Latine and Hispanic Artists" in item for item in separated_array):
        latine_and_hispanic_artist_count += 1
    if any("LGBTQ+ (after 1900)" in item for item in separated_array):
        lgbtq_artist_count += 1
    if any("Black American Artists" in item for item in separated_array):
        black_american_artist_count += 1

    row += 1

# Print artist_tags totals to the terminal.
print(Fore.BLACK + "Male Artist Count: " + Fore.BLUE + f"{male_artist_count}")
print(Fore.BLACK + "Female Artist Count: " + Fore.BLUE + f"{female_artist_count}")
print(Fore.BLACK + "Gender Unknown Artist Count: " + Fore.BLUE + f"{gender_unknown_artist_count}")
print(Fore.BLACK + "Asian Artist Count: " + Fore.BLUE + f"{asian_artist_count}")
print(Fore.BLACK + "Asian American Artist Count: " + Fore.BLUE +f"{asian_american_artist_count}")
print(Fore.BLACK + "Jewish Artist Count: " + Fore.BLUE + f"{jewish_artist_count}")
print(Fore.BLACK + "Latine and Hispanic Artist Count: " + Fore.BLUE + f"{latine_and_hispanic_artist_count}")
print(Fore.BLACK + "LGBTQ+ Artist Count: " + Fore.BLUE+ f"{lgbtq_artist_count}")
print(Fore.BLACK + "Black American Artist Count: " + Fore.BLUE + f"{black_american_artist_count}")

# Pie chart displaying info for artist genders.
gender_tag_names = ["Male",
                    "Female",
                    "Gender Unkown"]

gender_tag_counts = [male_artist_count,
                     female_artist_count,
                     gender_unknown_artist_count]

with plt.style.context("Solarize_Light2"):
    plt.pie(gender_tag_counts, labels = gender_tag_names, autopct = "%1.1f%%", wedgeprops = {"linewidth": .75, "edgecolor": "#EEE8D5"})
    plt.legend(title = "Gender", loc = "lower left")
    plt.axis("equal")
    plt.title("Pieces in the Cleveland Museum of Art's Collection by Artist Gender", fontsize = 14)
    plt.show()

# Bar chart displaying info for artist ethnicities.
ethnicity_tag_names = ["Asian",
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

with plt.style.context("Solarize_Light2"):
    plt.bar(ethnicity_tag_names, ethnicity_tag_counts)
    plt.xlabel("Ethnicity", labelpad = 20, fontsize = 14)
    plt.xticks(fontsize = 10)
    plt.ylabel("Artist Count", labelpad = 20, fontsize = 14)
    plt.yticks(fontsize = 10)
    plt.title("Artist Ethnicity vs. Number of Artists", fontsize = 14)
    plt.tight_layout()
    plt.show()

# Pie chart displaying info for LGBTQ+ artists.
lgbtq_tag_names = ["LGBTQ+ (After 1900)",
                   "Not LGBTQ+"]

not_lgbtq_count = total_art_pieces - lgbtq_artist_count

lgbtq_tag_counts = [lgbtq_artist_count,
                    not_lgbtq_count]

with plt.style.context("Solarize_Light2"):
    plt.pie(lgbtq_tag_counts, labels = lgbtq_tag_names, autopct = "%1.1f%%", wedgeprops = {"linewidth": .75, "edgecolor": "#EEE8D5"})
    plt.legend(loc = "lower left")
    plt.axis("equal")
    plt.title("Pieces in the Cleveland Museum of Art's Collection by LGBTQ+ Artists", fontsize = 14)
    plt.show()

# Bar chart displaying info for Jewish artists.
jewish_tag_names = ["Jewish",
                   "Not Jewish"]

not_jewish_count = total_art_pieces - jewish_artist_count

jewish_tag_counts = [jewish_artist_count,
                    not_jewish_count]

with plt.style.context("Solarize_Light2"):
    plt.bar(jewish_tag_names, jewish_tag_counts)
    plt.xlabel("Jewish", labelpad = 20, fontsize = 14)
    plt.xticks(fontsize = 10)
    plt.ylabel("Artist Count", labelpad = 20, fontsize = 14)
    plt.yticks(fontsize = 10)
    plt.title("Jewish Artists vs. Number of Artists", fontsize = 14)
    plt.tight_layout()
    plt.show()