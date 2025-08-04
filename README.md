# 🚦 Real-Time Public Transit Analytics Platform

## 🌍 Overview
This project is a real-time (or simulated) public transit analytics platform that ingests live vehicle location data, processes it through a Kafka-Apache Airflow pipeline, stores it in PostgreSQL, and visualizes it in an interactive dashboard built with Streamlit. It's designed for transit authorities and researchers to monitor transit operations live and extract actionable insights.

## 💡 Key Features
- Real-time or simulated GPS data generation for public buses
- Kafka-based data ingestion pipeline
- Workflow orchestration using Apache Airflow
- Data persistence in PostgreSQL
- Interactive dashboard displaying live vehicle positions and route analytics using Streamlit
- Optional machine learning module for delay forecasting (extendable)

## 🧱 Tech Stack
- **Programming Language:** Python
- **Streaming Platform:** Apache Kafka
- **Workflow Orchestration:** Apache Airflow
- **Database:** PostgreSQL (can be extended to Snowflake)
- **Dashboard:** Streamlit (optional: React.js)
- **Containerization:** Docker + Docker Compose

---

## 🚀 How to Run the Project Locally

### Prerequisites
- Docker and Docker Compose installed
- Python 3.8+
- Optional: Kafka CLI for debugging

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/transit-analytics-platform.git
cd transit-analytics-platform

2. Start Kafka, Zookeeper, PostgreSQL, and Airflow
bash
Copy
Edit
docker-compose up -d --build
✅ Ensure services like Kafka, Zookeeper, and Airflow are running using:
docker ps

3. Simulate GPS Data (Kafka Producer)
Open a new terminal:

cd airflow/data_pipeline
python simulate_gps_stream.py

4. Run Kafka Consumer to PostgreSQL
In a separate terminal:
python kafka_consumer_to_postgres.py
You can also run kafka_consumer_to_csv.py to log output to CSV instead.

5. Launch the Streamlit Dashboard
In a new terminal:

cd streamlit_dashboard
streamlit run app.py

Open browser at: http://localhost:8501

📦 Folder Structure

├── airflow/
│   └── data_pipeline/
│       ├── simulate_gps_stream.py
│       ├── kafka_consumer.py
│       ├── kafka_consumer_to_postgres.py
│       └── kafka_consumer_to_csv.py
├── streamlit_dashboard/
│   └── app.py
├── docker-compose.yml
└── README.md
