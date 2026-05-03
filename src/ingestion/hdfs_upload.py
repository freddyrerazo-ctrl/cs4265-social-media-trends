import subprocess
import yaml
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, "../../"))
config_path = os.path.join(project_root, "config/settings.yaml")

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

def upload_to_hdfs(local_path):
    """
    Physically move data to HDFS using Docker commands.
    This fulfills the M4 requirement for a real storage layer.
    """
    hdfs_dest = config['hdfs']['raw_data_path'] # /data/social/raw
    
    try:
        # 1. Create HDFS directory inside Docker
        subprocess.run(["docker", "exec", "namenode", "hadoop", "fs", "-mkdir", "-p", hdfs_dest], check=True)
        
        # 2. Upload file to the container
        subprocess.run(["docker", "cp", local_path, "namenode:/tmp/raw_tweets.csv"], check=True)
        
        # 3. Move from container disk to HDFS
        subprocess.run(["docker", "exec", "namenode", "hadoop", "fs", "-put", "-f", "/tmp/raw_tweets.csv", hdfs_dest], check=True)
        
        print(f"[SUCCESS] Uploaded {local_path} to HDFS at {hdfs_dest}")
        return True
    except Exception as e:
        print(f"[ERROR] HDFS physical upload failed: {e}")
        return False

if __name__ == "__main__":
    # Path to your local dataset
    local_file = "data/raw/raw_tweets.csv" 
    
    print(f"Starting upload for {local_file}...")
    upload_to_hdfs(local_file)
  
