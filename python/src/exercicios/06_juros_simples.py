#!python3

'''
Lúcia emprestou R$1000,00 reais para sua amiga Márcia mediante uma taxa de 10% ao mês, que se comprometeu em pagar a dívida num período de 1 ano.
1 - Calcule o valor que Márcia no final pagará para a Lúcia

Juros = Capital * Taxa * Tempo
Montante = Capital + Juros
'''
juros = 1000 * ((10 / 100) * 12)

print(f'Márcia deverá pagar a Lúcia um total de R${1000 + juros:.2f} com uma taxa de juros de {10 / 100:.2f}% ao mês')
