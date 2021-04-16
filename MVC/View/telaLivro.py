from MVC.View.tela import Tela


class TelaLivro(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

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

    def pega_titulo(self, tipo: str):
        continua = True
        while continua:
            print("-------- LIVRO ---------")
            titulo = input("Título: ")
            continua = any(char.isdigit() for char in titulo)
            if continua:
                print('Digite um título válido')

        return {"Titulo": titulo}

    def pega_dados_livro(self):
        autor = input("Autor: ")
        editora = input("Editora: ")

        return {'Autor': autor,
                'Editora': editora}

    def mostra_livro(self, dados_livro):
        print("Nome do livro: %s" % (dados_livro["Titulo"]))
        print("Autor do livro: %s" % (dados_livro["Autor"]))
        print("Editora do livro: %s" % (dados_livro['Editora']))



