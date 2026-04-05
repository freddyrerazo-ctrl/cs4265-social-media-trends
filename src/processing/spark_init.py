from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, BooleanType, TimestampType

def get_spark_session(app_name="SocialMediaTrendAnalytics"):
    """Initializes a Spark Session with basic configurations."""
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()

def get_tweet_schema():
    """
    Complete M3 Schema: 27 fields to match raw_tweets.csv perfectly.
    This fixes the NULL values caused by the header/schema mismatch.
    """
    return StructType([
        StructField("platform", StringType(), True),
        StructField("post_id", StringType(), True),
        StructField("user_id", StringType(), True),
        StructField("username", StringType(), True),
        StructField("user_verified", BooleanType(), True),
        StructField("user_followers_count", IntegerType(), True),
        StructField("user_location", StringType(), True),
        StructField("post_text", StringType(), True),
        StructField("language", StringType(), True),
        StructField("hashtags", StringType(), True),
        StructField("mentions", StringType(), True),
        StructField("post_length", IntegerType(), True),
        StructField("like_count", IntegerType(), True),
        StructField("comment_count", IntegerType(), True),
        StructField("share_count", IntegerType(), True),
        StructField("engagement_score", FloatType(), True),
        StructField("posted_datetime", StringType(), True),
        StructField("day_of_week", StringType(), True),        # Added
        StructField("is_trending_topic", BooleanType(), True), # Added
        StructField("topic_category", StringType(), True),     # Added
        StructField("sentiment_label", StringType(), True),    # Added
        StructField("sentiment_score", FloatType(), True),
        StructField("emotion_label", StringType(), True),      # Added
        StructField("toxicity_score", FloatType(), True),
        StructField("sarcasm_detected", BooleanType(), True),  # Added
        StructField("spam_flag", BooleanType(), True),         # Added
        StructField("data_source_url", StringType(), True)     # Added
    ])
    
def process_trends(df):
    print("[INFO] Starting Spark Transformation...")

    # 1. Cleaning & Filling
    df_cleaned = df.fillna({
        "sentiment_score": 0.0, 
        "toxicity_score": 0.0, 
        "like_count": 0,
        "spam_flag": False
    })

    # 2. Filtering: Only keep "Valid" and "Non-Spam" posts
    # This immediately makes the processed data different from the raw data
    df_filtered = df_cleaned.filter(
        (df_cleaned.post_id.isNotNull()) & 
        (df_cleaned.spam_flag == False)
    )

    # 3. Add a New Metric: "Viral Score"
    # Let's create a logic: engagement_score * like_count
    from pyspark.sql.functions import col
    df_transformed = df_filtered.withColumn(
        "viral_impact", col("engagement_score") * col("like_count")
    )

    # 4. Selection: Only keep the columns we actually need for the final report
    # This removes the "noise" (like user_id, mentions, data_source_url)
    final_columns = [
        "platform", "post_id", "username", "topic_category", 
        "sentiment_label", "sentiment_score", "viral_impact"
    ]
    df_final = df_transformed.select(*final_columns)

    # CONVERT TO PANDAS
    pandas_df = df_final.toPandas()

    # SAVE TO YOUR EMPTY FOLDER
    output_path = "data/processed/final_trends.csv"
    pandas_df.to_csv(output_path, index=False)
    print(f"[SUCCESS] File created in: {output_path}")

    return pandas_df
