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


