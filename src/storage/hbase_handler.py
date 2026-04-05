import happybase
import pandas as pd
import numpy as np

def save_to_hbase(df, table_name="social_media_trends"):
    """
    Persists the processed Pandas DataFrame to HBase.
    M3 Requirement: Complete Implementation of Storage Sink.
    """
    if df is None or (isinstance(df, pd.DataFrame) and df.empty):
        print("[WARNING] No data provided to save_to_hbase.")
        return False

    try:
        # 1. Establish connection with explicit protocol and transport
        connection = happybase.Connection(
            host='localhost',
            port=9090,
            protocol='binary',
            transport='buffered'
        )
        connection.open()

        # 2. Ensure table exists
        tables = [t.decode('utf-8') for t in connection.tables()]
        if table_name not in tables:
            print(f"[INFO] Creating HBase table: {table_name}")
            connection.create_table(
                table_name,
                {'metrics': dict(), 'meta': dict()}
            )

        table = connection.table(table_name)
        
        # 3. Batch insert with type-safety
        print(f"[INFO] Persisting {len(df)} rows to HBase...")
        with table.batch() as b:
            for index, row in df.iterrows():
                row_val = row.get('post_id')
                if pd.isna(row_val):
                    row_val = index
                row_key = str(row_val).encode('utf-8')
                
                def clean(val):
                    return str(val) if pd.notna(val) else "0"

                b.put(row_key, {
                    b'metrics:sentiment': clean(row.get('sentiment_score')).encode('utf-8'),
                    b'metrics:toxicity': clean(row.get('toxicity_score')).encode('utf-8'),
                    b'meta:platform': clean(row.get('platform', 'unknown')).encode('utf-8'),
                    b'meta:author': clean(row.get('username', 'anonymous')).encode('utf-8')
                })

        connection.close()
        print(f"[SUCCESS] Data successfully persisted to HBase table: {table_name}")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to save to HBase: {e}")
        return False
