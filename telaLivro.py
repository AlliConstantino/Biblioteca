
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

    # mostra o livro
    def mostraLivro(self, titulo, capitulo, autor):
        return self.ctrlLivro.retornaLivro(titulo)

    # exclui livro
    def excluirLivro(self, titulo, capitulo, autor):
        # pegar o metodo excluir Livro do ctrlBiblioteca
        return self.ctrBiblioteca.exclui_livro()

    def incluirLivro(self, titulo, capitulo, autor):
        return self.ctrlBiblioteca.inclui_livro(self,titulo,capitulo,autor)
        
    def pega_nome(self, tipo: str):
        continua = True
        while continua:
            titulo = tipo.upper()
            print("-------- %s ---------" % titulo)
            titulo = input("Titulo: ")
            continua = any(char.isdigit() for char in titulo)
            if continua:
                print('Digite um nome válido')

        return {"Titulo": titulo}


