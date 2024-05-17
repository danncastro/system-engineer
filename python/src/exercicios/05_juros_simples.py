#!python3

'''
Uma pessoa empresta R$3000,00 a uma taxa de juros simples de 3% ao mês num período de 05 meses.
1 - Quanto receberá ao final desse período?

Juros = Capital * (Taxa * Tempo)
Montante = Capital + Juros
'''

capital = 3000
taxa = 3 / 100
tempo = 5

juros = capital * (taxa * tempo)
montante = capital + juros

print(f'A pessoa receberá ao final do emprestimo R${montante:.2f}')
