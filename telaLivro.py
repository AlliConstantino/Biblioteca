from autor import Autor
from livro import Livro
from ctrlLivro import CtrlLivro
from ctrlBiblioteca import CtrlBiblioteca

class TelaLivro:
  
  def mostraLivro(self,titulo,capitulo,autor):
    #pegar o metodo mostra Livro do ctrlBiblioteca
    return False
  
  #exclui livro
  def excluirLivro(self,titulo,capitulo,autor):
    #pegar o metodo excluir Livro do ctrlBiblioteca
    return False
  
  #mostra nome do livro
  def telaOpcoes(self):
    print("-------- LIVROS ----------")
        print("1 - Incluir livro")
        print("2 - Alterar livro")
        print("3 - Mostrar livro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
  #
  
