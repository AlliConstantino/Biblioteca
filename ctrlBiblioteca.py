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
from telaBiblioteca import telaBiblioteca

class CtrlBiblioteca:
  def __init__(self):
    self.__ctrlLivros = ctrlLivros(self)
    self.__controladorUsuario = controladorUsuario(self)
    self.__controladorEmprestimos = controladorEmprestimos(self)
    self.__telaBiblioteca = telaBistema()
  
  def inicializa_sistema(self):
    self.abre_tela()
