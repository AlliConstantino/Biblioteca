

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


