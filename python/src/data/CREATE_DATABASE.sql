# PASSO 1

## Criação da Base de dados e da Tabela (DDL - Data Definition Language)
'''
Principais Tipos de Dados

Text - Para textos longos como comentários por exemplo

Char - Somente caracteres e não é adaptável

Varchar - Até 255 caracteres, sua vantagem é a adaptação para a quantidade utilizada

Números
- Int - Utilizado para números inteiros
- Float - Para números com casas decimais
'''

# Cria o banco de dados(Schema): create database nome_do_banco(schema);
create database produtos;

# Indica qual base de dados(Schema) será utilizada: use nome_do_banco(schema);
use produtos;

# Cria uma tabela dentro do banco indicado: create table nome_da_tabela(
    # Identificação(id/nome/quantidade)
    # Tipo de dados(Text/Char/Varchar/Números)
    # Metodo(auto_increment/not null) Opcional
    # Tipo de Chave(primary/secundary)
# );
create table pecas(
    id int auto_increment primary key,
    nome varchar(70) not null,
    quantidade_estoque int not null
);