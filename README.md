# 📊 Distributed Social Media Trend Analytics
**CS 4265 Big Data Analytics — Milestone 4: Final Deliverable**

> A production-grade Big Data pipeline that ingests, processes, and analyzes 2,200+ social media records using real distributed infrastructure.

---

## 🏗️ Architecture
raw_tweets.csv → HDFS (Hadoop 3.2.1) → Spark 3.5.0 → KMeans ML → HBase 2.1.2
| Stage | Tool | Role |
|-------|------|------|
| Ingestion | HDFS + Python | Upload raw CSV to distributed storage |
| Processing | Apache Spark | Schema enforcement, cleaning, feature engineering |
| ML | Spark MLlib | KMeans clustering (k=5) |
| Storage | Apache HBase | NoSQL persistence of 2,200 processed records |

---

## 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Distributed Storage | Apache Hadoop HDFS | 3.2.1 |
| Processing Engine | Apache Spark (PySpark) | 3.5.0 |
| ML Library | Spark MLlib KMeans | 3.5.0 |
| NoSQL Database | Apache HBase | 2.1.2 |
| Orchestration | Docker + Docker Compose | - |
| HBase Client | happybase | latest |
| Language | Python | 3.8+ |

---

## 📁 Project Structure

```
cs4265-social-media-trends/
├── README.md
├── LICENSE
├── requirements.txt
├── docker-compose.yml
├── hadoop.env
├── .env.example
├── main.py
├── config/
│   └── settings.yaml
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── src/
│   ├── ingestion/
│   │   └── hdfs_upload.py
│   ├── processing/
│   │   └── spark_init.py
│   └── storage/
│       └── hbase_handler.py
└── docs/
    ├── architecture.md
    ├── data_dictionary.md
    └── validation.md
```
---

## 🚀 Setup Instructions

### Prerequisites
- Docker Desktop installed and running
- Python 3.8+
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/freddyrerazo-ctrl/cs4265-social-media-trends.git
cd cs4265-social-media-trends
```

### 2. Set Up Environment Variables
```bash
cp .env.example .env
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Full Cluster
```bash
docker-compose up -d
sleep 30
docker ps
```

### 5. Upload Data to HDFS
```bash
python src/ingestion/hdfs_upload.py
```

### 6. Run the Full Pipeline
```bash
docker exec -u root spark pip install pyspark pyyaml python-dotenv numpy happybase
docker exec -u root spark bash -c "cd /app && python3 -u main.py"
```

### 7. Verify HBase Data
```bash
docker exec -it hbase hbase shell
```
Inside the shell:
```
list
count 'social_trends'
scan 'social_trends', {LIMIT => 3}
exit
```

---

## ✅ Expected Output

```
[INFO] Ingesting data from HDFS: hdfs://namenode:9000/data/social/raw/raw_tweets.csv
[VALIDATION] Ingested 2200 records from HDFS.
[SAMPLE] First 5 records:
+--------+--------+--------------+---------------+----------------+
|platform|username|topic_category|sentiment_score|engagement_score|
+--------+--------+--------------+---------------+----------------+
|YouTube |rxckafna|Technology    |0.82           |0.7             |
|Reddit  |zjovqwps|Sports        |-0.02          |0.45            |
+--------+--------+--------------+---------------+----------------+
[HBASE] Created table: social_trends
[SUCCESS] Written 2200 records to HBase table: social_trends
[SUCCESS] Pipeline complete for app: SocialMediaTrendAnalytics
```
---

## 📊 Validation Results

| Metric | Value |
|--------|-------|
| Records ingested from HDFS | 2,200 |
| Records dropped during cleaning | 0 |
| KMeans clusters | 5 |
| Records written to HBase | 2,200 |

**Cluster Distribution:**

| Cluster | Count |
|---------|-------|
| 0 | 509 |
| 1 | 153 |
| 2 | 411 |
| 3 | 860 |
| 4 | 267 |

Full report: [docs/validation.md](docs/validation.md)

---

## ⚠️ Known Limitations

- **Single datanode**: Development uses replication factor 1. Production would use 3+.
- **Platform emulation**: Docker runs amd64 images under Rosetta on Apple Silicon — functionally correct.

---

## 👤 Author

**Freddy Erazo** — CS 4265 Big Data Analytics, Spring 2026
