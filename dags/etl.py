import configparser
from path import Path
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

config = ConfigParser()
config.read_file(open(f"{Path(__file__).parents[0]}/config.cfg"))

user_email = config["etl"]["email"]
retries = config["etl"]["retries"]

main_args = { 
    """
    arguments for use to set up main_dag below;
    default_args asks for a dictionary of arguments
    """
    "owner": "airflow",
    "depends_on_past": False,
    "email": [user_email],
    "retries": retries,
    "retry_delay": timedelta(minutes = 5)
}

main_dag = DAG(
    "spotfy_dag",
    default_args = main_args
)

etl_dag = PythonOperator(
    task_id = 'spotify_etl_postgres',
    python_callable = spotify_etl_func,
    dag = my_dag
)

etl_dag