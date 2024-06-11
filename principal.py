from bd import *
from conexaobd import conexao

conbd = conexao()

a = input("Digite o Nome do Produto: ")
b = input("Digite a Descrição do Produto: ")
c = float(input("Digite o Preço do Produto: "))
cadastrarProdutos(conbd, a, b, c,)

conbd = conexao()

n = input("Selecione o Produto: ")
a = input("Digite o Nome do Produto: ")
b = input("Digite a Descrição do Produto: ")
c = float(input("Digite o Preço do Produto: "))
atualizarProduto(conbd, n, a, b, c,)