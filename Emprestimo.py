from Livro import Livro
from Aluno import Aluno
from DataEmprestimo import DataEmprestimo
import datetime

class Emprestimo():

  tempoLimite = 7

  def __init__(self, livro: Livro, aluno: Aluno, dataEmprestimo: DataEmprestimo):
    #o controlador da biblioteca cria a própria tela e os demais controladores que ele acessará.
    self.__livro = livro
    self.__aluno = aluno
    self.__dataEmprestimo = dataEmprestimo
  

  def altera_emprestimo(self, dataEmprestimo: DataEmprestimo):
    self.__dataEmprestimo = dataEmprestimo

  def mostra_emprestimo():
    print('O livro emprestado é:' %(livro.titulo))
    print('Quem emprestou foi: ' %(aluno.nome))
    print('A data do emprestimo é' %(dataEmprestimo.dataIncial))
    print('A data de fim do emprestimo é' %(dataEmprestimo.dataFinal))
    print('E a o status do emprestimo é:' %(verificaStatus())
      
  def verifica_status():
    tempoEmEmprestimo = (datetime.datetime.now() - self.__dataEmprestimo.dataInicial)
    if (tempoEmEmprestimo > tempoLimite):
        return 'Seu emprestimo está atrasado há ' + tempoEmEmprestimo - tempoLimite + 'dias'
    else:
        return 'Seu emprestimo foi feito há ' + tempoEmEmprestimo + 'dias'
