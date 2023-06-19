# [StART documentation]
# create new bucket - bucket_raw_jr [GCSCreateBucketOperator]
# sync files from raw-zone to ingesting-zone [GCSSynchronizeBucketsOperator] 
# list objects on the ingesting-zone [GCSListObjectsOperator]
# create dataset on bigquery [BigQueryCrateEmptyDatasetOperator]
# ingest data from gcs to bigquery [GCSToBigQueryOperator]
# delete bucket junior-lafuente [GCSDeleteBucketOperator]
# senha postgres: airflow
# [END documentation]


from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.google.cloud.operators.gcs import GCSCreateBucketOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyTableOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator

project_id = 'semiotic-joy-379201'
region = 'us-central1'
bucket_name_raw = 'bucket_raw_jr'
dataset_name = 'venda'
tabela_name = 'tb_vendas'
bucket_name_datalake = 'datalake_jr'
function_code_bucket = 'bucket_raw_jr'  

default_args = {
    'owner': 'Junior Lafuente',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='create_infra',
    tags=['cloud storage', 'dataset', 'table'],
    default_args=default_args,
    start_date=datetime(year=2023, month=5,day=10),
    schedule_interval='@daily',
    catchup=False,
    #template_searchpath='gs://us-central1-composer-jr-28ae48d5-bucket/sql/'
) as dag:
    

    # Cria um bucket do Cloud Storage para armazenar os arquivos de entrada e saída do processo
    create_bucket_raw = GCSCreateBucketOperator(
        task_id='create_bucket_raw',
        bucket_name=bucket_name_raw,
        location=region,
        storage_class='STANDARD',
        project_id=project_id,
        gcp_conn_id='gcp',
        dag=dag,
    )


    create_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_dataset',
        dataset_id=dataset_name,
        project_id=project_id,
        gcp_conn_id='gcp',
        dag=dag,
    )

    # Criando tabela no bigquery passando schema_fields
    create_table_bq = BigQueryCreateEmptyTableOperator(
        task_id='create_table_bq',
        dataset_id=dataset_name,
        table_id=tabela_name,
        project_id=project_id,
        schema_fields=[
            {'name': 'ID_MARCA', 'type': 'INTEGER'},
            {'name': 'MARCA', 'type': 'STRING'},
            {'name': 'ID_LINHA', 'type': 'INTEGER'},
            {'name': 'LINHA', 'type': 'STRING'},
            {'name': 'DATA_VENDA', 'type': 'DATE'},
            {'name': 'QTD_VENDA', 'type': 'INTEGER'}   
        ],
        gcp_conn_id="gcp",
        dag=dag,
    )
    
    #criando tabela no bigquery atraves de um script SQLa
    #create_table_bq = BigQueryExecuteQueryOperator(
    #    task_id='create_table_bq',
    #    sql='create_table_bq.sql',
    #    use_legacy_sql=False,
    #    gcp_conn_id="gcp",
    #    dag=dag,
    #)

    
create_bucket_raw >> create_dataset >> create_table_bq

