from usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome, telefone, email, data_nascimento, ano_atual):
        super().__init__(nome, telefone, email, data_nascimento, ano_atual)
