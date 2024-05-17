# Tipo conjunto: Apenas valores

a = {1, 2, 3}
print(f'Retorna o tipo de dado atribuido a variavel - [{type(a)}]')

print(f'Retorna uma lista de dados - [{{1, 2, 3}}]')
print(f'Retorna dados do tipo conjunto - [{type({1, 2, 3})}]')

a = set('cod3r')
print(f'Retorna as letras separadas, sem garantia de ordenação - [{a}]')

conj = {1, 2, 3, 3, 3, 3}  # Atribui valores repetidos a uma variavel de dados do tipo conjunto
print(f'Retorna os elementos não repetidos atribuidos a variavel - [{conj}]')

print(f'Retorna a quantidade de caracteres não repedidos, atribuidos a variavel - [{len(conj)}]')

# print(conj[0]) Retornará um erro pois os elementos de dados do tipo conjunto não são acessiveis através de indices.

print(f'Retorna um tipo booleano(True/False) caso os valores consultandos sejam iguais, idependente da ordem -', [{1, 2, 3} == {3, 2, 1, 3}])

# Exemplo
c1 = {1, 2}
c2 = {2, 3}
print(f'Retornará a união dos 2 conjuntos - [{c1.union(c2)}]')
print(f'Retornará os conjuntos que sejam similares - [{c1.intersection(c2)}]')

c1.update(c2)
print(f'Retorna uma atualização dos conjuntos, similar a união porém o update altera de fato o conjunto - [{c1}]')

print(f'Retorá verdadeiro pois os conjuntos foram atualizados com update - [{c2 <= c1}]')

c1 = {1, 2}
c2 = {2, 3}
print(f'Retornará a união dos 2 conjuntos, mas sem alterar de fato a variavel - [{c1.union(c2)}]')
print(f'Retorá false pois os conjuntos estão da forma que foram atribuidos inicialmente, sem o update - [{c2 <= c1}]')

print(f'Retorá o resultado se conjunto c2 é superconjunto do c1 - [{c1 >= c2}]')

print(f'Retorá a diferença entre os conjuntos - [{c1 - c2}]')
