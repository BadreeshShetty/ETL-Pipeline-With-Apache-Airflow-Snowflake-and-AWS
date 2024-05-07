# ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS
We build an ETL pipeline using Apache Airflow, Snowflake, and AWS Services. Using Airflow, the pipeline fetches All articles about NBA news from the last month, sorted by recent; then, the data is saved on AWS S3 in a parquet format, and the S3 bucket will be connected to the Snowflake.
![ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS](https://github.com/gakas14/ETL-Pipeline-With-Apache-Airflow-Snowflake-and-AWS/assets/74584964/f4ac0308-97e2-4fce-821b-139e4b503163)



Write an ETL script with Python. 

Snowflake copy command.

Exchange data between tasks in airflow(using XCOM). 

 

## 1. Set up an EC2 instance(ubuntu image) and run airflow on it: 

#### Create an instance 

#### Create an IAM role to allow the EC2 to access S3 and attach the roe to the EC2 

#### Edit the inbound rules by allowing all traffic from anywhere 

#### Ssh into the EC2, then run the different commands 

#### Open the airflow server. 


## 2. Create an airflow connection. 

#### Run the airflow dags. 


## 3. Set the snowflake connection 



