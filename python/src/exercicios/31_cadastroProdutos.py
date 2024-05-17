#!Python3

while True:
    nomeProduto = input('Insira a descrição do produto: ')
    quantidade = int(input('Digite a quantidade: '))
    continuar = input('Deseja inserir mais um produto no cadastro? SIM[s] ou NÂO[n]: ')
    if continuar == 'n':
        break
print(f'Produto: {nomeProduto}')
print(f'Quantidade: {quantidade}')