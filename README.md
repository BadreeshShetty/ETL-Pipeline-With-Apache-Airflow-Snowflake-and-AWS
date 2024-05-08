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

 pip install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
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

 Execute the below code to start the server:
------------------------------------------------
airflow db init
airflow webserver & (to run airflow in the background)

Open a new terminal & execute the below commands:
----------------------------------------------------------------------------------------
source venv/bin/activate
airflow scheduler
 ```

#### Run the airflow server. 


## 2. Set the snowflake connection 


## 3. Create an airflow connection. 

#### Run the airflow dags. 
