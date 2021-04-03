import email

import aluno
import professor
import usuario
#from ctrlBiblioteca import CtrlBiblioteca
from telaUsuario import TelaUsuario
from aluno import Aluno
from professor import Professor


class ControladorUsuario():

    def __init__(self):
        self.__alunos = []
        self.__professores = []

        self.__telaUsuario = TelaUsuario()
        #self.__ctrlBiblioteca = CtrlBiblioteca()


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
        for aluno in self.__alunos:
            self.__telaUsuario.mostra_usuario({"Nome": aluno.nome, "Telefone": aluno.telefone, 'Email': aluno.email,
                                             'Data de nascimento': aluno.data_nascimento, 'Ano atual': aluno.ano_atual}, 'Aluno')

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
        if isinstance(aluno, Aluno):
            aluno_incluso = False
            for i in self.__alunos:
                if i.nome == aluno.nome:
                    self.__alunos.remove(i)
                    aluno_incluso = True
            if not aluno_incluso:
                print('O aluno não estava incluso')
        else:
            print('Aluno inválido')


    # Professor
    def incluir_professor(self):
        dados_professor = self.__telaUsuario.pega_dados_usuario()  #deixar que nem incluir aluno

        professor = Professor(dados_professor["Nome"], dados_professor["Telefone"], dados_professor['Email'],
                              dados_professor['Data de nascimento'],
                              dados_professor['Ano atual'])

        self.__professores.append(professor)

    def lista_professores(self):
        for professor in self.__professores:
            self.__telaUsuario.mostra_usuario(
                {"Nome": professor.nome, "Telefone": professor.telefone, 'Email': professor.email,
                 'Data de nascimento': professor.data_nascimento, 'Ano atual': professor.ano_atual}, 'Professor')

    def exclui_professor(self): ##deixar que nem incluir aluno
        if isinstance(professor, Professor):
            professor_incluso = False
            for i in self.__professores:
                if i.nome == professor.nome:
                    self.__professores.remove(i)
                    professor_incluso = True
            if not professor_incluso:
                print('O professor não estava incluso')
        else:
            print('professor inválido')

    def altera_professor(self): ##deixar que nem incluir aluno
        dados_professor = self.__telaUsuario.pega_dados_usuario()
        professor_existe = self.retornaUsuario(dados_professor['Nome'], 'professor')
        if professor_existe:
            index = self.__professores.index(professor_existe)
            self.__professores[index].nome = dados_professor["Nome"]
            self.__professores[index].telefone = dados_professor["Telefone"]
            self.__professores[index].email = dados_professor['Email']
            self.__professores[index].data_nascimento = dados_professor['Data de nascimento']
            self.__professores[index].ano_atual = dados_professor['Ano atual']

            print("Professor alterado com sucesso.")
        else:
            print("Esse professor não existe!")

    def abre_tela(self):
        lista_opcoes = {0: self.__ctrlBiblioteca.abre_tela(), 1: self.incluir_aluno, 2: self.altera_aluno, 3: self.lista_alunos, 4: self.exclui_aluno, 5: self.incluir_professor(), 6: self.altera_professor(),
                        7: self.lista_professores(), 8: self.exclui_professor()}

        continua = True
        while continua:
            lista_opcoes[self.__telaUsuario.tela_opcoes()]()
