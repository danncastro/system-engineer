# PASSO 7

## Removendo informações de dados do banco

# Definir a base de dados que será utilizada: use nome_do_banco(schema);
use produtos;

# Acessando informações de uma tabela do banco de dados: select * from nome_da_tabela
select * from pecas;

# Removendo linha de uma coluna especifica do banco de dados: 
# delete from nome_da_tabela where identificador='valor';
delete from pecas where id='4';

# Adicionando uma nova linha para validar o identificador: 
# insert into nome_da_tabela (colunas) value ('coluna1', 'coluna2', 'coluna3')
insert into pecas (nome, quantidade_estoque, vendas) value ('Placa de video', '300', '185');

# Validando as informações atribuidas a tabela do banco: select * from nome_da_tabela;
select * from pecas;