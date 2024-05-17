# PASSO 4

## Insersão de informações no banco após o update de dados (DML - Data Manipulation Language)

# Definir a base de dados que será utilizada: use nome_do_banco(schema);
use produtos;

# Atualização dados na tabela do banco de dados(Schema) definido após o Update: insert into nome_da_tabela (Dados da tabela)
insert into pecas (nome, quantidade_estoque, vendas)
value ('Cabo Sata', '180', '0');