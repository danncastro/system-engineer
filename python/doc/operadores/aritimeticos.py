# Operadores Aritméticos

## Tipos de atribuições
# +3 prefix
# x++ postfix
# x + y infix

x = 10 # Recebe tipo Inteiro
y = 4 # Recebe tipo Inteiro
z = 3.3 # Recebe tipo Float

soma = x + y # Soma os valores atribuidos as variaveis x e y
print(f'A soma da variavel X={x} + a variavel Y={y} é igual a {soma}')

subtracao = x - y # Subtrai os valores atribuidos as variaveis x e y
print(f'A subtração da variavel X={x} - a variavel Y={y} é igual a {subtracao}')

multiplicacao = x * y # Multiplica os valores atribuidos as variaveis x e y
print(f'A Multiplicação da variavel X={x} * a variavel Y={y} é igual a {multiplicacao}') 

exponenciação = x ** y # Potencializa os valores atribuidos as variaveis x e y
print(f'A Exponeciação da variavel X={x} com a variavel Y={y} é igual a {exponenciação}') 

divisao = x / z # Divide os valores atribuidos as variaveis x e z
print(f'A Divisão da variavel X={x} pela variavel Y={z} é igual a {divisao}')

divisao_inteiro = x // z # Divide os valores atribuidos as variaveis x e z e obtem seu resultado inteiro
print(f'A Divisão inteira da variavel X={x} pela variavel Y={z} é igual a {divisao_inteiro}') 

resto = x % y # Coleta o resto da divisão dos valores atribuidos as variaveis x e y
print(f'O resto da divisão entre as variavel X={x} pela variavel Y={z} é igual a {resto}')

par = 34 # Recebe tipo Inteiro
impar = 33 # Recebe tipo Inteiro

print(f'Se o resto da divisão for 0 o resultado será: {par % 2 == 0} ou seja PAR') # Valida se o resto da divisão é igual a Zero, caso True, retorna par
print(f'Se o resto da divisão for 1 o resultado será: {impar % 2 == 1} ou seja IMPAR') # Valida se o resto da divisção é igual a Um, caso True, retorna impar

# Desafio Operadores Aritméticos
salario = 3450.45
despesas = 2456.2
percentual_comprometido = despesas / salario * 100
print(f'Percentual comprometido é de: {percentual_comprometido} %')