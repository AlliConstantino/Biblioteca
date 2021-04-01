from livro import Livro
from telaLivro import TelaLivro


class CtrlLivro:
  def __init__(self):
    self.__telaLivro = telaLivro()
    self.__livro = Livro
    
  def retornaLivro(self, titulo):
    for livro in self.__lista_livros:
        if (livro.titulo == titulo):
            return livro
    return False  
  
  def editaLivro(self,titulo,autor,genero,capitulo):
    #metodo para editar o livro
    return False
  
  #Metodo para checar se livro esta emprestado ou nao
  def checaStatus(self,livro):
    #Pergunta pro usuario qual livro ele quer checar
    livroAChecar = input("Qual livro você quer checar se esta disponivel?")
    #Pega o input e percorre o array dos livros emprestados,comparando se o livro buscado está la
    #Se estiver retorna uma msg dizendo que o livro esta emprestado e portanto nao esta disponivel
    #Se nao estiver retorna uma msg dizendo que esta disponivel e encerra
