# Distributed Social Media Trend Analytics
**CS 4265 Big Data Analytics - Milestone 2 Update**

## 🎯 Project Progress (Milestone 2)
As of March 8, 2026, the initial pipeline scaffolding and data acquisition phases are complete. 

**Current Status:**
- [x] Data acquired from Kaggle (Sentiment140/Reddit).
- [x] Project directory structure established.
- [x] Local ingestion script (Python/Pandas) verified for data persistence.
- [ ] Spark Batch Processing (Planned for M3).
- [ ] HBase Schema Integration (Planned for M3).

## 🛠️ Technology Stack
- **Ingestion:** Python 3.x / Pandas (Local Prototyping)
- **Storage:** HDFS-ready local file system (Mock HDFS structure)
- **Processing:** Apache Spark (Ready for deployment)
- **Data Store:** Parquet (Columnar storage for analytics)

## 📁 Repository Structure
```text
/social-media-trends-project
│
├── /data                
│   ├── /raw            <-- Contains Kaggle CSV (raw_social_media_data.csv)
│   └── /processed      <-- Contains script-generated samples
├── /src
│   └── ingest.py       <-- Script to load and persist data
├── requirements.txt     <-- Project dependencies (pandas, pyspark)
├── .gitignore           <-- Configured to exclude large datasets
└── README.md
