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
        data_entrada = input("Data de Nacimento (no formato DD/MM/AAAA): ")
        dia, mes, ano = map(int, data_entrada.split('/'))
        data_nascimento = datetime.date(ano, mes, dia)
        ano_atual = int(input("Ano atual: "))

        return {"Telefone": telefone, 'Email': email,
                'Data de nascimento': data_nascimento, 'Ano atual': ano_atual}


    def pega_nome(self, tipo: str):
        continua = True
        while continua:
            usuario = tipo.upper()
            print("-------- %s ---------" % usuario)
            nome = input("Nome: ")
            continua = any(char.isdigit() for char in nome)
            if continua:
                print('Digite um nome válido')

        return {"Nome": nome}

    def mostra_usuario(self, dados_usuario, tipo):
        print("Nome do %s: %s" % (tipo, dados_usuario["Nome"]))
        print("Fone do %s: %s" % (tipo, dados_usuario["Telefone"]))
        print("E-mail do %s: %s" % (tipo, dados_usuario['Email']))
        print('Nascimento do %s: ' % tipo + dados_usuario['Data de nascimento'].strftime("%d/%m/%Y"))
        print("Ano atual: %d" % (dados_usuario['Ano atual']))
