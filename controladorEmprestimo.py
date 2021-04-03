import emprestimo
#from ctrlBiblioteca import CtrlBiblioteca
from ctrlLivro import CtrlLivro
from controladorUsuario import ControladorUsuario
from telaEmprestimo import TelaEmprestimo
from emprestimo import Emprestimo
from livro import Livro
from usuario import Usuario
from dataEmprestimo import DataEmprestimo
import datetime


class ControladorEmprestimo():

    def __init__(self):

        self.__emprestimos = []

        self.__tela_emprestimo = TelaEmprestimo()
        self.__controlador_livro = CtrlLivro()
        self.__controlador_usuario = ControladorUsuario()
        self.__data_emprestimo = DataEmprestimo()
        #self.__ctrlBiblioteca = CtrlBiblioteca()

    def inclui_emprestimo(self):
        dados_emprestimo = self.__tela_emprestimo.pega_dados_emprestimo()
        livro = self.__controlador_livro.retornaLivro(dados_emprestimo["tituloLivro"])
        usuario = self.__controlador_usuario.retornaUsuario(dados_emprestimo["nomeUsuario"])
        if livro:
            if usuario:
                emprestimo = Emprestimo(livro, usuario, DataEmprestimo(datetime.datetime.now()))
                self.__emprestimos.append(emprestimo)
            else:
                print('Usuário inexistente, emprestimo não efetuado')
        elif usuario:
            print('Livro inexistente, emprestimo não efetuado')
        else:
            print('Livro e usuário inexistentes, emprestimo não efetuado')

# Pensar em atribuir datetime.timedelta(days=7) como atributo "tempoLimite" na classe DataEmprestimo
# verifica_Status ainda precisa de alguns ajustes
    def verifica_status(self, emprestimo):
        tempoEmEmprestimo = (datetime.datetime.now() - emprestimo.dataEmprestimo.dataInicial)
        if (datetime.datetime.now() > emprestimo.dataEmprestimo.dataFinal):
            return 'Seu emprestimo está atrasado há ' + tempoEmEmprestimo - datetime.timedelta(days=7) + ' dias'
        else:
            return 'Seu emprestimo foi feito há ' + tempoEmEmprestimo + 'dias'

    def lista_emprestimos(self):
        for emprestimo in self.__emprestimos:
            self.__tela_emprestimo.mostra_emprestimo({"tituloLivro": emprestimo.livro.titulo, "nomeUsuario": emprestimo.usuario.nome,
            "dataInicial": emprestimo.dataEmprestimo.dataIncial, "dataFinal": emprestimo.dataEmprestimo.dataFinal,
            "status": self.verifica_status(emprestimo)})

    def renova_emprestimo(self):
        dados_emprestimo = self.__tela_emprestimo.pega_dados_emprestimo()
        emprestimo_existe = self.retornaEmprestimo(dados_emprestimo['tituloLivro'])
        if emprestimo_existe:
            index = self.__emprestimo.index(emprestimo_existe)
            self.__emprestimo[index].dataEmprestimo = self.__emprestimo[index].dataEmprestimo + datetime.timedelta(days=7)
            print('Empréstimo renovado para mais 7 dias!')
        else:
            print("Esse empréstimo ainda não foi criado.")

    def retornaEmprestimo(self, tituloLivro):
        for emprestimo in self.__emprestimos:
                if emprestimo.livro.titulo == tituloLivro:
                    return emprestimo
        return False

    def exclui_emprestimo(self):
        if isinstance(emprestimo, Emprestimo):
            emprestimo_incluso = False
            for i in self.__emprestimos:
                if i.livro == emprestimo.livro.titulo:
                    self.__emprestimos.remove(i)
                    emprestimo_incluso = True
            if not emprestimo_incluso:
                print('O empréstimo não estava incluso')
        else:
            print('Empréstimo inválido.')


    def abre_tela(self):
        #Atenção: código incompleto: adicionar funcões para todas as opções da tela
        lista_opcoes = {1: self.inclui_emprestimo, 2: self.renova_emprestimo ,3: self.lista_emprestimos, 4: self.exclui_emprestimo,
                        5: self.verifica_emprestimo}

        continua = True
        while continua:
            lista_opcoes[self.__telaEmprestimo.tela_opcoes()]()

            """
              a classe DataEmprestimo deve receber uma data no init, 
              sendo essa a data atual (datetime.datetime.now())
              e irá definitir:
              self.__dataInicial = dataAtual
              self.__dataFinal = dataAtual + datetime.timedelta(days=7)
            """


