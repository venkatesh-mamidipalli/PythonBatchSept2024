import findspark
import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Step 1: Set up Spark Session
spark = SparkSession.builder.appName("Employee").getOrCreate()
sc = spark.sparkContext

# Step 2: Create a sample employee details dataset as a Python dictionary
employee_data = [
    {"emp_id": 1, "name": "Alice", "age": 30, "department": "HR", "salary": 50000},
    {"emp_id": 2, "name": "Bob", "age": 25, "department": "Engineering", "salary": 80000},
    {"emp_id": 3, "name": "Charlie", "age": 35, "department": "Finance", "salary": 60000},
    {"emp_id": 4, "name": "David", "age": 40, "department": "Engineering", "salary": 90000},
    {"emp_id": 5, "name": "Eva", "age": 29, "department": "HR", "salary": 55000}
]

# Step 3: Convert the Python dictionary to a Spark DataFrame
df = spark.createDataFrame(employee_data)

# Step 4: Perform a simple transformation - filter employees in the Engineering department with salary > 75000
filtered_df = df.filter((col("department") == "Engineering") & (col("salary") > 75000))

# Step 5: Show the result
filtered_df.show()

print(f"Spark Version: {sc.uiWebUrl}")