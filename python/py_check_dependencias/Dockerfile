# Usar uma imagem base com Python
FROM python:3.13-rc-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar arquivos de requisitos e instalar dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir Flask requests --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host=files.pythonhosted.org

# Copiar o código da aplicação para o contêiner
COPY . .

# Definir a variável de ambiente para o Flask
ENV FLASK_APP=py_check_dependencias.py

# Expor a porta em que a aplicação Flask estará rodando
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
