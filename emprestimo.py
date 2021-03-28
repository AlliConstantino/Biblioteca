from livro import Livro
from usuario import Usuario
from dataEmprestimo import DataEmprestimo

class Emprestimo:
  def __init__(self, livro: Livro, usuario: Usuario, dataEmprestimo: DataEmprestimo):
    self.__livro = livro
    self.__usuario = usuario
    self.__dataEmprestimo = dataEmprestimo

  @property
  def livro(self):
    return self.__livro

  @property
  def usuario(self):
    return self.__usuario

  @property
  def dataEmprestimo(self):
    return self.__dataEmprestimo
