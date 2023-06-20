### Descrição
Este repositório contém o código-fonte de um projeto que utiliza o Apache Airflow para criar e executar fluxos de trabalho relacionados a tarefas no banco de dados PostgreSQL. O código é responsável por criar tabelas e inserir dados em um banco de dados PostgreSQL usando operadores do Airflow.

### Dependências
Certifique-se de ter as seguintes dependências instaladas antes de executar o código:

Apache Airflow: É necessário ter o Airflow instalado para executar o fluxo de trabalho.

### Configuração
Antes de executar o código, é necessário fazer algumas configurações:
1. Certifique-se de ter uma conexão válida com o banco de dados PostgreSQL configurada no Airflow. O código utiliza a conexão postgres-airflow, portanto, certifique-se de configurar essa conexão no Airflow ou atualize o valor postgres_conn_id nos operadores do código para corresponder à conexão desejada.

2. Verifique se os arquivos SQL necessários estão presentes no diretório especificado em template_searchpath. Os arquivos create_table_db.sql, insere_dados_table_db.sql, create_table_ed.sql e insere_dados_tb_data_engineering.sql devem estar disponíveis nesse diretório.

### Execução
Após configurar corretamente o ambiente, siga as etapas abaixo para executar o projeto:

1. Certifique-se de que o Airflow esteja em execução.

2. Certifique-se de que o código esteja no local correto em seu sistema.

3. Certifique-se de que os arquivos SQL necessários estejam presentes no diretório especificado em template_searchpath.

4. Execute o código. O fluxo de trabalho será iniciado automaticamente de acordo com a programação definida em start_date e schedule_interval.

### Personalização
Se necessário, você pode personalizar o código para atender às suas necessidades. Aqui estão algumas opções de personalização:

* Atualize as conexões do PostgreSQL: No código atual, está sendo utilizada a conexão postgres-airflow. Se você quiser usar uma conexão diferente, atualize o valor de postgres_conn_id em cada operador para corresponder à sua conexão desejada.

* Atualize os arquivos SQL: Os arquivos SQL utilizados neste código são create_table_db.sql, insere_dados_table_db.sql, create_table_ed.sql e insere_dados_tb_data_engineering.sql. Se você precisar criar ou modificar tabelas ou inserir dados diferentes, atualize esses arquivos SQL de acordo.

### Contato
Se você tiver alguma dúvida ou sugestão relacionada a este projeto, sinta-se à vontade para entrar em contato valterlafuentejunior@gmail.com