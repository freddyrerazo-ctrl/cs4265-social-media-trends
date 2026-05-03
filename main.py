import yaml
import os
from dotenv import load_dotenv
from src.processing.spark_init import ingest_raw_data, process_trends
from src.storage.hbase_handler import write_to_hbase

load_dotenv()
os.environ["HADOOP_USER_NAME"] = "root"

with open("config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

def main():
    host = config["hdfs"]["host"]
    port = config["hdfs"]["port"]
    path = config["hdfs"]["raw_data_path"]
    HDFS_PATH = f"hdfs://{host}:{port}{path}/raw_tweets.csv"
    df = ingest_raw_data(HDFS_PATH)
    if df:
        processed_df = process_trends(df)
        write_to_hbase(processed_df)
        app = config["spark"]["app_name"]
        print(f"[SUCCESS] Pipeline complete for app: {app}")

if __name__ == "__main__":
    main()
