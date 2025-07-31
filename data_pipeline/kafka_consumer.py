from kafka import KafkaConsumer
import json

# Create the Kafka Consumer
consumer = KafkaConsumer(
    'transit_gps',  # Topic name
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Start from the beginning if no offset saved
    enable_auto_commit=True,
    group_id='transit-logger-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🚀 Consumer started. Waiting for GPS data...")

# Continuously listen for new messages
for message in consumer:
    data = message.value
    print(f"🛰️ Received: {data}")
