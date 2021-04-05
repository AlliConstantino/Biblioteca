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
        self.__livros = []  # array que vai guardar a lista de livros

    def startSystem(self):
        self.abre_tela()

    def inclui_livro(self):
        nome_livro = self.__telaBiblioteca.pega_titulo('Titulo')
        livro_existe = self.retornaLivro(nome_livro['Titulo'])

        if livro_existe:
            print('Esse livro já existe.')
        else:
            dados_livro = self.__telaBiblioteca.pega_dados_livro()
            livro = Livro(nome_livro["Titulo"], dados_livro["Autor"], dados_livro["Editora"])
            self.__livros.append(livro)
            print("Livro adicionado com sucesso!")

    def retornaLivro(self, titulo):
        for livro in self.__livros:
            if livro.titulo == titulo:
                return livro
        return False

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





