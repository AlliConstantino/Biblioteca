from editora import Editora
from autor import Autor
from capitulo import Capitulo

#colocar os setter's em CtrlLivro

class Livro:
    def __init__(
            self,
            codigo: int,
            titulo: str,
            ano: int,
            editora: Editora,
            autor: Autor,
            numeroCapitulo: int,
            tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def autores(self):
        return self.__autores

    #incluir no CtrlAutor ou no CtrlLivro (se bem que eu acho que é melhor no autor, mas não sei se essa classe vai continuar existindo)
    def incluirAutor(self, autor: Autor):
        if isinstance(autor, Autor):
            autor_incluso = False
            for i in self.__autores:
                if i.codigo == autor.codigo:
                    autor_incluso = True
            if not autor_incluso:
                self.__autores.append(autor)
            else:
                print('O autor ja estava incluso.')
        else:
            print('Autor invalido.')

    def excluirAutor(self, autor: Autor):
        if isinstance(autor, Autor):
            autor_incluso = False
            for i in self.__autores:
                if i.codigo == autor.codigo:
                    self.__autores.remove(i)
                    autor_incluso = True
            if not autor_incluso:
                print('O autor nao estava incluso.')
        else:
            print('Autor invalido.')

    
    
