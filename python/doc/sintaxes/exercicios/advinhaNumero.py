import random


chute = 0
chances = 7
tentativas = 1
jogador = ''

# Sistema sorteará um número entre 1 e 100
numero_secreto = random.randint(1, 5)

# Boas Vindas
print('#################################################')
print('Bem vindo ao jogo de advinha')
print('Você terá sete chances para adivinhar o número')
print('#################################################')

# programa solicita o nome do jogador
jogador = input('Digite seu nome: ')
print('Chute um número entre 1 e 100')


while tentativas <= 7:
    # Sistema solicita ao jogador seu palpite
    chute = int(input('Digite o número: '))
    if chute < numero_secreto:
        # Se errou, informar se para mais ou para menos, solicitar outro palpite
        print('Você errou. Seu número é menor que o sorteado,'
            ' tente novamente.)')
        # informar quantas tentativas ainda restam
        print('Tentativa %d de %d' % (tentativas, chances))
    # Se acertou, parabenizar e informar o número de tentativas utilizadas.
    elif chute == numero_secreto:
        print('PARABÉNS!!!!!', jogador)
        print('Você acertou com %d tentativcas' % tentativas)
        # Número máximo de tentativas = 7
        tentativas = 7
    else:
        print('Você errou, Seu número é maior que o sorteado,'
            ' tente novamente')
        print('Tentativa %d de %d' % (tentativas, chances))

    if tentativas == 6:
        print('Última tentativa')
    elif tentativas == 7:
        print('### Fim de jogo ###')

    tentativas = tentativas + 1

