from editora import Editora
from autor import Autor
from capitulo import Capitulo
from livro import Livro
from usuario import Usuario
from aluno import Aluno
from professor import Professor
from ctrlLivros import CtrlLivros
from controladorUsuario import ControladorUsuario
from controladorEmprestimo import ControladorEmprestimo
from telaBiblioteca import TelaBiblioteca

class CtrlBiblioteca:
  def __init__(self):
    self.__ctrlLivros = ctrlLivros(self)
    self.__controladorUsuario = controladorUsuario(self)
    self.__controladorEmprestimo = controladorEmprestimo(self)
    self.__telaBiblioteca = telaBistema()
  
  #troquei o nome pra startSystem p n ficar taaaao obvio
  def startSystem(self):
    self.abre_tela()
  
  def cadastraLivros(self):
    pass
    # Chama o controlador de Livros

  def cadastraAmigos(self):
    # Chama o controlador de Usuarios
    self.__controladorUsuario.abre_tela()

  def cadastra_emprestimos(self):
    pass
    # Chama o controlador de Emprestimos
  
