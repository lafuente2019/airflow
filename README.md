
Create Infrastructure
Este código implementa um fluxo de trabalho no Apache Airflow para criar infraestrutura de armazenamento e tabelas no Google Cloud Platform. O fluxo de trabalho consiste nos seguintes passos:

Criação de um bucket no Cloud Storage: O operador GCSCreateBucketOperator é utilizado para criar um novo bucket chamado bucket_raw_jr no local us-central1 com a classe de armazenamento padrão.

Criação de um dataset no BigQuery: O operador BigQueryCreateEmptyDatasetOperator é utilizado para criar um dataset chamado venda no projeto semiotic-joy-379201.

Criação de uma tabela no BigQuery: O operador BigQueryCreateEmptyTableOperator é utilizado para criar uma tabela chamada tb_vendas dentro do dataset venda. A tabela possui os seguintes campos: ID_MARCA (INTEGER), MARCA (STRING), ID_LINHA (INTEGER), LINHA (STRING), DATA_VENDA (DATE) e QTD_VENDA (INTEGER).

Configuração
Antes de executar o código, verifique se as seguintes informações estão configuradas corretamente:

project_id: ID do projeto no Google Cloud Platform (no exemplo, é definido como 'semiotic-joy-379201').
region: Região onde o bucket será criado (no exemplo, é definido como 'us-central1').
bucket_name_raw: Nome do bucket a ser criado no Cloud Storage para armazenar os arquivos de entrada e saída (no exemplo, é definido como 'bucket_raw_jr').
dataset_name: Nome do dataset a ser criado no BigQuery (no exemplo, é definido como 'venda').
tabela_name: Nome da tabela a ser criada no BigQuery (no exemplo, é definido como 'tb_vendas').
DAG
A DAG (Directed Acyclic Graph) create_infra é criada com as seguintes configurações:

default_args: Configurações padrão para as tarefas da DAG.
start_date: Data de início da DAG (no exemplo, é definido como 10 de maio de 2023).
schedule_interval: Frequência de execução da DAG (no exemplo, é definido como '@daily' para executar diariamente).
catchup: Define se a DAG deve fazer recuperação de tarefas em atraso.
O fluxo do DAG é o seguinte:
    create_bucket_raw >> create_dataset >> create_table_bq
