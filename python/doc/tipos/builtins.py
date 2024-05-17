# Builtins: Metodos internos das funções

# help(f'Trás uma tela de ajuda que explica as funcionalidades informadas [{dir}])
# __builtins__.help(__builtins__.dir)

exemplo1 = type(1)
print(f'Retorna qual o tipo de dado foi atribuido a variavel - [{exemplo1}]')

exemplo2 = __builtins__.type('Fala Galera!')
print(f'Retorna qual o tipo de dado foi atribuido a variavel, porém utilizando um metódo interno da função - [{exemplo2}]')

exemplo3 = __builtins__.print('Retorna uma mensagem em tela utilizando um metódo interno da função - [Fala Galera!]') 

print(f'Retorna na tela os elementos adicionados ao escopo global[{dir()}]')
print(f'Retorna na tela as funcionalidades disponibilizadas dentro do método builtins - [{dir(__builtins__)}]')

# Exemplo
nome = 'Danniel Gutierres de Castro'
print(type(nome))
print(__builtins__.len(nome))
print(dir())
