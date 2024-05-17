#python3

'''
AUMENTO SALARIAL: Faça um programa que calcule o aumento de um salário. 
1 -  Ele deve solicitar o valor do salário e a porcentagem do aumento. 
2 -  Exiba o valor do aumento e do novo salário
'''

salario = float(input('Digite o valor de salario: '))
porcentagem = float(input('Digite a porcentagem de aumento: '))

percentualAumento = porcentagem / 100
valorAumento = salario * percentualAumento
aumentoFinal = salario + valorAumento

print(f'Houve um aumento de {porcentagem:.0f}% no salario, aumentando R${valorAumento:.2f}, o salario atual é de: R${aumentoFinal:.2f}')
