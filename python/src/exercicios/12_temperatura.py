#!python3

'''
TEMPERATURA CELSIUS PARA FAHRENHEIT: Faça um programa que leia e converta a temperatura celsius para fahrenheit.

Fahrenheit = Celsius * 1.8 + 32
Fahrenheit = (Celsius * 9 / 5) + 32
'''

celsius = float(input('Digite a temperatura em celsius Cº: '))

fahrenheit = (celsius * 1.8) + 32

print(f'A temperatura em Fahrenheit é: {fahrenheit}Fº')
