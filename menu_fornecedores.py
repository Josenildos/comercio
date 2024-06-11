from bd import *
from conexaobd import conexao

conbd = conexao()

while True:
    print("Selecione a Opção Desejada:")
    print("1. Cadastrar Fornecedor")
    print("2. Alterar Fornecedor")
    print("3. Deletar Fornecedor")
    print("4. Listar Fornecedores")
    print("5. Sair")
    opcao=input("Escolha uma opcão:")
    if opcao=="1":
        a = input("Digite o Nome do Fornecedor: ")
        b = input("Digite o Contato do Fornecedor: ")
        c = input("Digite o Endereço do Fornecedor: ")
        cadastrarFornecedor(conbd, a, b, c,)       
    if opcao=="2":
        a = input("Selecione o Fornecedor: ")
        b = input("Digite o Novo Nome do Fornecedor: ")
        c = input("Digite o Novo Contato do Fornecedor: ")
        d = input("Digite o Novo Endereço do Fornecedor: ")        
        atualizarFornecedor(conbd, a, b, c, d,)
    if opcao=="3":
        a = input("Selecione o Fornecedor que Será Excluído: ")
        deletarFornecedor(conbd, a)
    
    if opcao=="4":
        listarFornecedor(conbd)

    if opcao=="4":
        input("Volte Sempre")
    break