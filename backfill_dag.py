from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from datetime import date, datetime, timedelta

def dag_args():
    args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime.combine((date.today() - timedelta(days=7)), datetime.min.time()),
        'email': ['MLOperations@tele2.onmicrosoft.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=2),
        'concurrency': 1
    }

    return args


dag = DAG("test-back-fill",
          default_args=dag_args(),
          schedule_interval=timedelta(days=1))


doing_nothing = DummyOperator(
    task_id='doing-nothing',
    dag=dag,
)
