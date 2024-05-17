# PASSO 6

## Select no banco de dados utilizando a clausura Where

# Definir a base de dados que será utilizada: use nome_do_banco(schema);
use produtos;

# Acessando informações especifica de uma coluna do banco de dados: select nome_da_coluna from nome_tabela
select vendas from pecas;
select nome, vendas from pecas;
select nome, vendas, quantidade_estoque from pecas;
select nome, vendas, id, quantidade_estoque from pecas;

# Acessando informações especifica de uma coluna filtrando pelos valores:
# select * from nome_tabela where coluna denomidador valor;
select * from pecas where vendas > 0;
select * from pecas where quantidade_estoque < 200;