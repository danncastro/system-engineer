def saudacao():
    print('Bom dia !')

def saudacao(nome):
    print(f'Bom dia {nome}!')

def saudacao(nome = 'Pessoa'):
    print(f'Bom dia {nome} !')

def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia {nome} ! Você nem parece ter {idade} anos!')

def saudacao():
    print('Boa tarde!')

print(__name__)

if __name__ == '__main__':
    saudacao(nome = 'Danniel', idade = 30)

def soma_e_multiplicacao(a, b, x):
    return a + b * x