Distributed Social Media Trend Analytics
CS 4265 Big Data Analytics - Milestone 3: Complete Implementation

🎯 Project Progress (Milestone 3)
As of April 5, 2026, the end-to-end Big Data pipeline is fully operational. Data now flows automatically from raw ingestion through Spark transformation into a persistent HBase NoSQL store.

Current Status:

[x] Data Ingestion: Automated pipeline for 2,200+ social media records.

[x] Spark Batch Processing: Full schema implementation (27 columns) with data cleaning and normalization.

[x] HBase Persistence: Successful integration with HBase via Thrift Server for scalable NoSQL storage.

[x] Automated Workflow: Verified end-to-end execution from main.py.

🛠️ Technology Stack
Processing: Apache Spark (PySpark)

Storage Sink: Apache HBase (NoSQL)

Interface: Thrift Server / HappyBase

Environment: Java 11 / Python 3.x

Data Format: CSV (Raw) -> Spark DataFrame -> HBase Tables

📁 Repository Structure
Plaintext
/cs4265-social-media-trends
│
├── /data                
│   ├── /raw            <-- Input: raw_tweets.csv (27 columns)
│   └── /processed      <-- Output: final_trends.csv (Spark-transformed)
├── /src
│   ├── /processing     <-- spark_init.py (Schema & Transformations)
│   └── /storage        <-- hbase_handler.py (HBase/Thrift connection)
├── /config             <-- Environment & Port configurations
├── main.py             <-- Pipeline Entry Point (Run this)
├── requirements.txt    <-- Dependencies: pyspark, happybase, pandas
└── README.md
🚀 Execution Instructions
1. Prerequisites
Ensure HBase is installed and running locally. Due to the distributed nature of the storage sink, the Thrift Server must be active to allow Python communication.

2. Start Services
Open a terminal and start the Thrift service:

Bash
hbase thrift start
3. Run the Pipeline
Execute the main script to trigger the full ingestion and transformation process:

Bash
python3 main.py
4. Verify Persistence
To confirm data has been successfully stored in the NoSQL sink, use the HBase shell:

Bash
hbase shell
hbase> scan 'social_media_trends', {LIMIT => 5}
