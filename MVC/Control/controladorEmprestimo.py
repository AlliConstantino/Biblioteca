from MVC.Model.emprestimo import Emprestimo
from MVC.Control.ctrlLivro import CtrlLivro
from MVC.Control.controladorUsuario import ControladorUsuario
from MVC.View.telaEmprestimo import TelaEmprestimo
from MVC.Model.dataEmprestimo import DataEmprestimo
from datetime import datetime
from datetime import timedelta as td

class ControladorEmprestimo():

    def __init__(self, ctrlBiblioteca):
        self.__ctrlBiblioteca = ctrlBiblioteca
        self.__emprestimo = []

        self.__tela_emprestimo = TelaEmprestimo()
        self.__controlador_livro = CtrlLivro()
        self.__controlador_usuario = ControladorUsuario()
        self.__data_emprestimo = DataEmprestimo()


    def inclui_emprestimo(self):
        dados_emprestimo = self.__tela_emprestimo.pega_dados_emprestimo()
        livro = self.__ctrlBiblioteca.ctrlLivro.retornaLivro(dados_emprestimo["tituloLivro"])
        usuario = self.__controlador_usuario.retornaUsuario(dados_emprestimo["nomeUsuario"])
        if livro:
            if usuario:
                emprestimo = Emprestimo(livro, usuario, DataEmprestimo())
                self.__emprestimo.append(emprestimo)
            else:
                print('Usuário inexistente, emprestimo não efetuado')
        elif usuario:
            print('Livro inexistente, emprestimo não efetuado')
        else:
            print('Livro e usuário inexistentes, emprestimo não efetuado')

    def verifica_status(self, emprestimo):
        dataAtual = datetime.now()
        atual = datetime.strptime(dataAtual.strftime("%Y-%m-%d"), "%Y-%m-%d")
        inicial = datetime.strptime(emprestimo.dataEmprestimo.dataInicial.strftime("%Y-%m-%d"), "%Y-%m-%d")
        final = datetime.strptime(emprestimo.dataEmprestimo.dataFinal.strftime("%Y-%m-%d"), "%Y-%m-%d")
        if abs((atual - inicial).days) > 7:
            tempoEmEmprestimo = abs((atual - final).days)
            return 'Seu emprestimo está atrasado há ' + str(tempoEmEmprestimo) + ' dias'
        else:
            tempoEmEmprestimo = abs((atual - inicial).days)
            return 'Seu emprestimo foi feito há ' + str(tempoEmEmprestimo) + ' dias'

    def lista_emprestimos(self):
        for emprestimo in self.__emprestimo:
            self.__tela_emprestimo.mostra_emprestimo({"tituloLivro": emprestimo.livro.titulo, "nomeUsuario": emprestimo.usuario.nome,
            "dataInicial": emprestimo.dataEmprestimo.dataInicial, "dataFinal": emprestimo.dataEmprestimo.dataFinal,
            "status": self.verifica_status(emprestimo)})

    def renova_emprestimo(self):
        dados_emprestimo = self.__tela_emprestimo.pega_dados_emprestimo()
        emprestimo_existe = self.retornaEmprestimo(dados_emprestimo['tituloLivro'])
        if emprestimo_existe:
            index = self.__emprestimo.index(emprestimo_existe)
            self.__emprestimo[index].dataEmprestimo.dataFinal = self.__emprestimo[index].dataEmprestimo.dataFinal + td(
                days=7)
            print('Empréstimo renovado para mais 7 dias!')
        else:
            print("Esse empréstimo ainda não foi criado.")

    def retornaEmprestimo(self, tituloLivro):
        for emprestimo in self.__emprestimo:
                if emprestimo.livro.titulo == tituloLivro:
                    return emprestimo
        return False

    def exclui_emprestimo(self): #verificar
        print('Insira o nome do livro que gostaria de excluir o empréstimo.')
        nome_livro = self.__tela_emprestimo.pega_dados_emprestimo('tituloLivro')
        livro_existe = self.retornaEmprestimo(nome_livro['tituloLivro'])

        if livro_existe:
            self.__emprestimo.remove(livro_existe)

            print("Empréstimo exluído com sucesso.")
        else:
            print("Esse empréstimo não existe!")

    def abre_tela(self):
        while True:
            opcao = self.__tela_emprestimo.tela_opcoes()
            if opcao == 1:
                self.inclui_emprestimo()
            elif opcao == 2:
                self.renova_emprestimo()
            elif opcao == 3:
                self.lista_emprestimos()
            elif opcao == 4:
                self.exclui_emprestimo()
            elif opcao == 0:
                self.__ctrlBiblioteca.abre_tela()
                break
