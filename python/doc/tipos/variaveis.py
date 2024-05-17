# Variáveis

a = 10 # Tipo Inteiro
b = 5.2 # Tipo Float
print(a + b) # Soma as variáveis a(Inteiro) + b(Float)
a = 'Agora sou uma string!' # Tipo String
print(a) # Tipo de variaveis alterada para string
print(a + b) # Gera erro por ambiguidade

texto = 'Sua idade é... ' # Tipo String
idade = 23 # Tipo Inteiro
saudacao = 'Bom dia ' # Tipo String
PI = 3.14 # Constante
raio = float(input('Informe o raio da circuferencia ')) # Entrada de dados
area = PI * raio * raio # Multiplicação da Constante 2x + Entrada dos dados
araa = PI * pow(raio, 2) # Potencialização da Constante * Entrada de dados

print(texto + str(idade)) # Alterando a variavel Inteiro para String
print(f'{texto}' f'{idade}') # Demonstração in tela
print(3 * saudacao) # Multiplicando 3x a String
print(type(raio)) # Tipo Float
print(area) # Demonstra in tela a variavel
print(f'A área da circunferencia é {area} m2.') # Demonstração in tela a variavel com textos