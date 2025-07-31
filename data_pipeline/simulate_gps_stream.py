from faker import Faker
import random
import time
import json
from datetime import datetime

fake = Faker()

def generate_vehicle_data():
    return {
        "vehicle_id": f"BUS{random.randint(100, 999)}",
        "route": random.choice(["RouteA", "RouteB", "RouteC"]),
        "latitude": float(round(fake.latitude(), 6)),    # <-- FIXED
        "longitude": float(round(fake.longitude(), 6)),  # <-- FIXED
        "speed_kmph": round(random.uniform(20, 80), 2),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

if __name__ == "__main__":
    while True:
        data = generate_vehicle_data()
        print(json.dumps(data))
        time.sleep(2)
