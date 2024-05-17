# Tipo String

frase = 'Python é uma linguagem excelente'

print(f'Retorna um valor booleano(True/False) caso a palavra py em minusculo esteja presente na variavel - [', {'py' in frase}, ']') 
print(f'Retorna um valor booleano(True/False) caso a palavra ing em minusculo esteja presente na variavel - [', {'ing' in frase}, ']')
print(f'Retorna um valor booleano(True/False) caso a palavra py em minusculo não esteja presente na variavel  - [', {'py' not in frase}, ']')

print(f'Retorna a quantidade de caracteres atribuidos na variavel - [{len(frase)}]')

print(f'Retorna todos os caracteres em letras minusculas - [{frase.lower()}]')
print(f'Retorna um valor booleano(True/False) caso a palavra py em maiusculo esteja presente na variavel [', {'py' in frase.lower()}, ']')

print(f'Retorna todos os caracteres em letras maiusculas - [{frase.upper()}]') # 
print(f'Retorna o valor original da variavel - [{frase}]') # 

frase = frase.upper() # Altera definitivo o valor atribuido a variavel inicialmente
print(f' Retorna o novo valor atribuido a variavel - [{frase}]')

print(f'Retorna a frase separada pelo espaços em branco - {frase.split()}')
print(f'Retorna a frase separada sem o caracter A', frase.split('A')) 
