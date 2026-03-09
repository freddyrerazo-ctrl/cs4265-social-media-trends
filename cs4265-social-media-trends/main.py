import yaml
import os
from src.ingestion.hdfs_upload import ingest_raw_data

def load_config():
    with open("config/settings.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    print("--- Social Media Trend Analytics Pipeline: M2 Execution ---")
    config = load_config()
    
    # Step 1: Ingestion (Data Acquisition)
    # Using the path defined in your settings.yaml
    raw_file = os.path.join("data", "raw", "raw_tweets.csv")
    
    success = ingest_raw_data(raw_file)
    
    if success:
        print("M2 Milestone Reached: Data is accessible and persisted.")
    else:
        print("Pipeline failed at Ingestion stage.")

if __name__ == "__main__":
    main()
