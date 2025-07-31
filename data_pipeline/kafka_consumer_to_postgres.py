from kafka import KafkaConsumer
import psycopg2
import json
from datetime import datetime

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="transit_data",
    user="amithnair",
    password="amith123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Kafka Consumer setup
consumer = KafkaConsumer(
    'transit_gps',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='postgres-writer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🚀 Writing GPS data to PostgreSQL...")

for message in consumer:
    data = message.value
    timestamp = datetime.fromisoformat(data['timestamp'].replace("Z", ""))
    cursor.execute("""
        INSERT INTO gps_stream (vehicle_id, route, latitude, longitude, speed_kmph, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        data['vehicle_id'],
        data['route'],
        data['latitude'],
        data['longitude'],
        data['speed_kmph'],
        timestamp
    ))
    conn.commit()
    print(f"✅ Inserted: {data}")
