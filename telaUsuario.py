import datetime


class TelaUsuario():

    def tela_opcoes(self):
        print("-------- USUÁRIOS ----------")
        print("1 - Incluir aluno")
        print("2 - Alterar aluno")
        print("3 - Listar alunos")
        print("4 - Excluir aluno")
        print("5 - Incluir professor")
        print("6 - Alterar professor")
        print("7 - Listar professor")
        print("8 - Excluir professor")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_usuario(self):
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        data_entrada = input("Data de Nacimento (no formato DD/MM/AA: ")
        dia, mes, ano = map(int, data_entrada.split('/'))
        data_nascimento = datetime.date(dia, mes, ano)
        ano_atual = input("Ano atual: ")

        return {"Telefone": telefone, 'Email': email,
                'Data de nascimento': data_nascimento, 'Ano atual': ano_atual}

        # nome ser str; telefone int; dtaa no formato solicitado, e-mail com @.

    def pega_nome(self, tipo: str):
        usuario = tipo.upper()
        print("-------- %s ---------" % usuario)
        nome = input("Nome: ")
        return {"Nome": nome}

    def mostra_usuario(self, dados_usuario, tipo):
        print("NOME DO %s: %s" % (tipo, dados_usuario["Nome"]))
        print("FONE DO %s: %s" % (tipo, dados_usuario["Telefone"]))
        print("E-MAIL DO %s: %s" % (tipo, dados_usuario['Email']))
        print("NASCIMENTO DO %s: %x" % (tipo, dados_usuario['Data de nascimento']))
        print("ANO ATUAl: %d" % (dados_usuario['Ano atual']))
