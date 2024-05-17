# PASSO 2

## Insersão de informações no banco (DML - Data Manipulation Language)

# Definir a base de dados que será utilizada: use nome_do_banco(schema);
use produtos;

# Inseri dados na tabela do banco de dados(Schema) definido: insert into nome_da_tabela (Dados da tabela)
insert into pecas (nome, quantidade_estoque)

# Inseri um único valor aos dados da tabela: values ('Info 1(nome)', 'Info 2(quantidade_estoque)');
value ('Placa mãe', '500');

# Inserir varios valores aos dados da tabela: values ('Info 1(nome)', 'Info 2(quantidade_estoque)'), ('Info 1(nome)', 'Info 2(quantidade_estoque)'), ('Info 1(nome)', 'Info 2(quantidade_estoque)')
value ('HD', '300'),
('RAM', '350'),
('Monitor', '50');

# Consultar os dados atribuidos a tablea: select * from nome_da_tabela;
select * from pecas;

# Atualização dados na tabela do banco de dados(Schema) definido após o Update: insert into nome_da_tabela (Dados da tabela)
insert into pecas (nome, quantidade_estoque, vendas)
value ('Cabo Sata', '180', '0');