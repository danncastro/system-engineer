#!python3

'''
DESCONTO DE MERCADORIA: Solicite o preço de uma mercadoria e o percentual de desconto. 
1 - Exiba o valor do desconto e o preço a pagar
'''

mercadoria = float(input('Digite o valor do produto: '))
porcentagem = float(input('Digite o percentual de desconto: '))

percentualDesconto = porcentagem / 100
desconto = mercadoria * percentualDesconto
preco = mercadoria - desconto

print(f'A mercadorio tem R${desconto:.2f} de desconto, o preço fica: R${preco:.2f}')
