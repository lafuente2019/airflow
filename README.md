# START Documentation

Este código implementa um fluxo de trabalho no Apache Airflow para criar infraestrutura de armazenamento e tabelas no Google Cloud Platform. O fluxo de trabalho consiste nos seguintes passos:

1. Criação de um novo bucket no Cloud Storage - `bucket_raw_jr` - utilizando o operador `GCSCreateBucketOperator`.
2. Sincronização de arquivos da zona raw para a zona de ingestão no Cloud Storage utilizando o operador `GCSSynchronizeBucketsOperator`.
3. Listagem de objetos na zona de ingestão do Cloud Storage utilizando o operador `GCSListObjectsOperator`.
4. Criação de um dataset vazio no BigQuery utilizando o operador `BigQueryCreateEmptyDatasetOperator`.
5. Ingestão de dados do Cloud Storage para o BigQuery utilizando o operador `GCSToBigQueryOperator`.
6. Exclusão do bucket `junior-lafuente` utilizando o operador `GCSDeleteBucketOperator`.

### Configuração

Certifique-se de ter as seguintes informações configuradas corretamente:

- `project_id`: ID do projeto no Google Cloud Platform.
- `region`: Região onde o bucket será criado.
- `bucket_name_raw`: Nome do bucket a ser criado no Cloud Storage para armazenar os arquivos de entrada e saída.
- `dataset_name`: Nome do dataset a ser criado no BigQuery.
- `tabela_name`: Nome da tabela a ser criada no BigQuery.
- `bucket_name_datalake`: Nome do bucket a ser sincronizado na zona de ingestão.

### DAG

A DAG (Directed Acyclic Graph) `create_infra` é criada com as seguintes configurações:

- `default_args`: Configurações padrão para as tarefas da DAG.
- `start_date`: Data de início da DAG.
- `schedule_interval`: Frequência de execução da DAG.

O fluxo do DAG é o seguinte:

create_bucket_raw >> create_dataset >> create_table_bq

Certifique-se de que as dependências e as configurações do ambiente, como conexão com o Google Cloud Platform, estejam corretamente configuradas antes de executar a DAG.

[END Documentation]
