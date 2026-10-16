# ============================================
# Lesson 2: Practice Exercise
# ============================================
# You are a data analyst for a fictional streaming service called StreamWave.
# Use what you learned to explore the data below!

import pandas as pd

# ---- THE DATA ----
streamwave = pd.DataFrame([
    [1, 'Inception', 'sci-fi', 2010, 8.8, 'English'],
    [2, 'Parasite', 'thriller', 2019, 8.6, 'Korean'],
    [3, 'The Crown', 'drama', 2016, 8.6, 'English'],
    [4, 'Dark', 'sci-fi', 2017, 8.8, 'German'],
    [5, 'Money Heist', 'thriller', 2017, 8.3, 'Spanish'],
    [6, 'Interstellar', 'sci-fi', 2014, 8.6, 'English'],
    [7, 'Squid Game', 'thriller', 2021, 8.0, 'Korean'],
    [8, 'The Witcher', 'fantasy', 2019, 7.2, 'English'],
    [9, 'Lupin', 'drama', 2021, 7.5, 'French'],
    [10, 'Stranger Things', 'sci-fi', 2016, 8.7, 'English'],
],
    columns=['id', 'title', 'genre', 'year', 'rating', 'language']
)

# ---- EXERCISES ----

# 1. Inspect the first 5 rows of the data
# print(???)

# 2. Check the data types and non-null counts
# print(???)

# 3. Select only the 'title' and 'rating' columns
# top_titles = ???

# 4. Select the 3rd row using iloc
# third_row = ???

# 5. Select all shows with a rating greater than 8.5
# highly_rated = ???

# 6. Select all shows that are either 'sci-fi' or 'fantasy'
# using isin()
# scifi_fantasy = ???

# 7. Select all Korean or Spanish language shows
# using | operator
# korean_spanish = ???

# 8. Select shows released in 2016 AND with a rating above 8.5
# using & operator
# new_and_great = ???

# 9. Reset the index of highly_rated (drop=True, inplace=True)
# ???

# ---- ANSWERS ----
# Uncomment to check your work!

# 1. print(streamwave.head())
# 2. print(streamwave.info())
# 3. top_titles = streamwave[['title', 'rating']]
# 4. third_row = streamwave.iloc[2]
# 5. highly_rated = streamwave[streamwave.rating > 8.5]
# 6. scifi_fantasy = streamwave[streamwave.genre.isin(['sci-fi', 'fantasy'])]
# 7. korean_spanish = streamwave[(streamwave.language == 'Korean') | (streamwave.language == 'Spanish')]
# 8. new_and_great = streamwave[(streamwave.year == 2016) & (streamwave.rating > 8.5)]
# 9. highly_rated.reset_index(drop=True, inplace=True)
