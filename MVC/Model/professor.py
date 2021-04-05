from MVC.Model.usuario import Usuario

class Professor(Usuario):
    def __init__(self, nome, telefone, email, data_nascimento, ano_atual):
        super().__init__(nome, telefone, email, data_nascimento, ano_atual)