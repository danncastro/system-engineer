import requests
import json

# Configurações do Zabbix API
zabbix_username = 'usuario'
zabbix_password = 'senha'

# Configurações do Zabbix API
url = 'http://ip_servidor/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}

# Autenticação na API do Zabbix
auth_payload = {
    'jsonrpc': '2.0',
    'method': 'user.login',
    'params': {
        'user': zabbix_username,
        'password': zabbix_password,
    },
    'id': 1,
}

response = requests.post(url, data=json.dumps(auth_payload), headers=headers)
result = response.json()

if 'result' in result:
    auth_token = result['result']

    # Obter todas as triggers desativadas
    trigger_payload = {
        'jsonrpc': '2.0',
        'method': 'trigger.get',
        'params': {
            'output': ['description', 'hosts'],
            'filter': {
                'value': 1  # 1 para triggers desativadas, 0 para ativadas
            },
            'selectHosts': ['hostid', 'host'],
        },
        'auth': auth_token,
        'id': 2,
    }

    response = requests.post(url, data=json.dumps(trigger_payload), headers=headers)
    result = response.json()

    if 'result' in result:
        triggers = result['result']

        # Extrair informações dos hosts e criar um JSON
        host_info = {}
        for trigger in triggers:
            for host in trigger['hosts']:
                host_info[host['host']] = {
                    'description': trigger['description'],
                }

        # Salvar as informações em um arquivo JSON
        with open('triggers_desativadas.json', 'w') as json_file:
            json.dump(host_info, json_file, indent=4)

    else:
        print("Erro ao obter triggers desativadas:", result['error']['data'])

else:
    print("Erro ao autenticar no Zabbix:", result['error']['data'])
