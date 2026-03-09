# Commands Used in YouTube Big Data Analytics Project

## 1. Start Hadoop

start-dfs.sh
start-yarn.sh

Check running services:

jps

---

## 2. Upload Dataset to HDFS

hdfs dfs -mkdir /youtube

hdfs dfs -put USvideos.csv /youtube/

Check files:

hdfs dfs -ls /youtube

---

## 3. Run Spark Analysis

spark-submit youtube_analysis.py

---

## 4. Store Results in HDFS

top_views.write.csv("hdfs://master:9000/results/top_views", header=True)

channel_views.write.csv("hdfs://master:9000/results/channel_views", header=True)

category_count.write.csv("hdfs://master:9000/results/category_count", header=True)

avg_views.write.csv("hdfs://master:9000/results/avg_views", header=True)

top_likes.write.csv("hdfs://master:9000/results/top_likes", header=True)

top_comments.write.csv("hdfs://master:9000/results/top_comments", header=True)

trending.write.csv("hdfs://master:9000/results/trending", header=True)

---

## 5. Copy Results to Local System

hdfs dfs -get /results ~/

---

## 6. Run Streamlit Dashboard

streamlit run dashboard.py
