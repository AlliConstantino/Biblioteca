class Autor:
    def __init__(self, codigo: int, autor: str):
        self.__codigo = codigo
        self.__autor = autor

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor
