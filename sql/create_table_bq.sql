create table if not exists venda.tb_vendas(
    ID_MARCA integer,
    MARCA string,
    ID_LINHA integer,
    LINHA string,
    DATA_VENDA date,
    QTD_VENDA integer
)
PARTITION BY DATA_VENDA;