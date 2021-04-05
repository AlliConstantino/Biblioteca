import datetime

class Usuario:
  def __init__(self, nome: str, telefone: str, email: str, data_nascimento: datetime, ano_atual: int):
    self.__nome = nome
    self.__telefone = telefone
    self.__email = email
    self.__data_nascimento = data_nascimento
    self.__ano_atual = ano_atual

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @property
  def telefone(self):
    return self.__telefone

  @telefone.setter
  def telefone(self, telefone):
    self.__telefone = telefone

  @property
  def email(self):
    return self.__email

  @email.setter
  def email(self, email):
    self.__email = email

  @property
  def data_nascimento(self):
    return self.__data_nascimento

  @data_nascimento.setter
  def data_nascimento(self, data_nascimento):
    self.__data_nascimento = data_nascimento

  @property
  def ano_atual(self):
    return self.__ano_atual

  @ano_atual.setter
  def ano_atual(self, ano_atual):
    self.__ano_atual = ano_atual