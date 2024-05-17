#!python3

'''
Conversor de Medidas: Faça um programa que leia e converte metros em milímetros e metros em quilômetros

Milimetros = Metros * 1000
Quilometros = Metros / 1000
''' 

metros = float(input('Digite o valor em metros: '))

milimetros = metros * 1000
quilometros = metros / 1000

print(f'A conversão de {metros:.0f}m para milimitros equivalem a: {milimetros:.0f}mm')
print(f'E a conversão de {metros:.0f}m para quilometro equivalem a: {quilometros:.3f}km')
