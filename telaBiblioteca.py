class TelaBiblioteca:
  
  def tela_opcoes(self):
    print("-------- BIBLIOTECA ---------")
    print("Escolha sua opcao")
    print("1 - Livros")
    print("2 - Usuários")
    print("3 - Emprestimos")
    print("0 - Finalizar sistema")
    opcao = int(input("Escolha a opcao: "))
    return opcao
