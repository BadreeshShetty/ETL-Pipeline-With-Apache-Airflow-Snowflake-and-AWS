import logging
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from news_api import runner

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

args = {"owner": "AbdoulKaled", "start_date": airflow.utils.dates.days_ago(2)}

dag = DAG(
    dag_id="snowflake_automation_dag", default_args=args, schedule_interval=None
)

with dag:
    extract_news_info = PythonOperator(
        task_id='extract_news_info',
        python_callable=runner,
        dag=dag,
    )

    move_file_to_s3 = BashOperator(
        task_id="move_file_to_s3",
        bash_command='aws s3 mv {{ ti.xcom_pull("extract_news_info")}}  s3://gakas-news-datapipeline-airflow',
    )

    snowflake_create_table = SnowflakeOperator(
        task_id="snowflake_create_table",
        sql="""create  table if not exists News_Table using template(select ARRAY_AGG(OBJECT_CONSTRUCT(*)) from TABLE(INFER_SCHEMA (LOCATION=>'@News_DB.PUBLIC.my_s3_parquet_stage',FILE_FORMAT=>'parquet_format')))
        """,
        snowflake_conn_id="snowflake_conn"
    )

    snowflake_copy = SnowflakeOperator(
        task_id="snowflake_copy",
        sql="""copy into news_db.PUBLIC.News_Table from @news_db.PUBLIC.my_s3_parquet_stage MATCH_BY_COLUMN_NAME=CASE_INSENSITIVE FILE_FORMAT=parquet_format
        """,
        snowflake_conn_id="snowflake_conn"
    )

extract_news_info >> move_file_to_s3 >> snowflake_create_table >> snowflake_copy