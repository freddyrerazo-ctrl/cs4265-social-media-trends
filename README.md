## Distributed Social Media Trend Analytics

**CS 4265 Big Data Analytics - Milestone 1 Project**  
*Building scalable trend analysis pipeline using HDFS, Spark, and HBase*

## 🎯 Project Overview

Analyzes large social media datasets (Twitter/Reddit posts) to compute hashtag trends, engagement patterns, and regional popularity over time. Processes millions of posts that exceed single-machine memory limits using distributed storage and parallel processing across the Big Data stack.

**Key Questions Answered:**
- What are the top trending hashtags by date/region?
- How does hashtag popularity evolve over time?
- Which topics generate highest engagement per region?

## 🛠️ Technology Stack

- **Storage**: HDFS (128MB blocks, replication=3)
- **Processing**: Apache Spark (DataFrame API, batch jobs)
- **Data Store**: HBase (wide-column) + Parquet (columnar analytics)
- **Querying**: Spark SQL (distributed trend analytics)

## 📁 Repository Structure


## 📊 Data Sources

- **Twitter Sentiment Dataset** (1.6M+ tweets): timestamps, hashtags, engagement metrics
- **Reddit Post Dataset**: posts, comments, subreddit metadata
- Download from Kaggle public repositories

## 🚀 Quick Start (Local Development)

### Prerequisites
- Hadoop 3.x (single-node cluster mode)
- Apache Spark 3.x
- HBase 2.x
- Python 3.8+ with `pyspark`

### 1. Start Services
```bash
# Start Hadoop/HDFS
start-dfs.sh

# Start HBase  
start-hbase.sh
-- Example: Top 10 trends on 2026-01-29
SELECT hashtag, SUM(likes) as total_engagement
FROM hbase_trends
WHERE date = '2026-01-29'
GROUP BY hashtag
ORDER BY total_engagement DESC
LIMIT 10;
