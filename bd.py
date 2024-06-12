def cadastrarProdutos(conbd, nome, descricao, preco):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO produtos (Nome, Descricao, Preco) VALUES (%s, %s, %s)'
    val = (nome, descricao, preco)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Produto Cadastrado com Sucesso")
    
    mycursor.close()

def atualizarProduto(conbd, anterior, nome, descricao, preco):
    mycursor = conbd.cursor()
    sql = 'UPDATE produtos SET Nome = %s, Descricao = %s, Preco = %s WHERE Nome = %s'
    val = (nome, descricao, preco, anterior)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Produto Atualizado com Sucesso")
    
    mycursor.close()

def deletarProduto(conbd, nome):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM produtos WHERE Nome = %s'
    val = (nome,)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Produto Excluido com sucesso")
    
    mycursor.close()

def listarProdutos(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM Produtos'
    mycursor.execute(sql)
    Lista = mycursor.fetchall()
    for i in Lista:
        print(i)

def cadastrarCliente(conbd, Nome, Sobrenome, Endereco, Cidade, CodigoPostal):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO clientes (Nome, Sobrenome, Endereco, Cidade, CodigoPostal) VALUES (%s, %s, %s, %s, %s)'
    val = (Nome, Sobrenome, Endereco, Cidade, CodigoPostal)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Cliente Cadastrado com Sucesso")
    
    mycursor.close()

def atualizarCliente(conbd, anterior, Nome, Sobrenome, Endereco, Cidade, CodigoPostal):
    mycursor = conbd.cursor()
    sql = 'UPDATE clientes SET Nome = %s, Sobrenome = %s, Endereco = %s, Cidade = %s, CodigoPostal = %s WHERE Nome = %s'
    val = (Nome, Sobrenome, Endereco, Cidade, CodigoPostal, anterior)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Cliente Atualizado com Sucesso")
    
    mycursor.close()

def deletarCliente(conbd, Nome):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM clientes WHERE Nome = %s'
    val = (Nome,)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Cliente Excluido com sucesso")
    
    mycursor.close()

def listarClientes(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM clientes'
    mycursor.execute(sql)
    Lista = mycursor.fetchall()
    for i in Lista:
        print(i)

def cadastrarFornecedor(conbd, Nome, Contato, Endereco):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO fornecedores (Nome, Contato, Endereco) VALUES (%s, %s, %s)'
    val = (Nome, Contato, Endereco)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Fornecedor Cadastrado com Sucesso")
    
    mycursor.close()

def atualizarFornecedor(conbd, anterior, Nome, Contato, Endereco):
    mycursor = conbd.cursor()
    sql = 'UPDATE fornecedores SET Nome = %s, Contato = %s, Endereco = %s WHERE Nome = %s'
    val = (Nome, Contato, Endereco, anterior)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Fornecedor Atualizado com Sucesso")
    
    mycursor.close()

def deletarFornecedor(conbd, Nome):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM fornecedores WHERE Nome = %s'
    val = (Nome,)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Fornecedor Excluido com sucesso")
    
    mycursor.close()

def listarFornecedor(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM fornecedores'
    mycursor.execute(sql)
    Lista = mycursor.fetchall()
    for i in Lista:
        print(i)

def cadastrarFuncionario(conbd, Nome, Cargo, Departamento):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO funcionarios (Nome, Cargo, Departamento) VALUES (%s, %s, %s)'
    val = (Nome, Cargo, Departamento)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Funcionário Cadastrado com Sucesso")
    
    mycursor.close()

def atualizarFuncionario(conbd, anterior, Nome, Cargo, Departamento):
    mycursor = conbd.cursor()
    sql = 'UPDATE funcionarios SET Nome = %s, Cargo = %s, Departamento = %s WHERE Nome = %s'
    val = (Nome, Cargo, Departamento, anterior)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Funcionário Atualizado com Sucesso")
    
    mycursor.close()

def deletarFuncionario(conbd, Nome):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM funcionarios WHERE Nome = %s'
    val = (Nome,)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Funcionário Excluido com sucesso")
    
    mycursor.close()

def listarFuncionario(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM funcionarios'
    mycursor.execute(sql)
    Lista = mycursor.fetchall()
    for i in Lista:
        print(i)

def cadastrarPromocao(conbd, Nome, Descricao, DataInicio, DataFim):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO promocoes (Nome, Descricao, DataInicio, DataFim) VALUES (%s, %s, %s, %s)'
    val = (Nome, Descricao, DataInicio, DataFim)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Promoção Cadastrada com Sucesso")
    
    mycursor.close()

def atualizarPromocao(conbd, anterior, Nome, Descricao, DataInicio, DataFim):
    mycursor = conbd.cursor()
    sql = 'UPDATE promocoes SET Nome = %s, Descricao = %s, DataInicio = %s, DataFim = %s WHERE Nome = %s'
    val = (Nome, Descricao, DataInicio, DataFim, anterior)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Promoção Atualizada com Sucesso")
    
    mycursor.close()

def deletarPromocao(conbd, Nome):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM promocoes WHERE Nome = %s'
    val = (Nome,)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Promoção Excluida com sucesso")
    
    mycursor.close()

def listarPromocao(conbd):
    mycursor = conbd.cursor()
    sql = 'SELECT * FROM promocoes'
    mycursor.execute(sql)
    Lista = mycursor.fetchall()
    x = Lista[0]
    print(x[1])
    y = Lista[0]
    print(y[2])
    w = Lista[0]
    print(w[3])
    z = Lista[0]
    print(z[4])
    x = Lista[1]
    print(x[1])
    y = Lista[1]
    print(y[2])
    w = Lista[1]
    print(w[3])
    z = Lista[1]
    print(z[4])
    x = Lista[2]
    print(x[1])
    y = Lista[2]
    print(y[2])
    w = Lista[2]
    print(w[3])
    z = Lista[2]
    print(z[4])
    x = Lista[3]
    print(x[1])
    y = Lista[3]
    print(y[2])
    w = Lista[3]
    print(w[3])
    z = Lista[3]
    print(z[4])
    x = Lista[4]
    print(x[1])
    y = Lista[4]
    print(y[2])
    w = Lista[4]
    print(w[3])
    z = Lista[4]
    print(z[4])
    x = Lista[5]
    print(x[1])
    y = Lista[5]
    print(y[2])
    w = Lista[5]
    print(w[3])
    z = Lista[5]
    print(z[4])

def cadastrarPedido(conbd, nomeCliente, nomeProduto, quantProduto, formaPag, hoje):
    mycursor = conbd.cursor()
    sql = 'SELECT ID_Cliente FROM clientes where nome = %s' 
    val = (nomeCliente,)
    mycursor.execute(sql,val)
    ID_Cliente = mycursor.fetchone()[0]

    print("------------->",  ID_Cliente)

    conbd.commit()
    print("Pedido Incluido com Sucesso")


    sql = 'INSERT INTO pedidos (Data_Pedido, ID_Cliente, Total) VALUES (%s, %s, %s, %s)'
    val = (ID_Pedido, Data_Pedido, ID_Cliente, Total)
    mycursor.execute(sql,val)
    conbd.commit()
    print("Pedido Incluido com Sucesso")
    
    mycursor.close()

# def alterarPedido(conbd, anterior, Nome, Sobrenome, Endereco, Cidade, CodigoPostal):
#     mycursor = conbd.cursor()
#     sql = 'UPDATE pedidos SET Nome = %s, Sobrenome = %s, Endereco = %s, Cidade = %s, CodigoPostal = %s WHERE Nome = %s'
#     val = (Nome, Sobrenome, Endereco, Cidade, CodigoPostal, anterior)
#     mycursor.execute(sql,val)
#     conbd.commit()
#     print("Cliente Atualizado com Sucesso")
    
#     mycursor.close()

# def deletarPedido(conbd, Nome):
#     mycursor = conbd.cursor()
#     sql = 'DELETE FROM pedidos WHERE Nome = %s'
#     val = (Nome,)
#     mycursor.execute(sql,val)
#     conbd.commit()
#     print("Cliente Excluido com sucesso")
    
#     mycursor.close()




