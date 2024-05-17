# Operadores de Atribuição

resultado = 2 # Variavel resultado recebe valor inteiro/float
print(f'Valor inicial retorna [{resultado}]')

resultado = resultado + 7 # Variavel resultado recebe o valor da variavel resultado + 7
print(f'Somando o valor inicial + 7 retorna [{resultado}]')

resultado = 'Texto' # Reatribui o tipo da variavel para String
print(f'O valor da variavel resultado foi reatribuido para o tipo String retornando um [{resultado}]')

resultado = 2.5 # Variavel resultado recebe um tipo float
print(f'O valor da variavel foi novamente reatribuido agora a um tipo float retornando [{resultado}]')

resultado += resultado # Acrecentando o valor da variavel resultado + o valor anteriormente atribuido a variavel resultado
print(f'O valor da variavel resultado foi somado com o valor anteriormente atribuido a variavel resultado retornando [{resultado}]')

resultado +=3  # Soma o valor da variavel resultado + 3 ou resumidamente (resultado = resultado + 3)
print(f'Somando o valor da variavel resultado + 3 retorna [{resultado}]')

resultado -=1  # Subtrai o valor 1 da variavel resultado, ou resumidamente (resultado = resultado - 1)
print(f'Subtrair 1 da variavel resultado retorna [{resultado}]')

resultado *=4  # Multiplica o valor 4 pela variavel resultado, ou resumidamente (resultado = resultado * 4)
print(f'Multiplica o valor 4 pela variavel resultado retornando {resultado}')

# resultado **=8 # resultado = resultado ** 8

# resultado /=2   # resultado = resultado / 2
# print(resultado)

# resultado //=2   # resultado = resultado // 2
# print(resultado)

# resultado %=6   # resultado = resultado % 6
# print(resultado)