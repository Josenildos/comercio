from bd import *
from conexaobd import conexao
from datetime import date
conbd = conexao()

while True:
    print("Selecione a Opção Desejada:")
    print("1. Fazer Pedido")
    print("2. Alterar o Pedido")
    print("3. Deletar o Pedido")    
    print("4. Sair")
    opcao=input("Escolha uma opcão:")
    if opcao=="1":
        a = input("Digite o Nome do Cliente: ")
        b = input("Digite o Produto: ")
        c = int(input("Digite a Quantidade: "))
        d = input("Escolha a forma de Pagamento: ")
        hoje=date.today()
        cadastrarPedido(conbd, a, b, c, d, hoje)
    
    
    
    
    
    
    
    
    
    
    # if opcao=="2":
    #     a = input("Selecione o Cliente: ")
    #     b = input("Digite o Novo Nome do Cliente: ")
    #     c = input("Digite o Novo Sobrenome do Cliente: ")
    #     d = input("Digite o Novo Endereço do Cliente: ")
    #     e = input("Digite a Nova Cidade do Cliente: ")
    #     f = input("Digite o Novo Código Postal do Cliente: ")
    #     alterarPedido(conbd, a, b, c, d, e, f,)
    # if opcao=="3":
    #     a = input("Selecione o Cliente que Será Excluído: ")
    #     deletarPedido(conbd, a)     
    # if opcao=="4":
    #     input("Volte Sempre")
    # break