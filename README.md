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
```
### 2. Start Required Services
Start Kafka, Zookeeper, PostgreSQL, and Airflow using Docker Compose:

```bash
docker-compose up -d --build
```
Check if all services are running:
```bash
docker ps
```
### 3. Simulate GPS Data
```bash
cd airflow/data_pipeline
python simulate_gps_stream.py
```
### 4. Consume Data and Load into PostgreSQL
```bash
python kafka_consumer_to_postgres.py
```
Optionally, you can log data to a CSV file for debugging or backup:
```bash
python kafka_consumer_to_csv.py
```
### 5. Launch Streamlit Dashboard
```bash
cd streamlit_dashboard
streamlit run app.py
```
Access the dashboard at:
```bash
[cd streamlit_dashboard
streamlit run app.py](http://localhost:8501
)
```
