### GSC to BQ
Este repositório contém o código-fonte de um projeto que utiliza o Apache Airflow para criar um fluxo de trabalho que copia arquivos do Google Cloud Storage (GCS) para o BigQuery. O código é responsável por realizar a ingestão de dados, transformação e carregamento em uma tabela específica no BigQuery.

### Pré-requisitos
Antes de executar o código, certifique-se de ter as seguintes dependências instaladas:

Apache Airflow: É necessário ter o Airflow instalado para executar o fluxo de trabalho.
Google Cloud SDK: É necessário ter o SDK do Google Cloud instalado para acessar os serviços do GCS e BigQuery.

### Configuração
Antes de executar o código, é necessário fazer algumas configurações:

Configure a conectividade entre o Airflow e o Google Cloud Platform (GCP) utilizando um arquivo de chave no formato JSON. Certifique-se de fornecer o arquivo de chave correto no diretório especificado em template_searchpath.

Crie um novo bucket no GCS chamado bucket_raw_jr, que será usado como destino para os arquivos a serem copiados.

Crie um dataset no BigQuery chamado my-dataset, que será usado como destino para os dados a serem carregados.

Certifique-se de ter uma conexão válida com o GCP configurada no Airflow. Certifique-se de configurar corretamente as credenciais de conexão no arquivo airflow.cfg ou na interface do Airflow, de acordo com a documentação do Airflow.

### Execução
Após configurar corretamente o ambiente, siga as etapas abaixo para executar o projeto:

Certifique-se de que o Airflow esteja em execução.

Certifique-se de que o código esteja no local correto em seu sistema.

Execute o código. O fluxo de trabalho será iniciado automaticamente de acordo com a programação definida em start_date e schedule_interval.

### Personalização
Se necessário, você pode personalizar o código para atender às suas necessidades. Aqui estão algumas opções de personalização:

Arquivos de origem e destino: No código atual, os arquivos são copiados do bucket datalake_jr para o bucket bucket_raw_jr. Se você quiser copiar arquivos de outros buckets, atualize os valores de bucket_name_datalake e bucket_name_raw de acordo.

Tabelas do BigQuery: No código atual, os dados são carregados em uma tabela específica chamada tb_vendas no dataset venda. Se você quiser usar um dataset ou tabela diferente, atualize os valores de DATASET_CURATED e TABELA_CURATED de acordo.