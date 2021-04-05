

from ctrlLivro import CtrlLivro
from controladorUsuario import ControladorUsuario
from controladorEmprestimo import ControladorEmprestimo
from telaBiblioteca import TelaBiblioteca
from telaLivro import TelaLivro


class CtrlBiblioteca():
    def __init__(self):
        self.__ctrlLivro = CtrlLivro(self)
        self.__controladorUsuario = ControladorUsuario(self)
        self.__controladorEmprestimo = ControladorEmprestimo(self)
        self.__telaBiblioteca = TelaBiblioteca()
        self.__telaLivro = TelaLivro()


    def startSystem(self):
        self.abre_tela()

    @property
    def controladorUsuario(self):
        return self.__controladorUsuario

    @property
    def ctrlLivro(self):
        return self.__ctrlLivro

    def abre_tela(self):
        opcao = self.__telaBiblioteca.tela_opcoes()
        if opcao == 1:
            self.__ctrlLivro.abre_tela()
        elif opcao == 2:
            self.__controladorUsuario.abre_tela()
        elif opcao == 3:
            self.__controladorEmprestimo.abre_tela()
        elif opcao != 0:
            self.abre_tela()





