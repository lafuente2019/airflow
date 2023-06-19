Fluxo de Trabalho para Criação de Infraestrutura no GCP
Este repositório contém um código que implementa um fluxo de trabalho no Apache Airflow para criar infraestrutura de armazenamento e tabelas no Google Cloud Platform (GCP). O objetivo desse fluxo é automatizar a criação dos recursos necessários para processar e armazenar dados no GCP.

Passos do Fluxo de Trabalho
O fluxo de trabalho consiste nos seguintes passos:

Criação de um Bucket no Cloud Storage: Utiliza o operador GCSCreateBucketOperator para criar um novo bucket no Cloud Storage, que será usado para armazenar os arquivos de entrada e saída do processo. O bucket é criado com o nome "bucket_raw_jr" e a classe de armazenamento padrão.

Criação de um Dataset no BigQuery: Utiliza o operador BigQueryCreateEmptyDatasetOperator para criar um novo dataset no BigQuery, que será usado para armazenar as tabelas. O dataset é criado com o nome "venda" no projeto "semiotic-joy-379201".

Criação de uma Tabela no BigQuery: Utiliza o operador BigQueryCreateEmptyTableOperator para criar uma nova tabela no BigQuery. A tabela é criada dentro do dataset "venda" e possui o nome "tb_vendas". Além disso, são definidos os campos e seus tipos: "ID_MARCA" (INTEGER), "MARCA" (STRING), "ID_LINHA" (INTEGER), "LINHA" (STRING), "DATA_VENDA" (DATE) e "QTD_VENDA" (INTEGER).

Configuração
Antes de executar o código, verifique se as seguintes informações estão configuradas corretamente:

project_id: ID do projeto no Google Cloud Platform. No exemplo, o ID do projeto é definido como "semiotic-joy-379201".
region: Região onde o bucket será criado. No exemplo, a região é definida como "us-central1".
bucket_name_raw: Nome do bucket a ser criado no Cloud Storage para armazenar os arquivos de entrada e saída. No exemplo, o nome do bucket é definido como "bucket_raw_jr".
dataset_name: Nome do dataset a ser criado no BigQuery. No exemplo, o nome do dataset é definido como "venda".
tabela_name: Nome da tabela a ser criada no BigQuery. No exemplo, o nome da tabela é definido como "tb_vendas".
DAG (Directed Acyclic Graph)
O fluxo de trabalho é definido como uma DAG chamada "create_infra". A DAG é configurada com os seguintes parâmetros:

default_args: Configurações padrão para as tarefas da DAG.
start_date: Data de início da DAG. No exemplo, a data de início é definida como 10 de maio de 2023.
schedule_interval: Frequência de execução da DAG. No exemplo, a DAG está programada para ser executada diariamente.
catchup: Define se a DAG deve executar tarefas em atraso. No exemplo, o valor é definido como False.
O fluxo da DAG é o seguinte:
create_bucket_raw >> create_dataset >> create_table_bq
