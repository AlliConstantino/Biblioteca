from autor import Autor
from livro import Livro
from ctrlLivro import CtrlLivro
from ctrlBiblioteca import CtrlBiblioteca

class TelaLivro:
  
  #mostra o livro
  def mostraLivro(self,titulo,capitulo,autor):
    
    return self.ctrlLivro.retornaLivro(titulo)
  
  #exclui livro
  def excluirLivro(self,titulo,capitulo,autor):
    #pegar o metodo excluir Livro do ctrlBiblioteca
    return self.ctrBiblioteca.exclui_livro()
  
  def incluiLivro(self,titulo,capitulo,autor):
    return self.ctrlBiblioteca.inclui_livro(self)
  
  #mostra nome do livro
  def telaOpcoes(self):
    print("-------- LIVROS ----------")
        print("1 - Incluir livro")
        print("2 - Alterar livro")
        print("3 - Mostrar livro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
  
  
