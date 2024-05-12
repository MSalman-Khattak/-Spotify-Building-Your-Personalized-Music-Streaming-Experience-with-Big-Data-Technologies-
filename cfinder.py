# # import pandas as pd

# # # Path to the CSV file
# # csv_file = '/home/khattak/Downloads/A3/allcsv/raw_echonest.csv'

# # # Read the CSV file
# # df = pd.read_csv(csv_file)

# # # Get unique column names
# # unique_columns = df.columns.unique()

# # # Print unique column names
# # print("Unique columns in a.csv:")
# # for column in unique_columns:
# #     print(column)

# import pandas as pd

# # Read the two CSV files
# audio_features_df = pd.read_csv('/home/khattak/Downloads/A3/audio_features.csv')
# m44_df = pd.read_csv('/home/khattak/Downloads/A3/allcsv/m44.csv')

# # Merge the two dataframes based on a common column, for example 'File_Name'
# merged_df = pd.merge(audio_features_df, m44_df, on='File_Name')

# # Print the merged dataframe
# print(merged_df)

# # Now you can do further operations with the merged dataframe, like saving it to a new CSV file
# merged_df.to_csv('final.csv', index=False)

import pandas as pd

# Read audio_features.csv
audio_features_df = pd.read_csv("/home/khattak/Downloads/A3/audio_features.csv")

# Read m44.csv
m44_df = pd.read_csv("/home/khattak/Downloads/A3/allcsv/m44.csv")

# Merge the two DataFrames based on their index
merged_df = pd.concat([audio_features_df, m44_df], axis=1)

# Store the merged DataFrame to a CSV file
merged_df.to_csv("final.csv", index=False)

print("Merged data stored in merged_data.csv")

