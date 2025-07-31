import streamlit as st
import pandas as pd
import psycopg2
import time

st.set_page_config(page_title="Transit Dashboard", layout="wide")

# Connect to PostgreSQL
@st.cache_data(ttl=10)  # refresh every 10 seconds
def load_data():
    conn = psycopg2.connect(
        dbname="transit_data",
        user="amithnair",
        password="amith123",
        host="localhost",
        port="5432"
    )
    query = """
        SELECT vehicle_id, route, latitude, longitude, speed_kmph, timestamp
        FROM gps_stream
        ORDER BY timestamp DESC
        LIMIT 50
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("🚍 Real-Time Transit Dashboard")
st.markdown("Live updates every 10 seconds")

data = load_data()

# Show table
st.subheader("📋 Latest Vehicle Data")
st.dataframe(data)

# Show map
st.subheader("🗺️ Live Map")
st.map(data[['latitude', 'longitude']])

# Optional: Speed chart
st.subheader("📈 Speed Trend")
st.line_chart(data[['speed_kmph']])
