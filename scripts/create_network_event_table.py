import psycopg2
import time

# ждём Postgres, потому что Docker — не магия
time.sleep(5)

conn = psycopg2.connect(
    host="postgres",
    port=5432,
    dbname="airflow",
    user="airflow",
    password="airflow"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS network_event (
    id SERIAL PRIMARY KEY,
    ts TIMESTAMP NOT NULL DEFAULT now(),
    check_type TEXT NOT NULL,
    target TEXT NOT NULL,
    latency_ms INTEGER,
    success BOOLEAN NOT NULL,
    error_type TEXT
);
""")

conn.commit()
cur.close()
conn.close()

print("network_event table ensured")