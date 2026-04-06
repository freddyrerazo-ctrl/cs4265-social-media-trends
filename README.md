# 📊 Distributed Social Media Trend Analytics
**CS 4265 Big Data Analytics - Milestone 3: Complete Implementation**

## 🎯 Project Overview
This project implements a fully automated Big Data pipeline designed to ingest, process, and persist social media trend data at scale. Using **Apache Spark** for distributed processing and **Apache HBase** as a NoSQL storage sink, the system transforms raw unstructured data into actionable insights stored in a high-performance database.

### **Current Status: Milestone 3 (April 5, 2026)**
- [x] **Robust Data Ingestion:** Automated pipeline for 2,200+ social media records with a comprehensive 27-column schema.
- [x] **Spark Batch Processing:** Implemented cleaning, normalization, and feature engineering (e.g., spam filtering and sentiment handling).
- [x] **NoSQL Persistence:** Successful integration with HBase via the Thrift Server for scalable data storage.
- [x] **End-to-End Automation:** Verified execution flow from raw CSV to HBase queryable state via `main.py`.

---

## 🛠️ Technology Stack
* **Engine:** Apache Spark (PySpark) 3.x
* **Database:** Apache HBase (NoSQL)
* **Interface:** Apache Thrift Server / HappyBase
* **Environment:** Java 11 / Python 3.x / macOS (Darwin)
* **Data Pipeline:** CSV (Raw) ➔ Spark DataFrame ➔ Refined CSV ➔ HBase Tables

---
## 🚀 Execution Instructions
1. Prerequisites
HBase must be installed and running on the local loopback. Due to the Python-HBase interface, the Thrift Server must be active.

2. Start Services
Open a terminal and start the Thrift daemon:

Bash
hbase thrift start

3. Run the Pipeline
Execute the main script to trigger the ingestion and transformation process:

Bash
python3 main.py

4. Verify Data Persistence
Confirm the data is stored in the NoSQL sink using the HBase shell:

Bash
hbase shell
hbase> scan 'social_media_trends', {LIMIT => 5}

---
## 🔧 Troubleshooting & Notes
VPN Interference: If the Thrift server fails to connect (port 9090), ensure any active VPNs are disabled to allow local loopback traffic.

Java Compatibility: This project is optimized for Java 11. Ensure JAVA_HOME is set correctly in your environment.

Local Paths: The pipeline uses relative paths. Ensure you execute main.py from the project root directory.

## 📁 Repository Structure
```text
/cs4265-social-media-trends
│
├── /data                
│   ├── /raw            <-- Input: raw_tweets.csv (Initial 27-column dataset)
│   └── /processed      <-- Output: final_trends.csv (Spark-cleaned & Transformed)
├── /src
│   ├── /processing     <-- spark_init.py (Schema definitions & Spark transformations)
│   └── /storage        <-- hbase_handler.py (HBase connection & Thrift operations)
├── /config             <-- Environment & Port configurations
├── main.py             <-- Entry Point: Coordinates the full pipeline execution
├── requirements.txt    <-- Dependencies: pyspark, happybase, pandas, thrift
└── README.md
