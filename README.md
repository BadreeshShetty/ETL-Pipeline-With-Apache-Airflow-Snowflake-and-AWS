# ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS
We build an ETL pipeline using Apache Airflow, Snowflake, and AWS Services. Using Airflow, the pipeline fetches All articles about NBA news from the last month, sorted by recent; then, the data is saved on AWS S3 in a parquet format. We configured a storage integration that stores a generated identity and access management (IAM) entity for AWS, and an external table is created as an interface between Snowflake and S3.

![ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS](https://github.com/gakas14/ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS/assets/74584964/f4ac0308-97e2-4fce-821b-139e4b503163)



 

## 1. Set up an EC2 instance(ubuntu image) and run airflow on it: 

#### Create an EC2 instance 

#### Create an IAM role to allow the EC2 to access S3 and attach the role to the EC2 

#### Edit the inbound rules by allowing all traffic from anywhere 

#### Ssh into the EC2, then run the different commands 
```
 sudo apt update
 sudo apt install python3-pip
 sudo apt install sqlite3
 sudo apt-get install libpq-dev
 pip3 install --upgrade awscli

 pip3 install virtualenv
 sudo apt install python3-virtualenv
 virtualenv venv 
 source venv/bin/activate

 pip install "apache-airflow[postgres]==2.5.0" --constraint "https://github.com/gakas14/ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS/blob/main/requirements.txt"
 pip install pandas apache-airflow-providers-snowflake==2.1.0 snowflake-connector-python==2.5.1 snowflake-sqlalchemy==1.2.5
 pip3  install pyarrow fastparquet

 airflow db init
 sudo apt-get install postgresql postgresql-contrib
 sudo -i -u postgres

 psql
 CREATE DATABASE airflow;
 CREATE USER airflow WITH PASSWORD 'airflow';
 GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
 exit

 ls
 cd airflow
 sed -i 's#sqlite:////home/ubuntu/airflow/airflow.db#postgresql+psycopg2://airflow:airflow@localhost/airflow#g' airflow.cfg
 sed -i 's#SequentialExecutor#LocalExecutor#g' airflow.cfg

 airflow db init
 airflow users create -u airflow -f airflow -l airflow -r Admin -e airflow@gmail.com

 User id --airflow
 password--airflow!


 mkdir /home/ubuntu/dags
 cd airflow
 vi airflow.cfg

 change the below properties --
 dags_folder = /home/ubuntu/dags
 load_examples = False

 # Now, put airflow_script.py and sport_news.py files in the dags folder.
-- Copy command--
 scp -i /directory/to/abc.pem /your/local/file/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/file

 ```

#### Run the airflow server. 
```
 Execute the below code to start the server:
------------------------------------------------
airflow db init
airflow webserver & (to run airflow in the background)

Open a new terminal & execute the below commands:
----------------------------------------------------------------------------------------
source venv/bin/activate
airflow scheduler
```

## 2. Set the snowflake connection 
```
use COMPUTE_WH;

-Create Database
create database if not exists News_db;

--use the database
use news_db;

CREATE OR REPLACE file format News_DB.Public.parquet_format
    type = parquet;

-- Create a storage integration object
create or replace storage integration s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE 
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::***********:role/Snowflake_role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://"s3 bucket"/')
  --COMMENT = 'This an optional comment'

-- See storage integration properties to fetch external_id so we can update it in S3
DESC integration s3_int;

-- Create stage object with integration object & file format object
CREATE OR REPLACE stage News_DB.Public.my_s3_parquet_stage
    URL = 's3://"s3 bucket"/'
    STORAGE_INTEGRATION = s3_int
    FILE_FORMAT = News_DB.Public.parquet_format

    
--check the data present in S3
list @News_DB.PUBLIC.my_s3_parquet_stage;

```

## 3. Create an airflow connection. 

<img width="1261" alt="Screen Shot 2024-05-08 at 1 24 29 PM" src="https://github.com/gakas14/ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS/assets/74584964/daaa98ef-7612-49ec-8e8c-b24fe094930f">

<img width="1246" alt="Screen Shot 2024-05-08 at 1 24 40 PM" src="https://github.com/gakas14/ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS/assets/74584964/b611c875-2bdb-4834-97a2-dee1448976c2">

#### Run the airflow dags. 
<img width="1250" alt="Screen Shot 2024-05-08 at 1 29 34 PM" src="https://github.com/gakas14/ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS/assets/74584964/0380b6cc-7806-498c-915c-919d1c2a0555">
