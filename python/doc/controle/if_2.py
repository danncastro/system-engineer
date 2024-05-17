a = 'valor' # True

print(not 'valor')

a = 0 # False
a = -1 # True
a = -0.00001 # True
a = '' # False
a = ' ' # True
a = [] # False
a = {} # False

if a:
    print('Existe!!!')
else:
    print('Não existe ou zero ou vazio...')