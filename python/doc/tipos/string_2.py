# Tipo String: Acessando os indices

nome = 'Danniel Gutierres'
nome2 = 'Isabella Carvalho'

print(f'Retorna o elemento de indice 0 atribuido a variavel - [{nome[0]}]')
print(f'Retorna o elemento de indice 6 atribuido a variavel - [{nome[6]}]')
print(f'Nesse caso a contagem começará de trás para frente contadas apartir do indice -1..-2... até o indice -11 que equivale ao elemento de indice 6 - [{nome[-11]}]')
print(f'Retorna um range de elementos começados a partir do indice 4 para frente - [{nome[8:]}]')
print(f'Retorna um range de elementos começados a partir do ultimo elemento dos indices, ou seja de trás para frente - [{nome[-9:]}]')
print(f'Retorna um range de elementos começados pelo indice 0 até a quantidade de elementos informados - [{nome[:8]}]')
print(f'Retorna um range de elementos começados no elemento de indice 6 até o elemento de indice 9 - [{nome[6:9]}]')

numeros = '1234567890'
print(f'Retorna todos os elementos atribuidos a variavel - [{numeros}]')
print(f'Também retornará todos os elementos atribuidos, pois não passamos nenhum range, ou indice especifico - [{numeros}]'[::])
print(f'Retorna os elementos atribuidos na variavel pulando de 2 em 2 indices - [{numeros[::2]}]')
print(f'Retorna os elementos atribuidos na variavel pulando de 2 em 2 indices começados apartir do indice 1, incluindo ele - [{numeros[1::2]}]')
print(f'Retorna os elementos de forma invertida - [{numeros[::-1]}]')
print(f'Retorna os elementos de forma invertida pulando de 2 em 2 indices - [{numeros[::-2]}]')

# Exemplo
print(nome[::-1])
print(nome2[::-1])
