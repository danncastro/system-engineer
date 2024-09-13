# Execução codigo 2

1. Criar um Ambiente Virtual

~~~
python -m venv venv
~~~

2. Ativar o Ambiente Virtual

~~~
source venv/bin/activate
~~~

3. Instalar Dependências

~~~
pip install flask requests --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host=files.pythonhosted.or
~~~

Se você tiver um arquivo requirements.txt com as dependências do projeto, você pode instalá-las todas de uma vez com

~~~
pip install -r requirements.txt
~~~

4. Executar a Aplicação Flask

~~~
python app.py
~~~

5. Desativar o Ambiente Virtual

~~~
deactivate
~~~


Explicação do Código:
Importações: Importa Flask e a função requests.get para obter o status das URLs.
Lista de URLs: Define as URLs que você deseja monitorar.
Função check_url: Verifica o status da URL. Se houver um erro, retorna a mensagem de erro.
Rota Principal (/): A função index gera um dicionário com os status das URLs e usa render_template_string para renderizar o HTML com esses dados.
Execução da Aplicação: app.run(debug=True) inicia o servidor Flask em modo de depuração.
