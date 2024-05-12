import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['MYDB']
collection = db['MTDATA']

# Read the CSV file using pandas
df = pd.read_csv('/home/khattak/Downloads/A3/final.csv')

# Convert the dataframe to a list of dictionaries and insert it into the collection
collection.insert_many(df.to_dict('records'))

print("Data inserted successfully!")

# Print inserted data
cursor = collection.find({})
for document in cursor:
    print(document)
