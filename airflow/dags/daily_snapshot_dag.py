from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2

def save_daily_snapshot():
    conn = psycopg2.connect(
        database="transit_data",
        user="amithnair",
        password="amith123",
        host="postgres",
        port="5432"
    )
    query = "SELECT * FROM gps_stream;"
    df = pd.read_sql(query, conn)
    df.to_csv(f'/opt/airflow/snapshots/snapshot_{datetime.today().date()}.csv', index=False)
    conn.close()

with DAG(
    dag_id="daily_snapshot_dag",
    start_date=datetime(2025, 8, 1),
    schedule="@daily",
    catchup=False
) as dag:
    task = PythonOperator(
        task_id="save_snapshot",
        python_callable=save_daily_snapshot
    )
