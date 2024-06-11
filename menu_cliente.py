from bd import *
from conexaobd import conexao

conbd = conexao()

while True:
    print("Selecione a Opção Desejada:")
    print("1. Cadastrar Cliente")
    print("2. Alterar Cliente")
    print("3. Deletar cliente")
    print("4. Listar cliente")
    print("5. Sair")
    opcao=input("Escolha uma opcão:")
    if opcao=="1":
        a = input("Digite o Nome do Cliente: ")
        b = input("Digite o Sobrenome do Cliente: ")
        c = input("Digite o Endereço do Cliente: ") 
        d = input("Digite o Nome da Cidade do Cliente: ") 
        e = input("Digite o Código Postal do Cliente: ")
        cadastrarCliente(conbd, a, b, c, d, e,)       
    if opcao=="2":
        a = input("Selecione o Cliente: ")
        b = input("Digite o Novo Nome do Cliente: ")
        c = input("Digite o Novo Sobrenome do Cliente: ")
        d = input("Digite o Novo Endereço do Cliente: ")
        e = input("Digite a Nova Cidade do Cliente: ")
        f = input("Digite o Novo Código Postal do Cliente: ")
        atualizarCliente(conbd, a, b, c, d, e, f,)
    if opcao=="3":
        a = input("Selecione o Cliente que Será Excluído: ")
        deletarCliente(conbd, a)
    
    if opcao=="4":
        listarClientes(conbd)

    if opcao=="5":
        input("Volte Sempre")
    break