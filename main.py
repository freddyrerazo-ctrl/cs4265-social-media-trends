from src.ingestion.hdfs_upload import ingest_raw_data
from src.processing.spark_init import process_trends
from src.storage.hbase_handler import save_to_hbase

def main():
    print("--- Social Media Trend Analytics Pipeline: M3 Execution ---")
    
    # 1. Capture the actual data here
    df = ingest_raw_data("data/raw/raw_tweets.csv")
    
    if df is not None:
        # 2. Now 'df' is a real table, so 'fillna' will work!
        processed_df = process_trends(df)
        
        # 3. Store in HBase
        save_to_hbase(processed_df)
        
        print("[SUCCESS] M3 Milestone Reached: Data is accessible and PERSISTED.")
    else:
        print("[ERROR] Pipeline failed at Ingestion stage.")

if __name__ == "__main__":
    main()
