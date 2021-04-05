from MVC.Model.livro import Livro
from MVC.Model.usuario import Usuario
from MVC.Model.dataEmprestimo import DataEmprestimo

class Emprestimo:
  def __init__(self, livro: Livro, usuario: Usuario, dataEmprestimo: DataEmprestimo):
    self.__livro = livro
    self.__usuario = usuario
    self.__dataEmprestimo = dataEmprestimo

  @property
  def livro(self):
    return self.__livro

  @livro.setter
  def nome(self, livro):
    self.__livro = livro

  @property
  def usuario(self):
    return self.__usuario

  @usuario.setter
  def nome(self, usuario):
    self.__usuario = usuario

  @property
  def dataEmprestimo(self):
    return self.__dataEmprestimo

  @dataEmprestimo.setter
  def dataEmprestimo(self, dataEmprestimo):
    self.__dataEmprestimo = dataEmprestimo
