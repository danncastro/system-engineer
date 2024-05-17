# Interpolação: Subistituindo valores


# Modelo antigo
nome, idade, idade_f = 'Danniel', 26, 26.4

print('Substituirá o valor de %s pelo valor da String - ', 'Nome: %s' % nome)
print('Substituirá o valor de %d pelo valor Inteiro - ', 'Idade: %d' % idade)
print('Substituirá o valor de %f pelo valor Float - ', 'Idade: %f' % idade_f)
print('Substituirá o valor de %.2f pelo valor Float, arredondando as casas deciais com o .2(Quantidade de casas decimais) - ', 'Idade: %.2f' % idade_f)
print('Substituirá o valor de %r pelo valor Booleano - ', 'Booleanos: %r %r' % (True, False))
print('Substituirá o valor de %s pelo valor Booleano - ', 'Booleanos: %s %s' % (True, False))
print('Substituirá o valor de %d pelo valor Binario - ', 'Binario: %d %d' % (True, False))

# Modelo anteiros ao python 3.6
print('Substituirá os valores dentro das chaves pelos valores das variaveis - ', 'Nome: {} Idade: {}'.format(nome, idade))

# Modelo novo acima do python 3.7
print(f'Substituirá os valores dentro das chaves pelos valores das variaveis de forma mais simples - Nome: {nome} Idade: {idade}')

# Modelo de interpolação com templates
from string import Template

s = Template('Nome: $nome Idade: $idade')
print(f'Retorna a interpolação de variaveis utilizando template - [{s.substitute(nome=nome, idade=idade)}]')