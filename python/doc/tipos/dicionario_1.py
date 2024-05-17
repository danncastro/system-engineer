# Tipo Dicionario: Elementos de chave e valor

aluno = {
    'nome': 'Danniel Castro',
    'nota': 9.2,
    'ativo': True,
    'doces' : ['Balas', 'Biscoitos']
} # Atribui elementos de chave e valor a variavel ['Key': 'Value']

print(f'Retorna o tipo de dado atribuido a variavel - [{type(aluno)}]')
print(f'Retorna as funcionalidaes disponiveis em dicionaiso - {dir(dict)}')
print(f'Retorna a quantidade de elementos chave e valor atribuidos - [{len(aluno)}]')

print(f'Retorna o valor da chave atribuido a um dos elementos da variavel -', '[', aluno['nome'], ']')
print(f'Retorna o valor da chave atribuido a um dos elementos da variavel -', '[', aluno['nota'], ']')
print(f'Retorna o valor da chave atribuido a um dos elementos da variavel -', '[', aluno['ativo'], ']')
print(f'Retorna o valor da chave atribuido a um dos elementos da variavel -', aluno['doces'])
print(f'Retorna o elemento de indice 1 atribuido ao valor da chave - [', aluno['doces'][1], ']')

print(f'Retorna a quantidade de elementos não repetidos de chave e valor atribuidos a variavel - [{len(aluno)}]')

print(f'Retorna as chaves atribuidas a variavel - [{aluno.keys()}]')
print(f'Retorna os valores atribuidos as chaves - [{aluno.values()}]')
print(f'Retorna a chave e os valores atribuidos as variaveis - [{aluno.items()}]')

print(f'Retorna o valor atribuido a chave - [', {aluno.get('nome')}, ']')
print(f'Retorna um valor padrão caso nada tenha sido atribuido a chave - ', aluno.get('tags', []))