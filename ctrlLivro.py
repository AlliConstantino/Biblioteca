from autor import Autor
from livro import Livro
from telaLivro import TelaLivro
from livro import Livro
from telaLivro import TelaLivro

class CtrlLivro:
  def __init__(self):
    self.telaLivro = TelaLivro()
    self.__livro = Livro
    self.livros = [] #array que vai guardar a lista de livros
    
    
  def abre_tela(self):
      opcao = self.telaLivro.tela_opcoes()
      if opcao == 1:
        self.incluirLivro()
      elif opcao == 2:
        self.excluirLivro()
      elif opcao == 3:
        self.__mostraLivro()
      elif opcao != 0:
        self.abre_tela()
            
  def retornaLivro(self,livros: []):
      for livro in self.livros:
          if(livro.titulo == titulo):
              return livro
      return False

  def incluirLivro(self):
      nome_livro = self.telaLivro.pega_titulo('Titulo')
      autor_livro = self.telaLivro.pega_autor('Autor')
      livro_existe = self.retornaLivro(nome_livro['Titulo']) #serve para ver se o livro ja existe no array

      if livro_existe:
        print('Esse livro já existe.')
      else:
        dados_livro = self.telaLivro.pega_dados_livro()
        livro = Livro(nome_livro["Titulo"], dados_livro["Autor"])
        self.livros.append(livro)
        print("Livro adicionado com sucesso!")
    
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
