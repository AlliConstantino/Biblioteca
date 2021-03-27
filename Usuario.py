class Usuario:
  def __init__(self, nome: str, telefone: str, email: str, data_nascimento: int, ano_atual: Date):
    self.__nome = nome
    self.__telefone = telefone
    self.__email = email
    self.__data_nascimento = data_nascimento
    self.__ano_atual = ano_atual

  @property
  def nome(self):
    return self.__nome

  @property
  def telefone(self):
    return self.__telefone


  @property
  def email(self):
    return self.__email


  @property
  def data_nascimento(self):
    return self.__data_nascimento


  @property
  def ano_atual(self):
    return self.__ano_atual