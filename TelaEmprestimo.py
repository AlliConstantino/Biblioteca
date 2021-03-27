import datetime

class TelaEmprestimo():
    mostra_opcoes()

    def mostra_opcoes():
        print('Digite 1 para incluir emprestimos')
        print('Digite 2 para alterar emprestimos')
        print('Digite 3 para excluír emprestimos')
        opcao = int(input())
        if opcao == 1:
            inclui_emprestimo()



    def inclui_emprestimo():
        while True:
            tituloLivroEmprestimo = input('Qual o título do livro?') 
            if (tituloLivroEmprestimo != 0):
                if (any(livro.titulo == tituloLivroEmprestimo for livro in Livros)):
                    nomeAlunoEmprestimo = input('Qual o nome do aluno que quer emprestar?')
                    if (nomeAlunoEmprestimo != 0):
                        if (any(aluno.nome == nomeAlunoEmprestimo for aluno in Alunos)):
                            Emprestimo(livro, aluno, datetime.datetime.now())
                            print('Emprestimo feito')
                        else:
                            print('Aluno não encontrado, por favor digite um aluno existente')
                            print('Para sair do emprestimo digite 0')
                    else:
                        print('Você digitou para sair')
                        break
                else: 
                    print('Livro não encontrado, por favor digite um Livro existente')
                    print('Para sair do emprestimo digite 0')
            else:
                print('Você digitou para sair')
                break
        mostra_opcoes()
