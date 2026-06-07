# MovieLens Data Analytics using Apache Spark and Cassandra

## Project Overview

This project implements a distributed data analytics pipeline using Apache Spark and Apache Cassandra on the MovieLens 100K dataset.

The project demonstrates data loading from HDFS, RDD creation, Spark DataFrame transformation, data preprocessing, analytical queries, Cassandra storage, and validation by reading Cassandra tables back into Spark.

## Technologies Used

- Apache Spark
- Apache Cassandra
- Apache Zeppelin
- Hadoop HDFS
- Hive
- Python / PySpark
- Spark-Cassandra Connector

## Dataset

MovieLens 100K dataset containing:

- user ratings
- user demographic information
- movie details and genres

## Analytical Tasks

1. Calculate average rating for each movie.
2. Identify top ten highest-rated movies.
3. Identify active users and their favourite movie genres.
4. Analyse users younger than 20 years old.
5. Analyse scientists aged between 30 and 40 years old.
6. Store processed analytical results into Cassandra.
7. Read Cassandra tables back into Spark for validation.

## Key Findings

- Drama is the most common movie genre in the dataset.
- Drama is the dominant favourite genre among active users.
- The top-rated movies include Schindler's List, Casablanca, The Shawshank Redemption and Star Wars.
- Cassandra successfully stored and retrieved the analytical outputs.

## How to Run

1. Start HDP Sandbox.
2. Start HDFS, Hive, Spark, Zeppelin and Cassandra.
3. Import the Zeppelin JSON notebook if using Zeppelin.
4. Open the Jupyter Notebook version for review.
5. Run notebook sections sequentially.
6. Ensure Cassandra keyspace and tables are created before running Cassandra write and validation sections.

## Author

Hasma Nizam bin Mohamad Hassan
Master of Science Data Science and Analytics
