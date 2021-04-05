
from MVC.Model.livro import Livro
from MVC.View.telaLivro import TelaLivro
from MVC.View.telaBiblioteca import TelaBiblioteca


class CtrlLivro:
    def __init__(self, ctrlBiblioteca):
        self.__ctrlBiblioteca = ctrlBiblioteca
        self.__telaBiblioteca = TelaBiblioteca()
        self.telaLivro = TelaLivro()
        self.__livros = []

    def abre_tela(self):
        while True:
            opcao = self.telaLivro.tela_opcoes()
            if opcao == 1:
                self.inclui_livro()
            elif opcao == 2:
                self.excluirLivro()  # não funciona
            elif opcao == 3:
                self.lista_livro()
            elif opcao == 0:
                self.__ctrlBiblioteca.abre_tela()
                break

    def inclui_livro(self):
        nome_livro = self.__telaBiblioteca.pega_titulo('Titulo')
        livro_existe = self.retornaLivro(nome_livro['Titulo'])

        if livro_existe:
            print('Esse livro já existe.')
        else:
            dados_livro = self.__telaBiblioteca.pega_dados_livro()
            livro = Livro(nome_livro["Titulo"], dados_livro["Autor"], dados_livro["Editora"])
            self.__livros.append(livro)
            print("Livro adicionado com sucesso!")

    def retornaLivro(self, titulo):
        for livro in self.__livros:
            if livro.titulo == titulo:
                return livro
        return False

    def exclui_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            livro_incluso = False
            for i in self.__livros:
                if i.codigo == livro.codigo:
                    self.__livros.remove(i)
                    livro_incluso = True
            if not livro_incluso:
                print('O livro nao estava incluso.')
        else:
            print('Livro invalido.')

    def lista_livro(self):
        if len(self.__livros) > 0:
            for livro in self.__livros:
                self.__telaBiblioteca.mostra_livro(
                    {'Titulo': livro.titulo, 'Autor': livro.autor, 'Editora': livro.editora})
        else:
            print('Nenhum livro cadastrado.')

    # não está funcionando
    def editaLivro(self, titulo, autor, genero, capitulo):
        # metodo para editar o livro
        return False

        # Metodo para checar se livro esta emprestado ou nao

    # não está funcionando
    def checaStatus(self, livro):
        # Pergunta pro usuario qual livro ele quer checar
        livroAChecar = input("Qual livro você quer checar se esta disponivel?")
        # Pega o input e percorre o array dos livros emprestados,comparando se o livro buscado está la
        for i in self.__livro:
            if self.livro.status() == "emprestado":
                print("livro já foi emprestado")
            else:
                print("livro disponivel")
                # Se estiver retorna uma msg dizendo que o livro esta emprestado e portanto nao esta disponivel
        # Se nao estiver retorna uma msg dizendo que esta disponivel e encerra
