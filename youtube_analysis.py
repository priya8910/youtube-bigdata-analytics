from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Start Spark Session
spark = SparkSession.builder.appName("YouTubeAnalysis").getOrCreate()

# Read dataset from HDFS
df = spark.read.csv("hdfs://master:9000/youtube/USvideos.csv", header=True, inferSchema=True)

df.show(5)

# Top viewed videos
top_views = df.orderBy(col("views").desc())
top_views.select("title","channel_title","views").show(10)

# Top liked videos
top_likes = df.orderBy(col("likes").desc())
top_likes.select("title","channel_title","likes").show(10)

# Channels with highest total views
channel_views = df.groupBy("channel_title") \
    .sum("views") \
    .withColumnRenamed("sum(views)", "total_views") \
    .orderBy(col("total_views").desc())

channel_views.show(10)

# Category statistics
category_count = df.groupBy("category_id") \
    .count() \
    .orderBy(col("count").desc())

category_count.show()

# Average views per channel
avg_views = df.groupBy("channel_title") \
    .avg("views") \
    .withColumnRenamed("avg(views)", "average_views") \
    .orderBy(col("average_views").desc())

avg_views.show(10)

# Top commented videos
top_comments = df.orderBy(col("comment_count").desc())
top_comments.select("title","channel_title","comment_count").show(10)

# Trending videos
trending = df.orderBy(col("views").desc())
trending.select("title","views","likes","comment_count").show(10)

# Save results to HDFS
top_views.write.csv("hdfs://master:9000/results/top_views", header=True)
top_likes.write.csv("hdfs://master:9000/results/top_likes", header=True)
channel_views.write.csv("hdfs://master:9000/results/channel_views", header=True)
category_count.write.csv("hdfs://master:9000/results/category_count", header=True)
avg_views.write.csv("hdfs://master:9000/results/avg_views", header=True)
top_comments.write.csv("hdfs://master:9000/results/top_comments", header=True)
trending.write.csv("hdfs://master:9000/results/trending", header=True)
