# MovieLens Data Analytics using Apache Spark and Cassandra

## Project Overview

This project implements a distributed data analytics pipeline using Apache Spark and Apache Cassandra on the MovieLens dataset.

The project demonstrates:

* Loading MovieLens data into HDFS
* Creating Spark RDDs and DataFrames
* Data cleaning and preprocessing
* Analytical queries using Spark SQL
* Storing analytical results in Cassandra
* Reading Cassandra tables back into Spark for validation

## Technologies Used

* Apache Spark 2.x
* Apache Cassandra 3.11
* Apache Zeppelin
* Hadoop HDFS
* Python (PySpark)

## Analytical Tasks

### Task 1

Movie rating statistics and genre analysis.

### Task 2

Top 10 highest-rated movies analysis.

### Task 3

Favourite genre analysis among active users.

### Task 4

Favourite genre analysis among users below 20 years old.

### Task 5

Favourite genre analysis among scientists aged 30–40 years old.

### Task 6

Store analytical outputs into Cassandra tables.

### Task 7

Validate Cassandra tables by reading them back into Spark.

## Key Findings

* Drama is the most common movie genre in the dataset.
* Drama is the dominant favourite genre among active users and scientists aged 30–40.
* Top-rated movies include Schindler's List, Casablanca, The Shawshank Redemption and Star Wars.
* Apache Cassandra successfully stored and retrieved all analytical outputs.

## Author

Hasma Nizam bin Mohamad Hassan

Master of Science (Data Science and Analytics)
