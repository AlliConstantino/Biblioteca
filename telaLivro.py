
class TelaLivro():
    # mostra nome do livro
    def tela_opcoes(self):
        print("-------- LIVROS ----------")
        print("1 - Incluir livro")
        print("2 - Alterar livro")
        print("3 - Mostrar livro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    #sem função no código
    def pega_autor(self,autor):
        autor = input("Autor: ")

        return{"Autor", autor}



