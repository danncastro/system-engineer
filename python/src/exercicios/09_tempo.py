#!python3

'''
Tempo em segundos: Faça um programa que leia e converte dias, horas, minutos e segundos para a grandeza de segundos.

Segundos = 60 Milisegundos
1 Minuto = 60 Segundos
1 Hora = 60 Minutos
1 Dia = 24 Horas
'''

segundos = int(input("Digite o valor de segundos: "))
minutos = int(input('Digite o valor de minutos: '))
horas = int(input('Digite o valor de horas: '))
dias = int(input("Digite o valor de dias: "))

segundosTotal = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

print(f'O valor total de segundos é: {segundosTotal}s')
