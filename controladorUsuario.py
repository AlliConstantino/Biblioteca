from telaUsuario import TelaUsuario
from aluno import Aluno
from professor import Professor

class ControladorUsuario:

  def __init__(self, controladorBiblioteca): #Controlador da Biblioteca

    self.__aluno = []
    self.__professor = []

    self.__telaUsuario = TelaUsuario() #pode ter o mesmo nome?
    self.__controladorBiblioteca = controladorBiblioteca



#Aluno
  def incluir_aluno(self):
    dados_aluno = self.__telaUsuario.pega_dados_aluno()

    aluno = Aluno(dados_aluno["Nome"], dados_aluno["Telefone"], dados_aluno['Email'], dados_aluno['Data de nascimento'], dados_aluno['Ano atual'])

    self.__aluno.append(aluno)

  def lista_alunos(self):
    for aluno in self.__aluno:
      self.__telaUsuario.mostra_aluno({"Nome": aluno.nome, "Telefone": aluno.telefone, 'Email': aluno.email, 'Data de nascimento': aluno.data_nascimento, 'Ano atual': aluno.ano_atual})

    #adicionar demais métodos

  def abre_tela(self):
    #Atenção: código incompleto: adicionar funcões para todas as opções da tela
    lista_opcoes = {1: self.incluir_amigo, 3: self.lista_amigos}

    continua = True
    while continua:
      lista_opcoes[self.__tela_amigo.tela_opcoes()]() #não entendi essa parte


#Professor

