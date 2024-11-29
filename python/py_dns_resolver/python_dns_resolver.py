import dns.resolver
import dns.exception
import requests
import json
from datetime import datetime

# Configurações do Zabbix
ZABBIX_API_URL = 'http://zabbix-uh.intranet/zabbix/api_jsonrpc.php'
ZABBIX_API_USER = '*******'
ZABBIX_API_PASSWORD = '*******'
ZABBIX_ITEM_ID = '911294'

# Lista de resolvers a serem testados
resolvers = ["x.x.x.x", "x.x.x.x", "x.x.x.x"]
domain = "uolhost.uol.com.br"

# Lista para armazenar resolvers que falharam
failed_resolvers = []

for resolver_ip in resolvers:
    print(f"Testando resolver {resolver_ip}")
    try:
        # Cria uma instância de Resolver e configura o nameserver
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [resolver_ip]
        
        # Faz a consulta DNS
        answers = resolver.resolve(domain, 'A')
        
        # Exibe os resultados
        for answer in answers:
            print(answer.to_text())
    except dns.exception.DNSException as e:
        # Em caso de erro, exibe a mensagem e adiciona à lista de falhas
        print(f"Erro ao consultar {resolver_ip}: {e}")
        failed_resolvers.append(resolver_ip)
    print()  # Linha em branco para separar as saídas

# Prepara a mensagem para o Zabbix
if failed_resolvers:
    status_message = "Resolvemos falhados: " + " ".join(failed_resolvers)
    zabbix_status = 'CRITICAL'
else:
    status_message = 'Todos os resolvers foram bem-sucedidos.'
    zabbix_status = 'OK'

# Função para autenticar no Zabbix
def authenticate_zabbix():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": ZABBIX_API_USER,
            "password": ZABBIX_API_PASSWORD
        },
        "id": 1
    }
    response = requests.post(ZABBIX_API_URL, headers=headers, data=json.dumps(data))
    result = response.json()
    return result['result']

# Função para enviar o valor para o item via API
def send_to_zabbix(value):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "jsonrpc": "2.0",
        "method": "history.create",
        "params": {
            "itemid": ZABBIX_ITEM_ID,
            "clock": int(datetime.now().timestamp()),  # Timestamp atual
            "value": value
        },
        "auth": zabbix_auth_token,
        "id": 1
    }
    response = requests.post(ZABBIX_API_URL, headers=headers, data=json.dumps(data))
    return response.json()

# Autentica no Zabbix e envia o status
zabbix_auth_token = authenticate_zabbix()
send_to_zabbix(status_message)
