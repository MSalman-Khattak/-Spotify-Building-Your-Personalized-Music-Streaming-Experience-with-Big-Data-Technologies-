from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("MongoDB to Spark") \
    .config("spark.mongodb.input.uri", "mongodb://localhost:27017/MYDB.MTDATA") \
    .config("spark.mongodb.output.uri", "mongodb://localhost:27017/MYDB.MTDATA") \
    .getOrCreate()

# Columns to retrieve from MongoDB
selected_columns = ['File_Name', 'MFCCs', 'Spectral_Centroid', 'Zero_Crossing_Rate', 'genre_id']

# Load data from MongoDB into DataFrame
df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load().select(selected_columns)

# Coalesce DataFrame to a single partition and write to CSV
df.coalesce(1).write.option("header", "true").csv("/home/khattak/Downloads/A3/output.csv")

# Stop Spark session
spark.stop()

