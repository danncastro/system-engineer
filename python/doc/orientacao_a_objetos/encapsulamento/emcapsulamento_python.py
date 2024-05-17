class Livro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.autor = autor

    @property #GET
    def titulo(self):
        return self.__titulo

    @titulo.setter #SET
    def titulo(self, titulo):
        self.__titulo = titulo



livro1 = Livro('Curso de Python', 'Alcimar Costa')
print(livro1.autor)
print(livro1.titulo)
livro1.titulo = 'Novo titulo'
print(livro1.titulo)








