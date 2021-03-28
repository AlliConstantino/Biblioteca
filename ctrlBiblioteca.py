from editora import Editora
from autor import Autor
from capitulo import Capitulo
from livro import Livro
from usuario import Usuario
from aluno import Aluno
from professor import Professor
from ctrlLivros import CtrlLivros

class CtrlBiblioteca:
  def __init__(self):
    self.__ctrlLivros = ctrlLivros(self)
    #self.__controladorUsuario = controladorUsuario(self)
    #self.__controlador_emprestimos = ControladorEmprestimos(self)
    #self.__tela_sistema = TelaSistema()
  
  def inicializa_sistema(self):
    self.abre_tela()
