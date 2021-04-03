#from editora import Editora
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

class CtrlBiblioteca():
  def __init__(self):
    #super().__init__(codigo,titulo,ano,editora,autor)
    self.__ctrlLivros = CtrlLivro()
    self.__controladorUsuario = ControladorUsuario()
    self.__controladorEmprestimo = ControladorEmprestimo()
    self.__telaBiblioteca = TelaBiblioteca()
  
  #troquei o nome pra startSystem p n ficar taaaao obvio
    def startSystem():
        self.abre_tela()

    def inclui_livro(self):
        if isinstance(livro, Livro):
            livro_incluso = False
            for i in self.__livros:
                if i.codigo == livro.codigo:
                    livro_incluso = True
            if not livro_incluso:
                self.__livros.append(livro)
            else:
                print('O livro ja estava incluso.')
        else:
            print('Livro invalido.')

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
  
  def cadastraAmigos(self): #amigo?
    # Chama o controlador de Usuarios
    self.__controladorUsuario.abre_tela()

  def cadastra_emprestimos(self):
    pass
    # Chama o controlador de Emprestimos
    self.__controladorEmprestimo.inclui_emprestimo()

  def abre_tela(self):
    self.__telaBiblioteca.tela_opcoes()
  
