# Tipo String: Metodos magicos

a = '123'
b = ' de Oliveira 4'

print(f'Concatena as expressões atribuidas a variavel [{a + b}]')
print(f'Concatena as expressões utilizando um metodo interno da função - [{a.__add__(b)}]')
print(f'Concatena as expressões utilizando outro metodo interno da função - [{str.__add__(a, b)}]')

print(f'Retorna os metodos disponibilizados pela função string - [{dir(str)}]')

print(f'Retorna a quantidade de caracteres atribuidos a variavel a - [{len(a)}]')
print(f'Retorna a quantidade de caractees atribuis a variavel, utilziando um metodo interno da função - [{a.__len__}]')

print(f'Retorna um valor booleano(True/False), caso a letra 1 encontra-se atribuido a variavel A - [', {'1' in a}, ']')
print(f'Valida se a variavel contem a letra 1 utilizando um metodo interno - [', {a.__contains__('1')}, ']')
