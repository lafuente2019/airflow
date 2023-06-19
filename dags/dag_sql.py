from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator



with DAG(
    dag_id='dag_sql', 
    start_date = datetime(2023,3,9), 
    schedule_interval = '@daily',
    tags=['postgres'], 
    catchup=False, 
    template_searchpath='/opt/airflow/sql'
    ) as dag:

    create_table_db = PostgresOperator(
        task_id = 'criar_tabela_db',
        postgres_conn_id = 'postgres-airflow',
        sql = 'create_table_db.sql'

    )

    insere_dados_table_db = PostgresOperator(
        task_id = 'insere_dados_table_db',
        postgres_conn_id = 'postgres-airflow',
        sql = 'insere_dados_table_db.sql'

    )
    create_table_ed = PostgresOperator(
        task_id = 'criar_tabela_ed',
        postgres_conn_id = 'postgres-airflow',
        sql = 'create_table_ed.sql'

    )
    insere_dados_tb_data_engineering = PostgresOperator(
        task_id = 'insere_dados_tb_data_engineering',
        postgres_conn_id = 'postgres-airflow',
        sql = 'insere_dados_tb_data_engineering.sql'

    )
   
create_table_db >> insere_dados_table_db >> create_table_ed >> insere_dados_tb_data_engineering

