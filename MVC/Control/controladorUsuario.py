
from MVC.View.telaBiblioteca import TelaBiblioteca
from MVC.View.telaUsuario import TelaUsuario
from MVC.Model.aluno import Aluno
from MVC.Model.professor import Professor



class ControladorUsuario():

    def __init__(self, ctrlBiblioteca):
        self.__ctrlBiblioteca = ctrlBiblioteca
        self.__alunos = []
        self.__professores = []

        self.__telaUsuario = TelaUsuario()
        self.__telaBiblioteca = TelaBiblioteca()


    # Aluno
    def incluir_aluno(self):
        nome_aluno = self.__telaUsuario.pega_nome('Aluno')
        aluno_existe = self.retornaUsuario(nome_aluno['Nome'], 'aluno')

        if aluno_existe:
            print('Esse aluno já existe.')
        else:
            dados_aluno = self.__telaUsuario.pega_dados_usuario()
            aluno = Aluno(nome_aluno["Nome"], dados_aluno["Telefone"], dados_aluno['Email'],
                          dados_aluno['Data de nascimento'],
                          dados_aluno['Ano atual'])
            self.__alunos.append(aluno)
            print("Aluno adicionado com sucesso!")

    def lista_alunos(self):
        if len(self.__alunos) > 0:
            for aluno in self.__alunos:
                self.__telaUsuario.mostra_usuario({"Nome": aluno.nome, "Telefone": aluno.telefone, 'Email': aluno.email,
                                             'Data de nascimento': aluno.data_nascimento, 'Ano atual': aluno.ano_atual}, 'Aluno')
        else:
            print('Nenhum aluno cadastrado.')

    def retornaUsuario(self, nome, tipo = 'ambos'):
        if tipo != 'professor':
            for aluno in self.__alunos:
                if aluno.nome == nome:
                    return aluno
        if tipo != 'aluno':
            for professor in self.__professores:
                if professor.nome == nome:
                    return professor
        return False


    def altera_aluno(self):
        print('Insira o nome do aluno que gostaria de alterar.')
        nome_aluno = self.__telaUsuario.pega_nome('Aluno')
        aluno_existe = self.retornaUsuario(nome_aluno['Nome'], 'aluno')

        if aluno_existe:
            dados_aluno = self.__telaUsuario.pega_dados_usuario()
            index = self.__alunos.index(aluno_existe)
            self.__alunos[index].nome = nome_aluno["Nome"]
            self.__alunos[index].telefone = dados_aluno["Telefone"]
            self.__alunos[index].email = dados_aluno['Email']
            self.__alunos[index].data_nascimento = dados_aluno['Data de nascimento']
            self.__alunos[index].ano_atual = dados_aluno['Ano atual']

            print("Aluno alterado com sucesso.")
        else:
            print("Esse aluno não existe!")


    def exclui_aluno(self):
        print('Insira o nome do aluno que gostaria de excluir.')
        nome_aluno = self.__telaUsuario.pega_nome('Aluno')
        aluno_existe = self.retornaUsuario(nome_aluno['Nome'], 'aluno')

        if aluno_existe:
            self.__alunos.remove(aluno_existe)

            print("Aluno exluído com sucesso.")
        else:
            print("Esse aluno não existe!")

    # Professor
    def incluir_professor(self):
        nome_professor = self.__telaUsuario.pega_nome('Professor')
        professor_existe = self.retornaUsuario(nome_professor['Nome'], 'professor')

        if professor_existe:
            print('Esse professor já existe.')
        else:
            dados_professor = self.__telaUsuario.pega_dados_usuario()
            professor = Professor(nome_professor["Nome"], dados_professor["Telefone"], dados_professor['Email'],
                              dados_professor['Data de nascimento'],
                              dados_professor['Ano atual'])

            self.__professores.append(professor)
            print("Professor adicionado com sucesso!")

    def lista_professores(self):
        for professor in self.__professores:
            self.__telaUsuario.mostra_usuario(
                {"Nome": professor.nome, "Telefone": professor.telefone, 'Email': professor.email,
                 'Data de nascimento': professor.data_nascimento, 'Ano atual': professor.ano_atual}, 'Professor')

    def exclui_professor(self):
        print('Insira o nome do professor que gostaria de excluir.')
        nome_professor = self.__telaUsuario.pega_nome('Professor')
        professor_existe = self.retornaUsuario(nome_professor['Nome'], 'professor')

        if professor_existe:
            self.__professores.remove(professor_existe)

            print("Professor exluído com sucesso.")
        else:
            print("Esse professor não existe!")

    def altera_professor(self):
        nome_professor = self.__telaUsuario.pega_nome('Professor')
        professor_existe = self.retornaUsuario(nome_professor['Nome'], 'professor')
        if professor_existe:
            dados_professor = self.__telaUsuario.pega_dados_usuario()
            index = self.__professores.index(professor_existe)
            self.__professores[index].nome = nome_professor["Nome"]
            self.__professores[index].telefone = dados_professor["Telefone"]
            self.__professores[index].email = dados_professor['Email']
            self.__professores[index].data_nascimento = dados_professor['Data de nascimento']
            self.__professores[index].ano_atual = dados_professor['Ano atual']

            print("Professor alterado com sucesso.")
        else:
            print("Esse professor não existe!")


    def abre_tela(self):
        #from ctrlBiblioteca import CtrlBiblioteca
        #self.__ctrlBiblioteca = CtrlBiblioteca()
        while True:
            opcao = self.__telaUsuario.tela_opcoes()
            if opcao == 1:
                self.incluir_aluno()
            elif opcao == 2:
                self.altera_aluno()
            elif opcao == 3:
                self.lista_alunos()
            elif opcao == 4:
                self.exclui_aluno()
            elif opcao == 5:
                self.incluir_professor()
            elif opcao == 6:
                self.altera_professor()
            elif opcao == 7:
                self.lista_professores()
            elif opcao == 8:
                self.exclui_professor()
            elif opcao == 0:
                self.__ctrlBiblioteca.abre_tela()
                break

