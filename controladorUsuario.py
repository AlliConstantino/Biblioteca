import email

import aluno
import professor
import usuario
from telaUsuario import TelaUsuario
from aluno import Aluno
from professor import Professor


class ControladorUsuario():

    def __init__(self, ctrlBiblioteca):
        # super().__init__(nome, telefone, email, data_nascimento, ano_atual)
        self.__aluno = []
        self.__professor = []

        self.__telaUsuario = TelaUsuario()
        self.__ctrlBiblioteca = ctrlBiblioteca

    # Nao esquecer de lidar com as excecoes

    # Aluno
    def incluir_aluno(self):
        dados_aluno = self.__telaUsuario.pega_dados_aluno()

        aluno = Aluno(dados_aluno["Nome"], dados_aluno["Telefone"], dados_aluno['Email'],
                      dados_aluno['Data de nascimento'],
                      dados_aluno['Ano atual'])

        self.__aluno.append(aluno)

    def lista_alunos(self):
        for aluno in self.__aluno:
            self.__telaUsuario.mostra_aluno({"Nome": aluno.nome, "Telefone": aluno.telefone, 'Email': aluno.email,
                                             'Data de nascimento': aluno.data_nascimento, 'Ano atual': aluno.ano_atual})

    def altera_aluno(self):
        dados_aluno = self.__telaUsuario.pega_dados_aluno()

        aluno = Aluno(dados_aluno["Nome"], dados_aluno["Telefone"], dados_aluno['Email'],
                      dados_aluno['Data de nascimento'],
                      dados_aluno['Ano atual'])

        self.__aluno.append(aluno)

    '''
        def retornaAluno(self, aluno):
            for aluno in self.__listaAlunos:
                if (usuario.aluno = aluno):
                    print(aluno.nome)
                    print(aluno.email)
                    print(aluno.emprestimos)
    '''

    def exclui_aluno(self):
        if isinstance(aluno, Aluno):
            aluno_incluso = False
            for i in self.__aluno:
                if i.nome == aluno.nome:
                    self.__aluno.remove(i)
                    aluno_incluso = True
            if not aluno_incluso:
                print('O aluno não estava incluso')
        else:
            print('Aluno inválido')

    # Professor

    def incluir_professor(self):
        dados_professor = self.__telaUsuario.pega_dados_professor()

        professor = Professor(dados_professor["Nome"], dados_professor["Telefone"], dados_professor['Email'],
                              dados_professor['Data de nascimento'],
                              dados_professor['Ano atual'])

        self.__professor.append(professor)

    def lista_professores(self):
        for professor in self.__professor:
            self.__telaUsuario.mostra_professor(
                {"Nome": professor.nome, "Telefone": professor.telefone, 'Email': professor.email,
                 'Data de nascimento': professor.data_nascimento, 'Ano atual': professor.ano_atual})

    def exclui_professor(self):
        if isinstance(professor, Professor):
            professor_incluso = False
            for i in self.__professor:
                if i.nome == professor.nome:
                    self.__professor.remove(i)
                    professor_incluso = True
            if not professor_incluso:
                print('O professor não estava incluso')
        else:
            print('professor inválido')

    def abre_tela(self):
        # Atenção: código incompleto: adicionar funcões para todas as opções da tela
        lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno}

        continua = True
        while continua:
            lista_opcoes[self.__tela_alunos.tela_opcoes()]()  # não entendi essa parte
