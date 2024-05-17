# Tipos Númericos: Disponibilidades da função

print(f'Retorna as funcionalidas disponiveis nos tipos de dados Inteiros - [{dir(int)}]')
print(f'Retorna as funcionalidas disponiveis nos tipos de dados Float - [{dir(float)}]')

a = 5 
b = 2.5

print(f'Retorna um tipo de dado Float, por que todas operações efetuadas com um Float, retornam Float - [{type(a / b)}]') # 
print(f'Retorna um tipo de dado Float - [{type(a + b)}]') 
print(f'Retorna um tipo de dado Float - [{type(a * b)}]')

print(f'Retorna qual o tipo de dado atribuido a variavel A [{type(a)}]')
print(f'Retorna qual o tipo de dado atribuido a variavel B [{type(b)}]')

print(f'[Retorna um valor booleano(True/False) para caso a variavel B seja um tipo de dado Inteiro  - [{b.is_integer()}]')
print(f'[Retorna um valor booleano(True/False) para caso a expressão seja um tipo de dado Inteiro, embora o 5.0 seja um tipo Float, 0 não é descartado na resolução  - [{5.0.is_integer()}]')

print(f'Retorna a soma dos valores 2 + 3, a função __add__ está disponivel dentro do metodo Inteiro. - [{int.__add__(2, 3)}]')

print(f'Retorna um valor sempre absoluto, seja ele Inteiro negativo - [{(-2).__abs__()}]')
print(f'Metodo abreviado do metodo __abs__ utilzado pela função abs - [{abs(-2)}]')

print(f'Retorna um valor sempre absoluto, seja ele Float negativo - [{(-3.6).__abs__()}]')
print(f'Metodo abreviado do metodo __abs__ utilzado pela função abs - [{abs(3.6)}]') # 

# Decimal

from decimal import Decimal, getcontext # Importa do modulo decimal, unicamente as função Decimal e getcontext.

print(f'Retorna de forma decimal a divisão de 1 por 7 - [{Decimal(1) / Decimal(7)}]')

getcontext().prec = 3 # Informa quantas casas decimais serão apresentadas em tela
print(f'Retorna a soma dos valores 1.1 + 2.2 com a quantidade de casas decimais definidas em getcontext - [{Decimal(1.1) + Decimal(2.2)}]')

import decimal # Importa todo o modulo decimal
print(f'Retorna as funções disponibilizadas no modulo decimal - [{dir(decimal)}]')
