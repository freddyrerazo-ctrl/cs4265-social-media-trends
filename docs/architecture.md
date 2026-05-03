# Architecture

## Pipeline Overview
raw_tweets.csv → HDFS → Spark → KMeans ML → CSV Output

## Components
- **HDFS**: Hadoop 3.2.1 (namenode + datanode) running in Docker
- **Spark**: Apache Spark 3.5.0 running in Docker, reads directly from HDFS
- **ML**: Spark MLlib KMeans clustering (k=5)
- **Output**: CSV written via Spark coalesce

## Data Flow
1. `hdfs_upload.py` uploads raw CSV to HDFS at /data/social/raw/
2. Spark reads from hdfs://namenode:9000/data/social/raw/raw_tweets.csv
3. Schema enforced via StructType (27 fields)
4. Nulls filled, viral_impact derived column computed
5. VectorAssembler prepares features for KMeans
6. Results written to /tmp/output as CSV
