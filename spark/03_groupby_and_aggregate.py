import findspark
import pyspark

from pyspark import SparkConf, SparkContext
import sys
from pyspark.sql import SparkSession, functions, types, SQLContext

spark = SparkSession.builder.appName('temperature range sql').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("ERROR")

cMap = {"k1": "v1", "k2": "v1", "k3": "v2", "k4": "v2"}
aCMap = [(k, v) for k, v in cMap.items()]
data = spark.createDataFrame(aCMap, ['key', 'val'])

from pyspark.sql.functions import count
data = data.groupBy('key').pivot('val').agg(count('val'))
data.show()
