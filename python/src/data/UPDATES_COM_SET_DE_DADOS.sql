# PASSO 5

## Update de informações no banco de dadoss: Atualização de dados de uma tabela, setando um item especifico 

# Definir a base de dados que será utilizada: use nome_do_banco(schema);
use produtos;

# Atualiza uma tabela do banco de dados setando um item especifico: 
# update nome_da_tabela set nome_da_coluna = 'Valor' where nome_da_coluna = 'Identificador';
update pecas set vendas = '10' where id = '3';
update pecas set vendas = '80' where id = '5';