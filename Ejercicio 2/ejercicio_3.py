import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}
dag = DAG(
    'ejercicio MassMovil',
    default_args=default_args,
    description='Ejercicio Airflow',
    schedule_interval=timedelta(days=1),
)

start = DummyOperator(
    task_id='start',
    dag=dag
)
end = DummyOperator(
    task_id='end'
    dag=dag
    )
end >> start
