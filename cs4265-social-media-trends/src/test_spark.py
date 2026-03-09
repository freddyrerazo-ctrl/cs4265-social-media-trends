from src.processing.spark_init import get_spark_session, get_tweet_schema
import os

def test_pipeline_link():
    # 1. Initialize Spark
    print("Checking Spark Session...")
    spark = get_spark_session()
    
    # 2. Locate Data
    data_path = "data/raw/raw_tweets.csv"
    if not os.path.exists(data_path):
        print(f"Error: Could not find {data_path}")
        return

    # 3. Try to load with your Schema
    print(f"Loading {data_path} with defined schema...")
    try:
        df = spark.read.csv(data_path, header=True, schema=get_tweet_schema())
        
        # 4. The Proof
        print("\n--- SCHEMA VALIDATION ---")
        df.printSchema()
        
        print("\n--- DATA PREVIEW (First 5 Rows) ---")
        df.show(5)
        
        print("\n[SUCCESS] Spark logic and Data Ingestion are connected!")
    except Exception as e:
        print(f"\n[FAILURE] Connection error: {e}")

if __name__ == "__main__":
    test_pipeline_link()
