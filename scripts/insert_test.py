import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="postgres",
    port=5432,
    dbname="airflow",
    user="airflow",
    password="airflow"
)

cur = conn.cursor()

cur.execute(
    """
    INSERT INTO network_event (ts, check_type, target, latency_ms, success, error_type)
    VALUES (%s, %s, %s, %s, %s, %s)
    """,
    (
        datetime.utcnow(),
        "test",
        "dummy",
        123,
        True,
        None
    )
)

conn.commit()
cur.close()
conn.close()