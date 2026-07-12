from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime

with DAG(
    dag_id="prod_etl_load",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    run_product_job = DatabricksRunNowOperator(
        task_id="run_product_job",
        databricks_conn_id="databricks_default",
        job_id=784847302740087  # Replace with your Databricks Job ID
    )