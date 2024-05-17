#!python3

calculo = 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2

print('Realizando o cálculo com as prioridades da variavel calculo, efetuando apenas uma operação por linha, temos a seguinte ordem de cálculo')
print()

print(f'1º Resolve a exponenciação --> 10 % 3 * (10 ** 2) + 1 - 10 * 4 / 2')
print(f'2º Resolve o resto da divisão --> (10 % 3) * 100 + 1 - 10 * 4 / 2')
print(f'3º Resolve a primeira multiplicação --> (1 * 100) + 1 - 10 * 4 / 2')
print(f'4º Resolve a segunda multiplicação --> 100 + 1 - (10 * 4) / 2')
print(f'5º Resolve a divisão --> 100 + 1 - (40 / 2)')
print(f'6º Resolve a soma --> (100 + 1) - 20')
print(f'7º Resolve a subtração --> (101 - 20)')
print(f'8º Retorna o resultado --> 81 [{calculo}]')
