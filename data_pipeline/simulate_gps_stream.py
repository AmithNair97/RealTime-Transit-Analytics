from faker import Faker
import random
import time
import json
from datetime import datetime
from kafka import KafkaProducer

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_vehicle_data():
    return {
        "vehicle_id": f"BUS{random.randint(100, 999)}",
        "route": random.choice(["RouteA", "RouteB", "RouteC"]),
        "latitude": float(round(fake.latitude(), 6)),
        "longitude": float(round(fake.longitude(), 6)),
        "speed_kmph": round(random.uniform(20, 80), 2),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

if __name__ == "__main__":
    topic = "transit_gps"
    while True:
        data = generate_vehicle_data()
        producer.send(topic, value=data)
        print(f"Sent to Kafka: {data}")
        time.sleep(2)
