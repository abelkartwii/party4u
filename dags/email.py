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

my_dag = DAG(
    'spotify_email_dag',
    default_args = my_args,
    description= 'Spotify Weekly Email',
    schedule_interval= '5 14 * * 0'
)

run_email = PythonOperator(
    task_id='spotify_email_weekly',
    python_callable= weekly_email_function,
    dag=my_dag
)
run_email
