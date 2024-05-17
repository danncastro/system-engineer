import requests
import json

# Defina as informações do servidor Zabbix
zabbix_api_url = 'http://ip_servidor/zabbix/api_jsonrpc.php'
zabbix_user = 'usuario'
zabbix_password = 'senha'

# Autenticação na API do Zabbix
auth_data = {
    'jsonrpc': '2.0',
    'method': 'user.login',
    'params': {
        'user': zabbix_user,
        'password': zabbix_password,
    },
    'id': 1,
}

response = requests.post(zabbix_api_url, json=auth_data)
auth_result = response.json()

if 'result' in auth_result:
    auth_token = auth_result['result']
    print(f"Autenticação bem-sucedida. Token: {auth_token}")

    # Consulta para obter hosts desabilitados
    disabled_hosts_data = {
        'jsonrpc': '2.0',
        'method': 'host.get',
        'params': {
            'output': ['host'],
            'filter': {'status': 1},  # 1 representa hosts desabilitados
            'selectGroups': ['groupid', 'name'],
            'selectInterfaces': ['ip'],
        },
        'auth': auth_token,
        'id': 2,
    }

    response = requests.post(zabbix_api_url, json=disabled_hosts_data)
    disabled_hosts_result = response.json()

    # Organizar os hosts por grupos em um dicionário
    grouped_hosts = {}
    for host_data in disabled_hosts_result['result']:
        for group_data in host_data['groups']:
            group_name = group_data['name']
            host_name = host_data['host']
            if group_name not in grouped_hosts:
                grouped_hosts[group_name] = []
            grouped_hosts[group_name].append(host_name)

    # Gerar JSON com os hosts desabilitados por grupo
    with open('hosts_desabilitados.json', 'w') as json_file:
        json.dump(grouped_hosts, json_file, indent=4)

    print("JSON com hosts desabilitados por grupo gerado com sucesso.")

else:
    print("Falha na autenticação.")