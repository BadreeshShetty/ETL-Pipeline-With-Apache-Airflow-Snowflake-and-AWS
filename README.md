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
 ```

#### Run the airflow server. 


## 2. Set the snowflake connection 


## 3. Create an airflow connection. 

#### Run the airflow dags. 
