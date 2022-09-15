#Importação de bibliotecas
import sqlite3 as lite
from datetime import datetime

#Criar conexão com o banco
con = lite.connect('dados.db')

#Função para inserir inventário
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO INVENTARIO (NOME, LOCAL, DESCRICAO, MARCA, DATA_DA_COMPRA, VALOR_DA_COMPRA, SERIE, IMAGEM)" \ 
                "VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query.i)

#Função para deletar um registro/linha/tupla
def deletar_form(d):
    with con:
        cur = con.cursor()
        query = "DELETE FROM INVENTARIO WHERE ID=?"
        cur.execute(query,d)

#Função para atualizar um registro/linha/tupla
def atualizar_form(a):
    with con:
        cur = con.cursor()
        query = "UPDATE INVENTARIO SET NOME=?, LOCAL=?, DESCRICAO=?, MARCA=?, DATA_DA_COMPRA=?,"\
                "VALOR_DA_COMPRA=?, SERIE=?, IMAGEM=?"
        cur.execute(query,d)

#Função para ver todos os itens
def ver_form():
    lista_itens = []
    with con:
        cur.execute("SELECT * FROM INVENTARIO ORDER BY NAME")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

#Função para ver apenas um item
def visualizar_form(v):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * INTO INVENTARIO WHERE ID=?", (id))
        rows = cur.fetchall()
        for row is rows:
            lista_itens.append(row)
    return lista_itens

