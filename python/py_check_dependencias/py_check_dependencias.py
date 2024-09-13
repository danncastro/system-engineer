from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

# Função para carregar configuração do arquivo JSON
def load_config():
    with open('config.json') as f:
        config = json.load(f)
    return config['urls'], config['contacts']

# Função para salvar configuração no arquivo JSON
def save_config(urls, contacts):
    with open('config.json', 'w') as f:
        json.dump({'urls': urls, 'contacts': contacts}, f, indent=4)

# Carregar URLs e informações de contato do arquivo JSON
URLS, CONTACT_INFO = load_config()

def fetch_status_codes(urls):
    results = []
    for item in urls:
        url = item["url"]
        contact = item["contact"]
        component = item.get("component", "")  # Obter o componente se existir
        try:
            response = requests.get(url, timeout=10, allow_redirects=True)
            status_code = response.status_code
            if status_code in {200, 301, 302, 303, 307, 308}:
                status_description = 'up'
            else:
                status_description = 'down'
        except requests.Timeout:
            status_description = 'down'
        except requests.TooManyRedirects:
            status_description = 'down'
        except requests.RequestException as e:
            status_description = 'down'
            print(f"RequestException for URL {url}: {e}")  # Para depuração
        results.append({
            "alias": item["alias"],
            "url": url,
            "status_description": status_description,
            "contact": contact,
            "component": component  # Adicionando o componente aqui
        })
    return results


@app.route('/')
def index():
    status_results = fetch_status_codes(URLS)
    return render_template('index.html', status_results=status_results)

@app.route('/contact/<app_name>')
def contact(app_name):
    contact = CONTACT_INFO.get(app_name, None)
    if not contact:
        return "Informações de contato não disponíveis", 404
    return render_template('contact.html', contact=contact)

@app.route('/add_url', methods=['GET', 'POST'])
def add_url():
    if request.method == 'POST':
        alias = request.form['alias']
        url = request.form['url']
        port = request.form.get('port', '')  # Porta é opcional
        contact = request.form['contact']
        email = request.form['email']
        component = request.form['component']  # Novo campo

        # Adicionar a porta se fornecida
        if port:
            url = f"{url}:{port}"

        # Adicionar nova URL à lista
        new_entry = {"alias": alias, "url": url, "contact": contact, "component": component}
        global URLS, CONTACT_INFO
        URLS.append(new_entry)

        # Adicionar novo contato se ainda não existir
        if contact not in CONTACT_INFO:
            CONTACT_INFO[contact] = {"name": contact, "email": email}

        # Atualizar o arquivo JSON com as novas URLs e contatos
        save_config(URLS, CONTACT_INFO)

        return redirect(url_for('index'))

    return render_template('add_url.html')

@app.route('/edit_url/<int:index>', methods=['GET', 'POST'])
def edit_url(index):
    if index < 0 or index >= len(URLS):
        return "URL não encontrada", 404

    if request.method == 'POST':
        alias = request.form['alias']
        url = request.form['url']
        port = request.form.get('port', '')  # Porta é opcional
        contact = request.form['contact']
        email = request.form['email']
        component = request.form['component']  # Novo campo

        if port:
            url = f"{url}:{port}"

        # Atualizar a URL existente
        URLS[index] = {"alias": alias, "url": url, "contact": contact, "component": component}

        # Atualizar ou adicionar contato
        if contact not in CONTACT_INFO:
            CONTACT_INFO[contact] = {"name": contact, "email": email}

        # Salvar as alterações
        save_config(URLS, CONTACT_INFO)

        return redirect(url_for('index'))

    # Carregar dados para o formulário
    url_entry = URLS[index]
    return render_template('edit_url.html', url_entry=url_entry, index=index)

if __name__ == '__main__':
    app.run(debug=True)
