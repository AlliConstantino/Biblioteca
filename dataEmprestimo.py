
from datetime import datetime

from datetime import timedelta as td


class DataEmprestimo():
    def __init__(self):
        dataAtual = datetime.now()

        self.__dataInicial = dataAtual
        self.__dataFinal = dataAtual + td(days=7)

    @property
    def dataInicial(self):
        return self.__dataInicial

    @dataInicial.setter
    def dataInicial(self, dataInicial):
        self.__dataInicial = dataInicial

    @property
    def dataFinal(self):
        return self.__dataFinal

    @dataFinal.setter
    def dataFinal(self, dataFinal):
        self.__dataFinal = dataFinal
