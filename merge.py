# # # # # # import os
# # # # # # import pandas as pd

# # # # # # # Path to the directory containing CSV files
# # # # # # directory = '/home/khattak/Downloads/A3/allcsv'

# # # # # # # Read CSV files
# # # # # # genres = pd.read_csv(os.path.join(directory, 'genres.csv'))
# # # # # # raw_albums = pd.read_csv(os.path.join(directory, 'raw_albums.csv'))

# # # # # # # Merge genres and raw_albums DataFrames
# # # # # # merged_df = pd.merge(genres, raw_albums, left_on='genre_id', right_on='album_id', how='outer')

# # # # # # # Save merged DataFrame to a single CSV file
# # # # # # merged_df.to_csv(os.path.join(directory, 'm11.csv'), index=False)

# # # # # import pandas as pd

# # # # # # Read m11.csv
# # # # # m11 = pd.read_csv("/home/khattak/Downloads/A3/allcsv/m11.csv")

# # # # # # Read raw_genres.csv
# # # # # raw_genres = pd.read_csv("/home/khattak/Downloads/A3/allcsv/raw_genres.csv")

# # # # # # Merge the two DataFrames on 'genre_id'
# # # # # merged_df = pd.merge(m11, raw_genres, on='genre_id', how='inner')

# # # # # # Save the merged DataFrame to a CSV file
# # # # # merged_df.to_csv("/home/khattak/Downloads/A3/allcsv/m22.csv", index=False)

# # # # # # Print a message indicating the file has been saved
# # # # # print("Merged file saved as m22.csv")

# # # # import pandas as pd

# # # # # Read m22.csv
# # # # m22 = pd.read_csv("/home/khattak/Downloads/A3/allcsv/m22.csv")

# # # # # Read raw_tracks.csv
# # # # raw_tracks = pd.read_csv("/home/khattak/Downloads/A3/allcsv/raw_tracks.csv")

# # # # # Merge the two DataFrames on 'album_id'
# # # # merged_df = pd.merge(m22, raw_tracks, on='album_id', how='inner')

# # # # # Save the merged DataFrame to a CSV file
# # # # merged_df.to_csv("/home/khattak/Downloads/A3/allcsv/m33.csv", index=False)

# # # # # Print a message indicating the file has been saved
# # # # print("Merged file saved as m22_raw_tracks_merged.csv")


# # # import pandas as pd

# # # # Read m33.csv, specify data types to address DtypeWarnings
# # # m33 = pd.read_csv("/home/khattak/Downloads/A3/allcsv/m33.csv", dtype={'column_name': str})

# # # # Read raw_artists.csv, specify data types to address DtypeWarnings
# # # raw_artists = pd.read_csv("/home/khattak/Downloads/A3/allcsv/raw_artists.csv", dtype={'column_name': str})

# # # # Merge the two DataFrames on 'artist_id'
# # # merged_df = pd.merge(m33, raw_artists, on='artist_id', how='inner')

# # # # Save the merged DataFrame to a CSV file
# # # merged_df.to_csv("/home/khattak/Downloads/A3/allcsv/m44.csv", index=False)

# # # # Print a message indicating the file has been saved
# # # print("Merged file saved as m33_raw_artists_merged.csv")


# # import pandas as pd

# # # Read raw_echonest.csv
# # raw_echonest_df = pd.read_csv("/home/khattak/Downloads/A3/allcsv/raw_echonest.csv")

# # # Display the first 5 entries of the DataFrame
# # print(raw_echonest_df.head())


# data = """
# ,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,
# echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,
# echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,
# echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,
# echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,
# echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,
# echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,
# echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,
# echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,
# echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest
# ,audio_features,audio_features,audio_features,audio_features,audio_features,audio_features,audio_features,audio_features,
# metadata,metadata,metadata,metadata,metadata,metadata,metadata,ranks,ranks,ranks,ranks,ranks,social_features,social_features,
# social_features,social_features,social_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,
# temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features
# ,acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence,album_date,album_name,artist_latitude,
# artist_location,artist_longitude,artist_name,release,artist_discovery_rank,artist_familiarity_rank,artist_hotttnesss_rank,
# song_currency_rank,song_hotttnesss_rank,artist_discovery,artist_familiarity,artist_hotttnesss,song_currency,song_hotttnesss
# """

# # Split the data into a list
# data_list = data.split(",")

# # Initialize lists for echonest, temporal_features, and other words
# list1 = []
# list2 = []
# list3 = []

# # Iterate through the data list
# for item in data_list:
#     if item == "echonest":
#         list1.append(item)
#     elif item == "temporal_features":
#         list2.append(item)
#     elif item.strip() != "":
#         list3.append(item.strip())

# # Print the lists
# print("List 1 (echonest):", list1)
# print("List 2 (temporal_features):", list2)
# print("List 3 (other unique words):", list3)


# # Size and length of all three lists
# size_list1 = len(list1)
# size_list2 = len(list2)
# size_list3 = len(list3)

# length_list1 = len(set(list1))  # Length of unique elements in list1
# length_list2 = len(set(list2))  # Length of unique elements in list2
# length_list3 = len(set(list3))  # Length of unique elements in list3

# print("Size of List 1 (echonest):", size_list1)
# print("Length of List 1 (unique elements):", length_list1)
# print()
# print("Size of List 2 (temporal_features):", size_list2)
# print("Length of List 2 (unique elements):", length_list2)
# print()
# print("Size of List 3 (other unique words):", size_list3)
# print("Length of List 3 (unique elements):", length_list3)

import pandas as pd

# Load the CSV file
df = pd.read_csv("/home/khattak/Downloads/A3/allcsv/raw_echonest.csv")

# Remove null values based on the "album" column
df = df.dropna()

# Remove duplicates

# Save the preprocessed data to a new CSV file
df.to_csv("praw_echonest.csv", index=False)

print("Preprocessing complete. Preprocessed data saved as preprocessed_a.csv")
