# Operadores Ternários

lockdown = True # Booleano
grana = 30 # Inteiro

status = 'Em casa' if lockdown else 'Uhuuuul' # Valida se expressão(variavel lockdown) é verdadeira
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu' # Valida se a expressão(variavel lockdown) é verdadeira e se o valor informado na variavel grana é maior ou igual a 100
print(f'O status é: {status}') # Informa o resultado das expressões acima

esta_chovendo = False # Booleano
roupas = 'Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo] # Validador ternario de 3 operandos (secas, molhadas, variavel)
print(roupas) # Neste caso a validação true está mais proxima da expressão(esta_chovendo)

esta_chovendo = True
roupas = 'Hoje estou com as roupas ' + ('molhadas' if esta_chovendo else 'secas.') # Valida se a expresão é verdadeira, caso negativo será o outro operando
print(roupas)