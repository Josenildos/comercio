from mysql.connector import connect

def conexao():
    conbd = connect(
        host='localhost',
        user='root',
        password='',
        database='comercioj'
        )
    return conbd


