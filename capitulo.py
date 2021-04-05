class Capitulo:
  #init
  def __init__(self, numeroCap: int, nomeCap: str):
        self.__numeroCap = numeroCap
        self.__nomeCap = nomeCap

  #getter numeroCap
  @property
  def mostraNumeroCap(self):
    return self.__numeroCap
  
  #getter nomeCap
  @property
  def mostraNomeCap(self):
    return self.__nomeCap
  
  #getter cap
  def mostraCap(self,nomeCap,numeroCap):
    print(nomeCap, numeroCap)
