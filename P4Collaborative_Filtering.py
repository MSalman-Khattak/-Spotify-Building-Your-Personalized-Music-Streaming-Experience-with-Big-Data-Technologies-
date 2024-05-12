from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Collaborative Filtering Feature Engineering") \
    .getOrCreate()

# Load data from MongoDB into Spark DataFrame
mongo_uri = "mongodb://localhost:27017/music_database.audio_features"
df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", mongo_uri).load()

# Convert user and item IDs to numeric indices
user_indexer = StringIndexer(inputCol="user_id", outputCol="user_idx").fit(df)
item_indexer = StringIndexer(inputCol="item_id", outputCol="item_idx").fit(df)

# Apply indexing transformations
df = user_indexer.transform(df)
df = item_indexer.transform(df)

# Optionally, transform ratings if needed

# Stop SparkSession
spark.stop()

