# Tipo Strings: Funcionalidades disponiveis

print(f'Retorna as funcionalidades disponiveis nas funções da String - [{dir(str)}]')

nome = 'Danniel Castro'
print(f'Retorna o conteúdo atribuido a variavel - [{nome}]')
print(f'Retorna o elemento de indice 0 atribuido a variavel - [{nome[0]}]')

# nome[0] = 'P' # Gerará um erro pois não é possivel alterar um valor de indice especifico atribuido a uma variavel
# print('Marca d 'água') # Gerará um erro de sintax pois está escapando o valor da string

print('Resolveria o problema de sintaxe citado acima', "[Danniel D' Castro]")
print('Outro metodo de resolução do problema de sintaxe', '[Danniel D\' Castro]')

texto = 'Texto entre apostrófos pode ter "aspas"'
print(f'Apenas demonstrando que também é possivel adicionar aspas aos apostrófos - [{texto}]')

doc = """Texto com múltiplas
    ... linhas"""
print(doc)

doc2 = '''Também é possível
    ... com 3 aspas simples'''
print(doc2)

doc2 = '''Também é possível...\t utilizar tab'''
print(doc2)
