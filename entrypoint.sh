#!/usr/bin/env bash
set -e

# Настройки Airflow
export AIRFLOW__CORE__EXECUTOR=LocalExecutor
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres:5432/airflow
export AIRFLOW__CORE__LOAD_EXAMPLES=False

# Инициализация базы Airflow
airflow db init

# Создаём пользователя admin
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password supersecret || true

# Создаём таблицу network_event, если её нет
python /opt/airflow/scripts/create_network_event_table.py

# Запуск scheduler в фоне
airflow scheduler &

# Запуск webserver как основного процесса контейнера
exec airflow webserver