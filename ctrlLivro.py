from autor import Autor
from livro import Livro
from telaLivro import TelaLivro

class CtrlLivro:
  def __init__(self):
    self.__telaLivro = TelaLivro()
    self.__livro = Livro

  def retornaLivro(self,titulo):
      for livro in self.__lista_livros:
          if(livro.titulo == titulo):
              return livro
      return False



  def incluirAutor(self, autor: Autor):
      if isinstance(autor, Autor):
          autor_incluso = False
          for i in self.__autores:
              if i.codigo == autor.codigo:
                  autor_incluso = True
          if not autor_incluso:
              self.__autores.append(autor)
          else:
              print('O autor ja estava incluso.')
      else:
          print('Autor invalido.')

  def excluirAutor(self, autor: Autor):
      if isinstance(autor, Autor):
          autor_incluso = False
          for i in self.__autores:
              if i.codigo == autor.codigo:
                  self.__autores.remove(i)
                  autor_incluso = True
          if not autor_incluso:
              print('O autor nao estava incluso.')
      else:
          print('Autor invalido.')

  def editaLivro(self, titulo, autor, genero, capitulo):
      # metodo para editar o livro
      return False

      # Metodo para checar se livro esta emprestado ou nao

      #tá certo sera?
  def checaStatus(self, livro):
      # Pergunta pro usuario qual livro ele quer checar
      livroAChecar = input("Qual livro você quer checar se esta disponivel?")
      # Pega o input e percorre o array dos livros emprestados,comparando se o livro buscado está la
      for i in self.__livro:
        if self.livro.status() == "emprestado":
          print ("livro já foi emprestado)
        else:
          print("livro disponivel")       
      # Se estiver retorna uma msg dizendo que o livro esta emprestado e portanto nao esta disponivel
      # Se nao estiver retorna uma msg dizendo que esta disponivel e encerra
