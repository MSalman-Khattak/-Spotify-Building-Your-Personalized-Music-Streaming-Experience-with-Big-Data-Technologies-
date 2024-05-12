Report: Preprocessing Phase for Spotify Music Recommendation System
Introduction
The Spotify Music Recommendation System aims to provide personalized music recommendations to users based on their listening history, preferences, and characteristics of the songs. The first phase of this project involves Extract, Transform, Load (ETL) preprocessing of the raw data to prepare it for further analysis and model development.

Phase 1: Extract, Transform, Load (ETL) Preprocessing
Step 1: Data Extraction
The raw data is extracted from various CSV files containing information about genres, albums, tracks, artists, echonest features, and audio features.

Step 2: Data Transformation
Merging DataFrames: The extracted data is transformed by merging relevant DataFrames using common columns such as genre_id, album_id, and artist_id. This consolidation allows for a comprehensive view of the data and reduces redundancy.
Feature Extraction: For audio data, features such as Mel-Frequency Cepstral Coefficients (MFCCs), spectral centroid, and zero-crossing rate are extracted using the librosa library. These features provide valuable insights into the characteristics of the audio signals.
Normalization: The extracted features are normalized or standardized to ensure that they have a comparable scale and distribution. This step is essential for the accuracy and stability of subsequent machine learning algorithms.
Step 3: Data Loading
The preprocessed data is loaded into new CSV files for easy access and further analysis. These files contain the transformed data ready for modeling and recommendation algorithms.

Explanation of Music Recommendation Model Phase
Introduction
In the Music Recommendation Model phase of the project, we focus on leveraging data from various sources, including CSV files and MongoDB, to develop a robust recommendation system. This phase involves two main tasks: storing preprocessed data in MongoDB and retrieving it for further analysis using Apache Spark.

Task 1: Storing Preprocessed Data in MongoDB
Step 1: Connecting to MongoDB
The code establishes a connection to a MongoDB database named 'MYDB' running on the localhost at port 27017 using the pymongo library.
Step 2: Reading the Preprocessed Data
The preprocessed data, stored in a CSV file named 'final.csv', is read into a Pandas DataFrame using the pd.read_csv() function.
Step 3: Inserting Data into MongoDB Collection
The DataFrame is converted into a list of dictionaries using the to_dict('records') method.
Each dictionary represents a document to be inserted into the MongoDB collection named 'MTDATA'.
The insert_many() method is used to insert multiple documents into the collection at once.
Step 4: Confirmation
A message is printed to indicate that the data insertion process was successful.
The inserted data is then retrieved from the MongoDB collection and printed for verification.
Task 2: Retrieving Data from MongoDB and Storing in CSV
Step 1: Initializing Spark Session
A Spark session is initialized using SparkSession.builder with the necessary configurations for reading and writing data to MongoDB.
Step 2: Loading Data from MongoDB
Data is loaded from the MongoDB collection 'MYDB.MTDATA' into a Spark DataFrame using the com.mongodb.spark.sql.DefaultSource format.
Only selected columns ('File_Name', 'MFCCs', 'Spectral_Centroid', 'Zero_Crossing_Rate', 'genre_id') are retrieved from MongoDB.
Step 3: Writing Data to CSV
The DataFrame is coalesced into a single partition to ensure all data is written to a single CSV file.
The data is written to a CSV file named 'output.csv' with the specified header option.
Step 4: Stopping Spark Session
The Spark session is stopped to release resources. Framework and Technologies: The application is built using Flask, a lightweight Python web framework, making it easy to develop web applications. Additionally, it employs Apache Kafka, a distributed streaming platform, for real-time data processing and messaging.

Kafka Setup: The code initializes Kafka producer and consumer instances to interact with Kafka topics. These topics, namely user_activity and recommendations, serve as channels for transmitting user activity data and receiving recommendation messages, respectively.

User Activity Simulation: A background thread is created to simulate user activity by continuously sending mock user actions, such as listening to or liking songs, to the user_activity Kafka topic. This ensures that the application generates recommendations based on ongoing user interactions.

Homepage Route: The root route of the web application ('/') is defined to render the index template. Upon receiving recommendation messages from the Kafka consumer, the recommendations are appended to a global list. Once a sufficient number of recommendations (in this case, three) are collected, they are passed to the index template for rendering. The recommendations list is then cleared to accommodate new recommendations.

Main Block: The main block of the code ensures that the Flask application runs in debug mode when executed as the main script.

User Experience Enhancement: By integrating Kafka with Flask, the application offers users an enhanced music streaming experience. It dynamically updates recommendations in real-time, reflecting users' preferences and behaviors as they interact with the platform. This seamless integration facilitates personalized music suggestions, thereby improving user engagement and satisfaction.
