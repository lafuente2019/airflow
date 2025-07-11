# Projeto Airflow GCP & PostgreSQL

## 📚 Sumário
- [Descrição do projeto](#descrição-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Configuração do projeto](#configuração-do-projeto)
  - [Variáveis para GCP](#variáveis-para-gcp)
  - [Conexões no Airflow](#conexões-no-airflow)
  - [Arquivos SQL](#arquivos-sql)
- [Execução](#execução)
- [Personalização](#personalização)
  - [Conexões PostgreSQL](#conexões-postgresql)
  - [Arquivos SQL customizados](#arquivos-sql-customizados)
  - [Buckets e tabelas no GCP](#buckets-e-tabelas-no-gcp)
- [Fluxo GCS to BQ](#fluxo-gcs-to-bq)
- [Contato](#contato)

---

## 📝 Descrição do projeto

Este repositório contém o código-fonte de dois fluxos de trabalho desenvolvidos com o Apache Airflow:

- **Infraestrutura no Google Cloud Platform (GCP):**
  - Cria buckets no Google Cloud Storage (GCS).
  - Cria datasets e tabelas no BigQuery.
  - Organiza o pipeline em uma DAG chamada `create_infra`.

- **Banco de dados PostgreSQL:**
  - Cria tabelas e insere dados em um banco PostgreSQL.
  - Utiliza scripts SQL versionados e controlados via Airflow.

---

## 🚀 Pré-requisitos

Para executar este projeto, é necessário ter:

- [Apache Airflow](https://airflow.apache.org/) configurado e rodando no seu ambiente.
- [Google Cloud SDK](https://cloud.google.com/sdk) instalado e autenticado.
- Conta no Google Cloud Platform com permissões para criar buckets no GCS e datasets no BigQuery.

---

## ⚙️ Configuração do projeto

### 🔧 Variáveis para GCP

No seu DAG ou ambiente, configure as seguintes variáveis:

- `project_id`: ID do projeto no Google Cloud Platform.
- `region`: Região onde o bucket será criado.
- `bucket_name_raw`: Nome do bucket no GCS para arquivos de entrada e saída.
- `dataset_name`: Nome do dataset no BigQuery.
- `tabela_name`: Nome da tabela no BigQuery.
- `bucket_name_datalake`: Nome do bucket na zona de ingestão (GCS).

### 🔌 Conexões no Airflow

#### PostgreSQL
- Configure uma conexão no Airflow com o ID `postgres-airflow` apontando para seu banco de dados PostgreSQL.
- Se desejar, altere o `postgres_conn_id` no código para corresponder ao ID da sua conexão.

#### Google Cloud
- Configure a conexão `google_cloud_default` no Airflow com seu arquivo JSON de chave de serviço do GCP.

### 📂 Arquivos SQL

Garanta que os seguintes arquivos estejam no diretório configurado em `template_searchpath` no seu DAG do Airflow:

- `create_table_db.sql`
- `insere_dados_table_db.sql`
- `create_table_ed.sql`
- `insere_dados_tb_data_engineering.sql`

---

## ▶️ Execução

Para rodar o pipeline:

1. Certifique-se de que o Airflow está em execução (`airflow webserver` e `airflow scheduler`).
2. Confirme que as conexões e variáveis estão configuradas corretamente no Airflow.
3. O fluxo principal `create_infra` será executado com o seguinte encadeamento:


create_bucket_raw >> create_dataset >> create_table_bq


4. O pipeline do PostgreSQL cria as tabelas e insere dados conforme os arquivos SQL, obedecendo o `start_date` e `schedule_interval` definidos no DAG.

---

## 🛠️ Personalização

### 🔄 Conexões PostgreSQL
Caso utilize outro ID de conexão, ajuste no seu código:
```python
postgres_conn_id="postgres-airflow"
para o ID correspondente ao configurado no Airflow.

✍️ Arquivos SQL customizados
Edite ou substitua os arquivos .sql mencionados para refletir o seu modelo de dados ou novas regras de negócio.

☁️ Buckets e tabelas no GCP
Personalize as variáveis no DAG para utilizar outros buckets e tabelas:

bucket_name_raw e bucket_name_datalake no GCS.

dataset_name e tabela_name no BigQuery.

⛓️ Fluxo GCS to BQ
Este projeto também contém um pipeline para copiar dados do Google Cloud Storage (GCS) para o BigQuery:

Ingestão: copia arquivos do bucket datalake_jr para o bucket_raw_jr.

Carregamento: importa dados para o dataset my-dataset (ou venda) e para a tabela tb_vendas.

Como executar o GCS to BQ
Certifique-se de que o Airflow esteja rodando.

Configure as variáveis bucket_name_datalake, bucket_name_raw, DATASET_CURATED e TABELA_CURATED no DAG conforme seu ambiente.

O fluxo será acionado automaticamente pelo schedule_interval definido.

📬 Contato
Caso tenha dúvidas, sugestões ou queira contribuir, entre em contato pelo e-mail:

css
Copiar
Editar
valterlafuentejunior@gmail.com
🚀 Projeto desenvolvido para facilitar pipelines de dados usando o Airflow em conjunto com GCP e PostgreSQL.
