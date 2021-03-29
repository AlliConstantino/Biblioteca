from livro import Livro
from telaLivro import TelaLivro


class CtrlLivo:
  def __init__(self):
    self.__telaLivro = telaLivro()
    self.__livro = Livro
    
  def retornaLivro(self, titulo):
    for livro in self.__lista_livros:
        if (livro.titulo == titulo):
            return livro
    return False  
  
