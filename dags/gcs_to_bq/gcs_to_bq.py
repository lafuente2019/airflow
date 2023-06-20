# [START documentation]
# set up connectivity from airflow to gcp using [key] in json format
# create new bucket_raw_jr [GCSCreateBucketOperator] 
# create dataset on bigquery [BigQueryCrateEmptyDatasetOperator]
# ingest data from gcs to bigquery [GCSToBigQueryOperator]
# senha postgres: airflow
# [END documentation]

from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor
from airflow.operators.python_operator import PythonOperator     

project_id = 'semiotic-joy-379201'
region = 'us-central1'
bucket_name_raw = 'bucket_raw_jr'
dataset_name = 'my-dataset'
bucket_name_datalake = 'datalake_jr'
function_code_bucket = 'bucket_raw_jr'

def ingest_dados():
    import pandas as pd
    from google.cloud import storage
    from google.cloud import bigquery 
    from google.oauth2 import service_account
    import os
    import gcsfs
    import openpyxl

    
    DATASET_CURATED = f'venda'
    TABELA_CURATED = f'tb_vendas'

    client = bigquery.Client()
    

    table = client.get_table(f'{DATASET_CURATED}.{TABELA_CURATED}')
    print(table)

    generated_schema = [{'name':i.name, 'type':i.field_type} for i in table.schema]
    print(generated_schema)

    df = pd.read_excel(f"gs://bucket_raw_jr/input/Base 2017.xlsx")
    print(df.head())

    df.to_parquet('gs://bucket_raw_jr/input/Base 2017.parquet')

    df_final = pd.read_parquet('gs://bucket_raw_jr/input/Base 2017.parquet')

    print(df_final.head())
    
    # Carregando dados no BQ
    df_final.to_gbq(
                    destination_table= f'{DATASET_CURATED}.{TABELA_CURATED}',
                    table_schema = generated_schema,  
                    if_exists='append')
    

   
   
default_args = {
    'owner': 'Junior Lafuente',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='gsc_to_bq',
    tags=['cloud storage', 'google bigquery'],
    default_args=default_args,
    start_date=datetime(year=2023, month=3,day=23),
    schedule_interval='@daily',
    template_searchpath='/home/airflow/gcs/key',
    catchup=False
) as dag:
    

# Copiando arquivo do datalake para o bucket_raw
    copy_files_dataLake_To_bucket_raw = GCSToGCSOperator(
        task_id="copy_files_dataLake_To_bucket_raw",
        source_bucket=bucket_name_datalake,
        source_object='input/*.xlsx',
        destination_bucket=bucket_name_raw,
        destination_object='input/',
        move_object=True,
        gcp_conn_id="gcp",
        dag=dag,
    )

    # Create a sensor to wait for the bucket and file to exist
    #gcs_sensor = GCSObjectExistenceSensor(
    #    task_id='gcs_sensor',
    #    bucket=function_code_bucket,
    #    object=function_code_path,
    #    mode='reschedule',
    #    poke_interval=60,
    #    timeout=1200,
    #)

    inges_dado = PythonOperator(
    task_id='inges_dado',
    python_callable=ingest_dados,
    dag=dag,
)

    move_file_to_bkp = GCSToGCSOperator(
        task_id="move_file_to_bkp",
        source_bucket=bucket_name_raw,
        source_object='input/*.xlsx',
        destination_bucket=bucket_name_raw,
        destination_object='backup/',
        move_object=True,
        gcp_conn_id="gcp",
        dag=dag,
    )
    
copy_files_dataLake_To_bucket_raw >> inges_dado >> move_file_to_bkp

