# Tipo Tuplas: Não é possivel alterar os elementos atribuidos

tupla = tuple()
print(f'Retorna qual o tipo de dado foi atribuido a variavel - [{type(tupla)}]')
tupla = ()
print(f'Retorna qual o tipo de dado foi atribuido a variavel - [{type(tupla)}]')

print(f'Retorna as funcionalidades disponiveis [{dir(tupla)}]')

# help(tuple) - Retorna uma ajuda sobre as funcionalidades disponiveis na tupla

tupla = ('Um')
print(f'Retorna qual o tipo de dado foi atribuido a variavel - [{type(tupla)}]')

tupla = ('Um',)
print(f'Retorna qual o tipo de dado foi atribuido a variavel, para ser considerado tupla, mesmo que de apenas 1 unico elemento, precisa atribuir uma virgula - [{type(tupla)}]')

nomes = ('Ana', 'Bia', 'Gui', 'ana')
#          0      1      2      3
#          0     -3     -2     -1

print(f'Retorna um valor booleano(True/False), caso a palavra bia em minusculo esteja atribuido a variavel - [', {'bia' in nomes}, ']')
print(f'Retorna um valor booleano(True/False), caso a palavra Bia com o B maiusculo esteja atribuido a variavel - [', {'Bia' in nomes}, ']')

print(f'Retorna o elemento de indice 0 - [{nomes[0]}]')

# tupla[0] = 'Novo' # Gerará um erro, pois não é possivel a reatribuição de elementos aos indices

print(f'Retorna o elemento de indice -1, contando de trás para frente - [{nomes[-1]}]')
print(f'Retorna os elementos apartir do indice 1 - [{nomes[1:]}]')

print(f'Retorna em qual indice está o elemento Bia - [', nomes.index('Bia'), ']')
print(f'Retorna quantos elementos Bia iguais existem - [', nomes.count('Bia'), ']')

print(f'Retorna a quantidade de elementos - [{len(nomes)}]')
