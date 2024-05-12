from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Collaborative Filtering Model Training") \
    .getOrCreate()

# Assuming df is the DataFrame with indexed user and item columns

# Split data into training and testing sets
(training, test) = df.randomSplit([0.8, 0.2])

# Initialize ALS model
als = ALS(maxIter=10, regParam=0.01, userCol="user_idx", itemCol="item_idx", ratingCol="rating",
          coldStartStrategy="drop")

# Train ALS model
model = als.fit(training)

# Generate predictions
predictions = model.transform(test)

# Evaluate model
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print("Root Mean Squared Error (RMSE):", rmse)

# Stop SparkSession
spark.stop()

