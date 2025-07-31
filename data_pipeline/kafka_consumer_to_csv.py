from kafka import KafkaConsumer
import json
import csv
import os

CSV_FILE = "../data/gps_data.csv"

# Create file and write headers if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["vehicle_id", "route", "latitude", "longitude", "speed_kmph", "timestamp"])

# Kafka consumer setup
consumer = KafkaConsumer(
    'transit_gps',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='csv-writer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("✅ Listening to 'transit_gps' and writing to CSV...")

# Consume and write to CSV
for message in consumer:
    data = message.value
    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            data['vehicle_id'],
            data['route'],
            data['latitude'],
            data['longitude'],
            data['speed_kmph'],
            data['timestamp']
        ])
    print(f"📦 Saved to CSV: {data}")
