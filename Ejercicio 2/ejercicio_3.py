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

task_1 =DummyOperator(
            task_id='task_1'
            dag=dag
            )

task_3 =DummyOperator(
            task_id='task_3'
            dag=dag
            )

task_5 =DummyOperator(
            task_id='task_5'
            dag=dag
            )

task_2 =DummyOperator(
            task_id='task_2'
            dag=dag
            )

task_2 >> [task_1, task_3, task_5]

task_4 =DummyOperator(
            task_id='task_4'
            dag=dag
            )

task_4 >> [task_1, task_3, task_5]



