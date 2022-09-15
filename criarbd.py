#Importar biblioteca de conexão com o banco
import sqlite3 as lite

#Criar conexão banco
con = lite.connect('dados.db')

#Criando tabela
with con:
    cur = con.cursor
    cur.execute("CREATE TABLE INVENTARIO (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT, LOCAL TEXT, DESCRICAO TEXT, DATA_DA_COMPRA DATE, VALOR_DA_COMPRA DECIMAL, SERIE TEXT, IMAGEM TEXT)")