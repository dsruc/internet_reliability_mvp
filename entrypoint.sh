#!/usr/bin/env bash
set -e

export AIRFLOW__CORE__EXECUTOR=LocalExecutor
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres:5432/airflow
export AIRFLOW__CORE__LOAD_EXAMPLES=false

airflow db init
exec airflow webserver