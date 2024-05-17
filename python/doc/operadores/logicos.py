# Operadores Lógicos

b1 = True # Tipo Booleano
b2 = False # Tipo Booleano
b3 = True # Tipo Booleano

print(b1 and b2 and b3) # Valida se a variavel b1 e as variaveis b2 e b3 são verdadeiro
print(b1 or b2 or b3) # Valida se a variavel b1 ou as variaveis b2 e b3 são verdadeiro
print(b1 != b2) # equivalente ao xor ^
print(not b1) # Diz que a variavel b1 que é verdadeira agora passa a ser falsa
print(not b2) # Diz que a variavel b2 que é falsa agora passa a ser verdadeira

print(b1 and not b2 and b3) # Valida se a variavel b1 e as variaveis b2 que antes era falsa, agora passa a ser verdadeiro e a variavel b3 são verdadeiras

x = 3 # Tipo Inteiro
y = 4 # Tipo Inteiro

print(b1 and not b2 and x < y) # Valida se a variavel b1 e as variaveis b2 que antes era falsa, agora passa a ser verdadeiro a variavel b3, x e y são verdadeiras

## Tabela verdade do AND        |   Tabela verdade do OR       |   Tabela verdade do XOR     |   Operador de Negação (Unário)
#  True and True = True         |   True and True = True       |   True != True = False      |   not True = False
#  True and False = False       |   True and False = True      |   True != False = True      |   not False = True
#  False and True = False       |   False and True = True      |   False != True = True      |   not 0 = True
#  False and False = False      |   False and False = False    |   False != False = False    |   not 1 = False


## Cuidado! Operadores bit-a-bit    |   AND bit-a-bit     |   OR bit-a-bit  |   XOR bit-a-bit
#  True & True = True               |   3 = 11            |   3 = 11        |   3 = 11
#  True | False = True              |   2 = 10            |   2 = 10        |   2 = 10
#  True ^ False = True              |   _ = 10            |   _ = 11        |   _ = 01
#  False & False = False            |   3 & 2 = 2         |   3 | 2 = 3     |   3 ^ 2 = 1

## Exemplo real
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
print(f'Valor: {meta}')

# Desafio Operadores Lógicos
trabalho_terca = False
trabalho_quinta = False

"""
- Confirmado os 2 trabalhos: TV 50 + Sorvete
- Confirmado apenas 1 trabalho: TV 32 + Sorvete
- Nenhum trabalho confirmado: Fica em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca or trabalho_quinta
sorvete = trabalho_terca != trabalho_quinta
ficar_em_casa = not sorvete
print('Tv50={} Tv32={} Sorvete={} Casa={}'
    .format(tv_50, tv_32, sorvete, ficar_em_casa))

## Sobre o .format()
test_format = '{1}, {2}, {0}'.format(1, False, 'Resultado')
print(test_format)

test_format2 = '{0}, {1}, {2}'.format(1, False, 'Resultado')
print(test_format2)