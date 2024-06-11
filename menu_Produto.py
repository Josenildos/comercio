from bd import *
from conexaobd import conexao

conbd = conexao()

while True:
    print("Selecione a Opção Desejada: ")
    print("1. Cadastrar Protudo")
    print("2. Alterar Produto")
    print("3. Deletar Produto")
    print("4. Listar Produtos")
    print("5. Sair")
    
    opcao=input("Escolha uma opcão:")
    if opcao=="1":
        a = input("Digite o Nome do Produto: ")
        b = input("Digite a Descrição do Produto: ")
        c = float(input("Digite o Preço do Produto: "))
        cadastrarProdutos(conbd, a, b, c,)       
    if opcao=="2":
        n = input("Selecione o Produto: ")
        a = input("Digite o Novo Nome do Produto: ")
        b = input("Digite a Nova Descrição do Produto: ")
        c = float(input("Digite o Novo Preço do Produto: "))
        atualizarProduto(conbd, n, a, b, c,)
    if opcao=="3":
        a = input("Selecione o Produto que Será Excluído: ")
        deletarProduto(conbd, a)
    if opcao=="4":
        listarProdutos(conbd)        
    if opcao=="5":
        input("Volte Sempre")
    break





