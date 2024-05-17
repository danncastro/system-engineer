x = 0

while x != -1:
    x = float(input('Informe o número ou -1 para sair: '))
print('Fim')

total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota
print(f'A média da turma é {total / qtde}')

x = 10

while x:
    print(x)
    x -= 1
print('Fim')