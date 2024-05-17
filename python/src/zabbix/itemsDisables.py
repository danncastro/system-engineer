import requests
import json

# Configurações do Zabbix
zabbix_url = 'http://ip_servidor/zabbix/api_jsonrpc.php'
zabbix_username = 'usuario'
zabbix_password = 'senha'


# Autenticação no Zabbix API
auth_payload = {
    'jsonrpc': '2.0',
    'method': 'user.login',
    'params': {
        'user': zabbix_username,
        'password': zabbix_password
    },
    'id': 1
}

response = requests.post(zabbix_url, json=auth_payload)
auth_result = response.json()

# Verifique se a autenticação foi bem-sucedida
if 'result' in auth_result:
    auth_token = auth_result['result']
    print(f"Autenticação bem-sucedida. Token: {auth_token}")

    # Consulta de itens desabilitados
    item_payload = {
        'jsonrpc': '2.0',
        'method': 'item.get',
        'params': {
            'output': 'extend',
            'filter': {'status': 1},  # Itens desabilitados têm status 1
            'selectHosts': ['host'],
            'selectApplications': ['name'],
        },
        'auth': auth_token,
        'id': 2
    }

    response = requests.post(zabbix_url, json=item_payload)
    item_result = response.json()

    # Filtrar e formatar os resultados
    filtered_items = []
    for item in item_result.get('result', []):
        applications = item.get('applications', [])
        if applications:
            app_name = applications[0]['name']
        else:
            app_name = "Nenhuma aplicação associada"
        filtered_item = {
            'name': app_name,
            'key': item['key_'],
            'host': item['hosts'][0]['host'],
        }
        filtered_items.append(filtered_item)

    # Salvar os resultados em um arquivo JSON
    with open('items_desabilitados.json', 'w') as json_file:
        json.dump(filtered_items, json_file, indent=4)

    print(f"Os itens desabilitados foram salvos em 'items_desabilitados.json'")
else:
    print("Falha na autenticação.")