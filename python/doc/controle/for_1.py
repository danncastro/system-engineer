#!python3

for i in range(10):
    print(i)
    
for i in range(1, 11):
    print(i)
    
for i in range(1, 100, 7):
    print(i)
    
for i in range(20, 0, -3):
    print(i)
    
nums = [2, 4, 6, 8]

for n in nums:
    print(n)
    
for n in nums:
    print(n, end=',')
    
texto = 'Python é muito massa!'

for letra in texto:
    print(letra)
    
for letra in texto:
    print(letra, end=' ')
    
for s in {1, 2, 3, 4, 4, 4}:
    print(s)
    
produto = {
    'nome': 'Caneta',
    'preço': 8.80,
    'desc': 0.5
}

for atrib in produto:
    print(atrib, '==>', produto[atrib])
    
for atrib, valor in produto.items():
    print(atrib, '==>', valor)
    
for valor in produto.values():
    print(valor, end=' ')
    
for atrib in produto.keys():
    print(atrib, end=' ')