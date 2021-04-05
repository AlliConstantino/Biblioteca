# from editora import Editora
import livro
from autor import Autor
from capitulo import Capitulo
from livro import Livro
from usuario import Usuario
from aluno import Aluno
from professor import Professor
from ctrlLivro import CtrlLivro
from controladorUsuario import ControladorUsuario
from controladorEmprestimo import ControladorEmprestimo
from telaBiblioteca import TelaBiblioteca
from telaLivro import TelaLivro


class CtrlBiblioteca():
    def __init__(self):
        self.__ctrlLivro = CtrlLivro()
        self.__controladorUsuario = ControladorUsuario()
        self.__controladorEmprestimo = ControladorEmprestimo()
        self.__telaBiblioteca = TelaBiblioteca()
        self.__telaLivro = TelaLivro()

    def startSystem(self):
        self.abre_tela()

    def inclui_livro(self):
        titulo = input("Titulo: ")
        capitulo = input("Capitulo: ")
        autor = input("Autor: ")
        

        return {"Titulo": titulo, 'capitulo': capitulo,
                'autor': autor}

    def exclui_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            livro_incluso = False
            for i in self.__livros:
                if i.codigo == livro.codigo:
                    self.__livros.remove(i)
                    livro_incluso = True
            if not livro_incluso:
                print('O livro nao estava incluso.')
        else:
            print('Livro invalido.')

    @property
    def controladorUsuario(self):
        return self.__controladorUsuario

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





