# Tipo lista: Acessando o indice de uma lista

lista = [1, 5, 'Danniel', 'Isabella', 3.1415]

print(f'Retorna em qual indice está o item Danniel - Indice =', [lista.index('Danniel')])

print(f'Retorna o item do indice 2 atribuido a função list - [{lista[2]}]')

print(f'Retorna um valor booleano(True/False) caso o item 1 esteja atribuido a função list - [{1 in lista}]')
print(f'Retorna um valor booleano(True/False) caso o item Isabella esteja atribuido a função list - ', ['Isabella' in lista])
print(f'Retorna um valor booleano(True/False) caso o item Pedro, não esteja atribuido a função list -',  ['Pedro' not in lista])

print(f'Retorna o item de indice 0 atribuido a função list, ou seja o primeiro elemento - [{lista[0]}]')
print(f'Retorna o item de indice 4 atribuido a função list, ou seja o último elemento - [{lista[4]}]') 

# # print(lista[5]) # Retorna um erro, pois está fora do range da lista

print(f'Retorna o último elemento da lista, pois começará contabilizando de trás para frente - [{lista[-1]}]')
print(f'Retorna o item de indice -5 equivalente ao primeiro elemento da lista, pois começado em -1 de trás para frente temos 5 elementos - [{lista[-5]}]')

nova_lista = ['Danniel', 'Castrão', 'Isabella', 'Gutierres', 'Carvalho']
#    Indices =   0     ,     1    ,     2     ,     3      ,     4
# Invertidos =   0          -4         -3          -2           -1

print(f'Retorna os elementos apartir do indice 1 até o indice 3 - [{nova_lista[1:3]}]')
print(f'Retorna os elementos apartir no indice 1 até o indice -1 - [{nova_lista[1:-1]}]')
print(f'Retorna os elementos começados a partir indice 1 - [{nova_lista[1:]}]')
print(f'Retorna os elementos até o indice -1 - [{nova_lista[:-1]}]')
print(f'Retorna todo os elementos da lista - [{nova_lista[:]}]')
print(f'Retorna os elementos da lista pulando de 2 em 2 indices- [{nova_lista[::2]}]')
print(f'Retorna os elementos da lista de forma invertida- [{nova_lista[::-1]}]')

del nova_lista[2] # Remove o segundo indice da lista
print(f'Retorna os elementos da lista sem o indice 2 - [{nova_lista}]')

del nova_lista[1:] # Remove todos os elementos da lista apartir do indice 1
print(f'Retorna os elementos da lista sem o indice 2 - [{nova_lista}]')
