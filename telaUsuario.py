import datetime


class TelaUsuario():

  def tela_opcoes(self):
    print("-------- USUÁRIOS ----------")
    print("1 - Incluir aluno")
    print("2 - Alterar aluno")
    print("3 - Listar alunos")
    print("4 - Excluir aluno")
    print("0 - Retornar")

    #Temos que rever como vamos fazer essas opções ao add professor

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_aluno(self):
    print("-------- INCLUIR ALUNO ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    data_entrada = input("Data de Nacimento (no formato DD/MM/AA: ")
    dia, mes, ano = map(int, data_entrada.split('/'))
    data_nascimento = datetime.date(dia, mes, ano)
    ano_atual = input("Ano atual: ")

    return {"Nome": aluno.nome, "Telefone": aluno.telefone, 'Email': aluno.email, 'Data de nascimento': aluno.data_nascimento, 'Ano atual': aluno.ano_atual}

  def mostra_aluno(self, dados_aluno):
    print("NOME DO ALUNO: ", dados_aluno["Nome"])
    print("FONE DO ALUNO: ", dados_aluno["Telefone"])
    print("E-MAIL DO ALUNO: ", dados_aluno['Email'])
    print("NASCIMENTO DO ALUNO: ", dados_aluno['Data de nascimento'])
    print("ANO ATUAl: ",dados_aluno['Ano atual'])

    #ADICIONAR demais métodos


#Adicionar Professor