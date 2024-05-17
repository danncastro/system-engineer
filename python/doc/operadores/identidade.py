# Operador de Identidade

x = 3 # Tipo inteiro
y = x # Tipo String
z = 3 # Tipo inteiro

validacao1 = x is y # Valida se o x tem o mesmo valor de y
print(f'Valor de X é {validacao1} para Valor de Y') # Retorna True

validacao2 = y is z # Valida se o y tem o mesmo valor de z
print(f'Valor de Y é {validacao2} para Valor de Z') # Retorna True

validacao3 = x is not z # Valida se o valor de x não é igual ao valor de z
print(f'Valor de X é {validacao3} para Valor de Z') # Retorna False

lista_a = [1, 2, 3] # Tipo Lista
lista_b = lista_a # Tipo String
lista_c = [1, 2, 3] # Tipo lista

validador1 = lista_a is lista_b # Valida se a lista a é igual a lista b
print(f'Lista A é {validador1} para Lista C') # Retorna True

validador2 = lista_b is lista_c # Valida se a lista b é igual a Lista C
print(f'Lista B é {validador2} para Lista C') # Retorna False, por que embora os valores das listas sejam iguais, elas apontam para lugar diferentes em memoria

validador3 = lista_a is not lista_c # Valida se a lista a não é igual a lista c
print(f'Lista A é {validador3} para Lista C') # Retorna True