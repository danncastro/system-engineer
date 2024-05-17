# Dependências necessarias

- python 3.12+
- pip
- pyqt5

## Ferramentas necessárias

- pyqt5-tools
- mysql-community
- mysql-connector-python
- pyinstaller

### Tornando codigo executavel

- pyinstaller --windowed formulario.py

## Subindo Mysql in Docker

### Baixar uma imagem do Mysql

- docker pull mysql/mysql-server

### Executando container padrão

- docker run -d --name mysql_server -e MYSQL_ROOT_PASSWORD=1234 mysql/mysql-server

### Persistencia de dados

- docker container run -dit --name mysql_server --name mysql_server -e MYSQL_ROOT_PASSWORD=1234 -v /home/pmysql/projects-python/py_pmysql/database/cadastroProdutos/volumes:/var/lib/mysql mysql/mysql-server

### Bind da porta para expor externo

- docker run -d --name mysql_server --env MYSQL_USER=pmysql --env MYSQL_PASSWORD=Senha@123 -v /home/pmysql/projects-python/py_pmysql/database/cadastroProdutos/volumes:/var/lib/mysql -p 3306:3306 mysql/mysql-server

### Configurações de segurança

- MYSQL_RANDOM_ROOT_PASSWORD: define uma senha aleatória para o usuário root do MySQL.
- MYSQL_USER e MYSQL_PASSWORD: cria um usuário com acesso restrito ao banco de dados.
- MYSQL_ROOT_PASSWORD: Cria uma senha para o root
- MYSQL_DATABASE: cria um banco de dados específico para a aplicação

- docker container run -dit --name mysql_server --env MYSQL_RANDOM_ROOT_PASSWORD=yes --env MYSQL_DATABASE=produtos -p 3306:3306 mysql/mysql-server
- docker container logs mysql_server | grep 'GENERATED ROOT PASSWORD:'

- CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'Senha@123';
- GRANT ALL PRIVILEGES ON *.* TO 'pmysql'@'localhost';
- GRANT ALL PRIVILEGES ON nome_database.* TO 'pmysql'@'%';
- FLUSH PRIVILEGES;
