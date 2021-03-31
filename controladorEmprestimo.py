from ctrlLivro import CtrlLivro
from ctrlBiblioteca import CtrlBiblioteca
from controladorUsuario import ControladorUsuario
from telaEmprestimo import TelaEmprestimo
from emprestimo import Emprestimo
from livro import Livro
from usuario import Usuario
from dataEmprestimo import DataEmprestimo
import datetime



class ControladorEmprestimo():

  def __init__(self, controlador_sistema):

    self.__emprestimos = []

    self.__tela_emprestimo = TelaEmprestimo()
    self.__controlador_livro = CtrlLivro()
    self.__controlador_usuario = ControladorUsuario()
#    self.__data_emprestimo = DataEmprestimo() - talvez precise usar isso
    self.__ctrlBiblioteca = CtrlBiblioteca


"""
  incluir esse método no ControladorLivro

  def retornaLivro(self, titulo):
    for livro in self.__lista_livros:
        if (livro.titulo == titulo):
            return livro
    return False
"""

"""
  incluir esse método no ControladorUsuario

  def retornaUsuario(self, nome):
    for aluno in self.__lista_alunos:
        if (aluno.nome == nome):
            return aluno
    for professor in self.__lista_professores:
        if (professor.nome == nome):
            return professor
    return False
"""


"""
  a classe DataEmprestimo deve receber uma data no init, 
  sendo essa a data atual (datetime.datetime.now())
  e irá definitir:
  self.__dataInicial = dataAtual
  self.__dataFinal = dataAtual + datetime.timedelta(days=7)
"""
    
  def incluir_emprestimo(self):
    dados_emprestimo = self.__tela_emprestimo.pega_dados_emprestimo()
    livro = self.__controlador_livro.retornaLivro(dados_emprestimo["tituloLivro"])
    usuario = self.__controlador_usuario.retornaUsuario(dados_emprestimo["nomeUsuario"])
    if (livro):
        if (usuario):
            emprestimo = Emprestimo(livro, usuario, DataEmprestimo(datetime.datetime.now()))
            self.__emprestimos.append(emprestimo)
        else:
            print('Usuário inexistente, emprestimo não efetuado')
    elif(usuario):
        print('Livro inexistente, emprestimo não efetuado')
    else: 
        print('Livro e usuário inexistentes, emprestimo não efetuado')

# Pensar em atribuir datetime.timedelta(days=7) como atributo "tempoLimite" na classe DataEmprestimo
# verifica_Status ainda precisa de alguns ajustes
  def verifica_status(self, emprestimo):
    tempoEmEmprestimo = (datetime.datetime.now() - emprestimo.dataEmprestimo.dataInicial)
    if (datetime.datetime.now() > emprestimo.dataEmprestimo.dataFinal):
        return 'Seu emprestimo está atrasado há ' + tempoEmEmprestimo - datetime.timedelta(days=7) + ' dias'
    else:
        return 'Seu emprestimo foi feito há ' + tempoEmEmprestimo + 'dias'

  def lista_emprestimos(self):
    for emprestimo in self.__emprestimos:
      self.__tela_emprestimo.mostra_emprestimo({"tituloLivro": emprestimo.livro.titulo, "nomeUsuario": emprestimo.usuario.nome, 
      "dataInicial": emprestimo.dataEmprestimo.dataIncial, "dataFinal": emprestimo.dataEmprestimo.dataFinal,
      "status": verifica_status(emprestimo)})

  def abre_tela(self):
    #Atenção: código incompleto: adicionar funcões para todas as opções da tela
    lista_opcoes = {1: self.incluir_emprestimo, 3: self.lista_emprestimos}

    continua = True
    while continua:
      lista_opcoes[self.__tela_emprestimo.tela_opcoes()]()

