import time
import threading
import socket
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dicionário para armazenar os resultados dos testes
tests = {}

def resolve_domain(domain):
    """Resolve o domínio para um IP, retornando o primeiro IP disponível."""
    try:
        addr_info = socket.getaddrinfo(domain, None)
        return addr_info[0][4][0]  # Retorna o primeiro IP disponível
    except socket.gaierror:
        return "IP não resolvível"

def load_test(url, user_count, test_id):
    """Executa um teste de carga real e registra números de requisição."""
    responses = []

    # Adiciona 'http://' se não houver esquema na URL
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    # Resolve o IP do domínio
    domain = url.split("://")[-1]
    destination_ip = resolve_domain(domain)

    def send_request():
        """Função auxiliar para enviar uma requisição."""
        while not tests[test_id].get('stopped', False):
            start_time = time.time()
            try:
                response = requests.get(url, timeout=5)
                status_code = response.status_code
            except requests.RequestException as e:
                status_code = "Erro"
                print(f"Erro ao fazer a requisição para {url}: {e}")

            response_time = time.time() - start_time

            ip_info = {
                "destination_ip": destination_ip,
                "response_time": response_time,
                "status_code": status_code
            }
            responses.append(ip_info)
            print(f'Requisição feita para: {url}, Tempo de resposta: {response_time:.2f} segundos, IP de Destino: {destination_ip}, Status: {status_code}')

            # Atualiza as respostas
            tests[test_id]['responses'].append(ip_info)

            # Espera um pequeno intervalo antes da próxima requisição
            time.sleep(1)  # Ajuste o intervalo conforme necessário

    # Criar e iniciar várias threads
    threads = []
    for _ in range(user_count):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()

@app.route('/start', methods=['POST'])
def start_test():
    data = request.json
    url = data['url']
    user_count = int(data['users'])  # Lê e converte para inteiro
    test_id = len(tests) + 1

    tests[test_id] = {
        "url": url,
        "responses": [],
        "stopped": False
    }

    thread = threading.Thread(target=load_test, args=(url, user_count, test_id))
    thread.start()

    return jsonify({"test_id": test_id})

@app.route('/stop/<int:test_id>', methods=['POST'])
def stop_test(test_id):
    if test_id in tests:
        tests[test_id]['stopped'] = True
        return jsonify({"message": "Teste parado com sucesso."})
    else:
        return jsonify({"error": "Teste não encontrado."}), 404

@app.route('/results/<int:test_id>', methods=['GET'])
def get_results(test_id):
    if test_id in tests:
        return jsonify(tests[test_id])
    else:
        return jsonify({"error": "Teste não encontrado."}), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
