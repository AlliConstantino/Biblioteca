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
    super().__init__(codigo,titulo,ano,editora,autor)
    self.__ctrlLivros = ctrlLivros(self)
    self.__controladorUsuario = controladorUsuario(self)
    self.__controladorEmprestimo = controladorEmprestimo(self)
    self.__telaBiblioteca = telaBistema()
  
  #troquei o nome pra startSystem p n ficar taaaao obvio
  def startSystem(self):
    self.abre_tela()
  
  
   def incluirLivro(self, livro: Livro):
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

    def excluirLivro(self, livro: Livro):
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
  
  def cadastraAmigos(self):
    # Chama o controlador de Usuarios
    self.__controladorUsuario.abre_tela()

  def cadastra_emprestimos(self):
    pass
    # Chama o controlador de Emprestimos
  
