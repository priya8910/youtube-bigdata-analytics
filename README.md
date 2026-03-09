# YouTube Big Data Analytics

## Technologies Used
- Hadoop
- Spark
- HDFS
- Python
- Streamlit

## Project Description
This project analyzes YouTube trending video data using Hadoop and Spark.

The dataset is stored in HDFS and processed using Apache Spark to generate insights such as:

- Top viewed videos
- Top liked videos
- Channels with highest views
- Category statistics
- Trending videos

## Cluster Setup

The Hadoop cluster was configured using a master–worker architecture.

- **Master Node**: Responsible for running NameNode and ResourceManager.
- **Worker Node(s)**: Responsible for running DataNode and NodeManager services.

The cluster was deployed using Virtual Machines where one VM acts as the master node and another VM acts as the worker node.

Services running in the cluster include:
- NameNode
- DataNode
- ResourceManager
- NodeManager

## Dashboard
A Streamlit dashboard is used to visualize the analytics results.

## How to Run
1. Start Hadoop
2. Run Spark analysis
3. Store results in HDFS
4. Launch dashboard
