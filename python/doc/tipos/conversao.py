# Conversão de Tipos: Alterando o tipo da variavel

a = 2 
b = '3'

print(f'Retorna o tipo de dado da variavel A={a} - [{type(a)}]')
print(f'Retorna o tipo de dado da variavel B={b} - [{type(b)}]')

print(f'Converte a variavel B para um tipo inteiro - [{a + int(b)}] [{type(b)}]') 
print(f'Converte a variavel A para uma string - [{str(a) + b}] [{type(a)}]') 

print(f'Retorna que a variavel A é uma String, mesmo que inicialmente ela tenha sido atribuida como um tipo inteiro - [{type(str(a))}]')

# print(2 + int('2 Bom número')) # Ocorrerá um erro, pois mesmo que estejamos convertendo a expressão em um inteiro, não é possivel converter texto em base 10 
