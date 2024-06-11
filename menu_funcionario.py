from bd import *
from conexaobd import conexao

conbd = conexao()

while True:
    print("Selecione a Opção Desejada:")
    print("1. Cadastrar Funcionario")
    print("2. Alterar Funcionario")
    print("3. Deletar Funcionario")
    print("4. Listar Funcionarios")
    print("5. Sair")
    opcao=input("Escolha uma opcão:")
    if opcao=="1":
        a = input("Digite o Nome do Funcionario: ")
        b = input("Digite o Cargo do Funcionario: ")
        c = input("Digite o Departamento do Funcionario: ")
        cadastrarFuncionario(conbd, a, b, c,)       
    if opcao=="2":
        a = input("Selecione o Funcionario: ")
        b = input("Digite o Novo Nome do Funcionario: ")
        c = input("Digite o Novo Cargo do Funcionario: ")
        d = input("Digite o Novo Departamento do Funcionario: ")        
        atualizarFuncionario(conbd, a, b, c, d,)
    if opcao=="3":
        a = input("Selecione o Funcionario que Será Excluído: ")
        deletarFuncionario(conbd, a)
    
    if opcao=="4":
        listarFuncionario(conbd)

    if opcao=="5":
        input("Volte Sempre")
    break