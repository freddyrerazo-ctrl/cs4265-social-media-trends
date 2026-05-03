import happybase

def get_hbase_connection():
    return happybase.Connection("hbase", port=9090, autoconnect=True)

def ensure_table_exists(connection, table_name):
    tables = [t.decode() for t in connection.tables()]
    if table_name not in tables:
        connection.create_table(table_name, {"metrics": dict(), "metadata": dict()})
        print(f"[HBASE] Created table: {table_name}")
    else:
        print(f"[HBASE] Table already exists: {table_name}")

def write_to_hbase(df_final, table_name="social_trends"):
    print("[INFO] Writing results to HBase...")
    connection = get_hbase_connection()
    ensure_table_exists(connection, table_name)
    table = connection.table(table_name)
    rows = df_final.collect()
    count = 0
    with table.batch() as batch:
        for row in rows:
            row_key = str(row["post_id"]).encode()
            batch.put(row_key, {
                b"metadata:platform": str(row["platform"]).encode(),
                b"metadata:username": str(row["username"]).encode(),
                b"metadata:topic_category": str(row["topic_category"]).encode(),
                b"metrics:sentiment_score": str(row["sentiment_score"]).encode(),
                b"metrics:viral_impact": str(row["viral_impact"]).encode(),
                b"metrics:cluster": str(row["prediction"]).encode(),
            })
            count += 1
    connection.close()
    print(f"[SUCCESS] Written {count} records to HBase table: {table_name}")
