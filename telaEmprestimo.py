import datetime

class TelaEmprestimo():

  def tela_opcoes(self):
    print("-------- Emprestimos ----------")
    print("Escolha a opcao")
    print("1 - Incluir Emprestimo")
    print("2 - Alterar Emprestimo")
    print("3 - Listar Emprestimo")
    print("4 - Excluir Emprestimo")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_emprestimo(self):
    print("-------- INCLUIR EMPRESTIMO ----------")
    tituloLivro = input("Título do livro: ")
    nomeUsuario = input("Nome de quem irá emprestá-lo: ")

    return {"tituloLivro": tituloLivro, "nomeUsuario": nomeUsuario}

  def mostra_emprestimo(self, dados_emprestimo):
    print('O livro emprestado é: ' dados_emprestimo["tituloLivro"])
    print('Quem emprestou foi: ' dados_emprestimo["nomeUsuario"])
    print('A data do emprestimo é' dados_emprestimo["dataInicial"])
    print('A data de fim do emprestimo é' dados_emprestimo["dataFinal"])
    print('E a o status do emprestimo é:' dados_emprestimo["status"])
