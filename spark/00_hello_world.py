from pyspark.sql import SparkSession

# Step 1: Set up the Spark session
spark = SparkSession.builder \
    .appName("HelloWorldSparkJob") \
    .getOrCreate()

# Step 2: Define a simple action to print "Hello World" using Spark
rdd = spark.sparkContext.parallelize(["Hello World"])

# Step 3: Perform an action to collect and print the data from the RDD
for message in rdd.collect():
    print(message)
