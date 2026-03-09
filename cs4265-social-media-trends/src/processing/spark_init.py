from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, BooleanType, TimestampType

def get_spark_session(app_name="SocialMediaTrendAnalytics"):
    """Initializes a Spark Session with basic configurations."""
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()

def get_tweet_schema():
    """
    Defines the schema based on raw_tweets.csv structure.
    This fulfills the 'Schema Validation' requirement from your diagrams.
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
        StructField("posted_datetime", StringType(), True), # Often read as string then cast to Timestamp
        StructField("sentiment_score", FloatType(), True),
        StructField("toxicity_score", FloatType(), True)
    ])
