class CtrlAmigo:
  def __init(self,nome):
    self.__nome = nome

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome  

