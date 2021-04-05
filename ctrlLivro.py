from autor import Autor
from livro import Livro
from telaLivro import TelaLivro
from livro import Livro
from telaLivro import TelaLivro

class CtrlLivro:
  def __init__(self):
    self.telaLivro = TelaLivro()

    
    
  def abre_tela(self):
      from ctrlBiblioteca import CtrlBiblioteca
      self.__ctrlBiblioteca = CtrlBiblioteca()
      while True:
          opcao = self.telaLivro.tela_opcoes()
          if opcao == 1:
            self.__ctrlBiblioteca.inclui_livro()
          elif opcao == 2:
            self.excluirLivro()
          elif opcao == 3:
            self.__mostraLivro()
          elif opcao == 0:
              self.__ctrlBiblioteca.abre_tela()
              break


    
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
          print ("livro já foi emprestado")
        else:
          print("livro disponivel")       
      # Se estiver retorna uma msg dizendo que o livro esta emprestado e portanto nao esta disponivel
      # Se nao estiver retorna uma msg dizendo que esta disponivel e encerra
