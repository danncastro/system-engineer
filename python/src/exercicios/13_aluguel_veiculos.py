#!/bin/python3

'''
ALUGUEL DE VEÍCULOS: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário.
1 - Assim como a quantidade de dias pelos quais o carro foi alugado. 
2 - Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado
'''

quilometragem = float(input('Quilometragem percorrida: '))
diasAlugado = int(input('Quantos dias foi alugado: '))

precoDia = 60
precoQuilometragem = 0.15

custoDia = diasAlugado * 60
custoQuilometragem = quilometragem * precoQuilometragem

custoTotal = custoDia + custoQuilometragem

print(f'O valor total pelo aluguel de {diasAlugado} dias e {quilometragem:0.0f}km rodados é de: R${custoTotal:.2f}')
