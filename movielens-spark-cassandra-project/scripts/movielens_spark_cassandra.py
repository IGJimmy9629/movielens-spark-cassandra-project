from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Create Spark Session
spark = SparkSession.builder \
    .appName("MovieLens Spark Cassandra Pipeline") \
    .getOrCreate()

print("Spark session created successfully")

# Load MovieLens data
ratings_df = spark.read.csv(
    "ratings.csv",
    header=True,
    inferSchema=True
)

users_df = spark.read.csv(
    "users.csv",
    header=True,
    inferSchema=True
)

movies_df = spark.read.csv(
    "movies.csv",
    header=True,
    inferSchema=True
)

print("MovieLens datasets loaded successfully")