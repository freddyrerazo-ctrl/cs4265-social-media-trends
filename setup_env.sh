#!/bin/bash

echo "[INFO] Starting Environment Setup..."

# 1. Update and install Java (Required for HBase/Spark)
sudo apt-get update
sudo apt-get install -y default-jdk

# 2. Download and Extract HBase (Version 2.5.5 - Stable)
if [ ! -d "hbase-2.5.5" ]; then
    echo "[INFO] Downloading HBase..."
    wget https://archive.apache.org/dist/hbase/2.5.5/hbase-2.5.5-bin.tar.gz
    tar -xzf hbase-2.5.5-bin.tar.gz
fi

# 3. Set Environment Variables
export HBASE_HOME=$PWD/hbase-2.5.5
export PATH=$PATH:$HBASE_HOME/bin
export JAVA_HOME=/usr/lib/jvm/default-java

# 4. Configure HBase for Standalone Mode
# This ensures it runs without a full Hadoop cluster
mkdir -p ./hbase_data
cat <<EOF > $HBASE_HOME/conf/hbase-site.xml
<configuration>
  <property>
    <name>hbase.rootdir</name>
    <value>file://$PWD/hbase_data</value>
  </property>
  <property>
    <name>hbase.zookeeper.property.dataDir</name>
    <value>$PWD/hbase_data/zookeeper</value>
  </property>
</configuration>
EOF

# 5. Start HBase
echo "[INFO] Starting HBase Master..."
$HBASE_HOME/bin/start-hbase.sh

# 6. Start Thrift Server (Port 9090)
echo "[INFO] Starting Thrift Server for Python connection..."
$HBASE_HOME/bin/hbase-daemon.sh start thrift -p 9090

# 7. Install Python Dependencies
pip install -r requirements.txt

echo "[SUCCESS] Environment is ready. You can now run 'python3 main.py'"