from bd import *
from conexaobd import conexao
from datetime import datetime, date
hoje=date.today()
conbd = conexao()

while True:
    print("Selecione a Opção Desejada:")
    print("1. Cadastrar Promoção")
    print("2. Alterar Promoção")
    print("3. Deletar Promoção")
    print("4. Listar Promoções")
    print("5. Sair")
    opcao=input("Escolha uma opcão:")
    if opcao=="1":
        a = input("Digite o Nome da Promoção: ")
        b = input("Digite a Descrição da Promoção: ")
        c = input("Digite a DataInicio da Promoção(formato: DD-MM-YYYY): ")
        c = datetime.strptime(c, "%d-%m-%Y").strftime("%Y-%m-%d") 
        d = input("Digite a DataFim da Promoção(formato: DD-MM-YYYY): ")
        d = datetime.strptime(d, "%d-%m-%Y").strftime("%Y-%m-%d")          
        cadastrarPromocao(conbd, a, b, c, d,)       
    if opcao=="2":
        a = input("Selecione a Promoção: ")
        b = input("Digite o Novo Nome da Promoção: ")
        c = input("Digite a Nova Descrição da Promoção: ")
        d = input("Digite a Nova Data Inicio da Promoção(formato: DD-MM-YYYY): ")
        d = datetime.strptime(d, "%d-%m-%Y").strftime("%Y-%m-%d") 
        e = input("Digite a Nova Data Fim da Promoção(formato: DD-MM-YYYY): ")
        e = datetime.strptime(e, "%d-%m-%Y").strftime("%Y-%m-%d")         
        atualizarPromocao(conbd, a, b, c, d, e,)
    if opcao=="3":
        a = input("Selecione a Promoção que Será Excluída: ")
        deletarPromocao(conbd, a)    
    if opcao=="4":
        listarPromocao(conbd)
    if opcao=="5":
        input("Volte Sempre")
    break