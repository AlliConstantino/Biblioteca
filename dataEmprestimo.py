import datetime

class DataEmprestimo():
    def data_emprestimo(self):
        dataAtual = (datetime.datetime.now())

        self.__dataInicial = dataAtual
        self.__dataFinal = dataAtual + datetime.timedelta(days=7)