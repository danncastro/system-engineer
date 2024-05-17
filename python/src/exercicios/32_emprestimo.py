nomeCandidato = input('Por favor digite seu nome: ')
idadeCandidato = int(input('Digite sua idade: '))
rendaCandidato = float(input('Por favor, insira sua renda mensal brunta: R$'))

if rendaCandidato >= 2000 or idadeCandidato >= 65:
    print('SEU CRÉDITO FOI APROVADO')
else:
    print('Infelizmente não aprovamos seu crédito, tente novamente')