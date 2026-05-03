from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, BooleanType
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.sql.functions import col

def get_spark_session(app_name="SocialMediaTrendAnalytics"):
    return (SparkSession.builder
        .appName(app_name)
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2")
        .getOrCreate())

def get_tweet_schema():
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
        StructField("day_of_week", StringType(), True),
        StructField("is_trending_topic", BooleanType(), True),
        StructField("topic_category", StringType(), True),
        StructField("sentiment_label", StringType(), True),
        StructField("sentiment_score", FloatType(), True),
        StructField("emotion_label", StringType(), True),
        StructField("toxicity_score", FloatType(), True),
        StructField("sarcasm_detected", BooleanType(), True),
        StructField("spam_flag", BooleanType(), True),
        StructField("data_source_url", StringType(), True)
    ])

def ingest_raw_data(hdfs_path):
    print(f"[INFO] Ingesting data from HDFS: {hdfs_path}")
    spark = get_spark_session()
    df = spark.read.csv(
        hdfs_path, header=True, schema=get_tweet_schema(),
        multiLine=True, quote=chr(34), escape=chr(34)
    )
    count = df.count()
    print(f"[VALIDATION] Ingested {count} records from HDFS.")
    print("[SAMPLE] First 5 records:")
    df.select("platform", "username", "topic_category", "sentiment_score", "engagement_score").show(5, truncate=False)
    return df

def process_trends(df):
    print("[INFO] Starting Spark Transformation & ML Clustering...")
    df_cleaned = df.fillna({"sentiment_score": 0.0, "toxicity_score": 0.0, "like_count": 0, "engagement_score": 0.0})
    df_transformed = df_cleaned.withColumn("viral_impact", col("engagement_score") * col("like_count"))
    feature_cols = ["engagement_score", "sentiment_score", "viral_impact"]
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    df_features = assembler.transform(df_transformed)
    kmeans = KMeans().setK(5).setSeed(1)
    model = kmeans.fit(df_features)
    df_final = model.transform(df_features)
    result = df_final.select("platform", "post_id", "username", "topic_category", "sentiment_score", "viral_impact", "prediction")
    print("[RESULTS] Sample processed records:")
    result.show(10, truncate=False)
    print("[STATS] Cluster distribution:")
    result.groupBy("prediction").count().orderBy("prediction").show()
    return result
