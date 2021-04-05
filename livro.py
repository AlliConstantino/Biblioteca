from editora import Editora
from autor import Autor
from capitulo import Capitulo

#colocar os setter's em CtrlLivro

class Livro:
    def __init__(
            self,
            titulo: str,
            editora: Editora,
            autor: Autor): #apaguei os outros (codigo, capitulos, status) pois não foram implementados
        #self.__codigo = codigo
        self.__titulo = titulo
        #self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        #self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]
        #self.__status = status

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
    
    @property
    def status(self):
        return self.status
    
    @status.setter
    def status(self,status):
        self.__status = status

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

     
    
