# Informar ao aluno que o programa está em execução
print('OLÁ, NESTA TELA VOCÊ PODE CONSULTAR SUA MÉDIA')

# Solicitar ao aluno seu nome
nome = input('Nome: ')

# Solcitar ao aluno o nome da matéria
materia = input('Matéria: ')

# Solicitar as 4 notas
nota1= float(input('Digite a nota do Primeiro semestre: '))
nota2= float(input('Digite a nota do Segundo semestre: '))
nota3= float(input('Digite a nota do Terceiro semestre: '))
nota4= float(input('Digite a nota do Quarto semestre: '))

# Efetuar o calculo da média
# OBS.: A média para aprovação é 7
media = (nota1 + nota2 + nota3 + nota4)/4

# informar ao aluno a frase abaixo: "Se a média for menor que 7, imprimir a frase:"
if media < 7:
    print('Aluno %s, você foi REPROVADO. Sua média em %s foi %.2f.'
        % (nome, materia, media))
#Se a média foi igual ou maior que 7, imprimir a frase:
else:
    print('PARABENS!! Aluno %s, você foi APROVADO. Sua média em %s foi %.2f.'
        % (nome, materia, media))