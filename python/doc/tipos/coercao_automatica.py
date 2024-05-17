# Coerção Automática

print(f'Retorna dados do tipo Float - [{type(10 / 2)}]')
print(f'Retorna dados do tipo Inteiro, pois duas barras representam uma divisão inteiro - [{type(10 // 3)}]')
print(f'Retorna dados do tipo Float, mesmo utilizando duas barras, um dos elementos da divisão é um número flutuante. - [{type(10 // 3.3)}]')
print(f'Retorna dados do tipo Float - [{type(10 / 2.5)}]')
print(f'Retorna dados do tipo Inteiro - [{type(2 + True)}]')
print(f'Retorna dados do tipo Float - [{type(2.5 + False)}]')
