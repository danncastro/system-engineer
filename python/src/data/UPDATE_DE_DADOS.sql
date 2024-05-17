# PASSO 3

## Update de informações no banco de dados

# Definir a base de dados que será utilizada: use nome_do_banco(schema);
use produtos;

# Define qual a tabela terá informações atualizadas: alter table nome_da_tabela
alter table pecas

# Adiciona ou Remove uma nova coluna de dados a uma na tabela: add column nova_coluna tipo_de_dados metodos
add column vendas int not null;

# Descreve as informações de uma tabela: desc nome_da_tabela
desc pecas;