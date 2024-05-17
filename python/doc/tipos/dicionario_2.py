# Tipo Dicionario: Adicionando e removendo atributos

pessoa = {
    'nome': 'Prof. Danniel',
    'idade': '26',
    'cursos': ['React', 'Python']
}

pessoa['idade'] = 27 # Reatribui um valor a chave idade
print(f'Retorna o novo valor que foi atribuido a chave idade - [', pessoa['idade'], ']')

pessoa['cursos'].append('Angular')
print(f'Retorna o novo valor adicionado a lista dentro da chave - [{pessoa}]')

pessoa.pop('idade') # Remove a chave e valor idade
print(f'Retorna os elementos da variavel pessoa, sem o atribudo idade - {pessoa}')

pessoa.update({'idade': 28, 'Sexo': 'M'}) # Adiciona chaves e valores a variavel
print(f'Retorna as novas chaves e valores atribuidas a variavel - [{pessoa}]')

del pessoa['cursos'] # Deleta o elemento cursos da variavel
print(f'Retorna os elementos da variavel, sem o atributo cursos - [{pessoa}]')

pessoa.clear() # Limpa todos os elementos da variavel
print(f'Retorna um dicionario limpo, sem nenhum elemento adicionado - [{pessoa}]')