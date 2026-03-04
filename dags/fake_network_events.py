# fake_network_events.py
import random
from datetime import datetime, timedelta
import psycopg2

def generate_fake_events():
    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="postgres"
    )
    cursor = conn.cursor()

    targets = ["server1", "server2", "server3"]
    for _ in range(random.randint(4, 6)):
        ts = datetime.utcnow()
        check_type = "test"
        target = random.choice(targets)
        latency_ms = random.randint(50, 500)
        success = random.choice([True, False])
        error_type = None if success else "timeout"

        cursor.execute(
            """
            INSERT INTO network_event (ts, check_type, target, latency_ms, success, error_type)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (ts, check_type, target, latency_ms, success, error_type)
        )
    conn.commit()
    cursor.close()
    conn.close()