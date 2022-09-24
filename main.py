#IMPORTAÇÃO DE BIBLIOTECAS

from statistics import quantiles
from pickle import FRAME
from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd
from turtle import bgcolor, left, width
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
import tkinter.font as tkFont
from view import *

#CORES

co0 = "#2e2d2b" #PRETO
co1 = "#feffff" #BRANCO
co2 = "#4fa882" #VERDE
co3 = "#38576b" #VALOR
co4 = "#403d3d" #LETRA
co5 = "#e06636" #LARANJA
co6 = "#038cfc" #AZUL
co7 = "#3fbfb9" #VERDE1
co8 = "#263738" #VERDE+
co9 = "#e9edf5" #CINZA

#CRIANDO JANELA EM BRANCO

janela = Tk()
janela.title("")
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#CRIAÇÃO DOS FRAMES

framecima = Frame(janela, width=1050, height=50, bg=co1, relief="flat")
framecima.grid(row=0, column=0)

framemeio = Frame(janela, width=1050, height=303, bg=co1, pady=20, relief="raised")
framemeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

framebaixo = Frame(janela, width=1050, height=300, bg=co1, relief="sunken")
framebaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

#CRIANDO FUNÇÕES
global tree
global imagem, imagem_string, l_imagem
#função inserir
def inserir():
    global imagem,imagem_string,l_imagem
    nome        =   e_nome.get()
    local       =  e_local.get()
    descricao   = e_descricao.get()
    modelo      = e_modelo.get()
    d_compra    = e_cal.get()
    v_compra    = e_com.get()
    serie       = e_serie.get()
    imagem      = imagem_string

    lista_inserir = [nome, local, descricao, modelo, d_compra, v_compra, serie, imagem]
    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro - ','Preencha todos os campos')
        return
    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso - ','Dados inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_modelo.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_com.delete(0, 'end')
    e_serie.delete(0, 'end')

    for widget in framemeio.winfo_children():
        widget.destroy()
    mostrar()

#função para escolher imagem

def escolher_imagem():
    global imagem, image_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170,170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label (framemeio,image=imagem, bg=co1,fg=co4)
    l_imagem.place (x=700,y=10)

#função para atualizar os dados

def atualizar():
    








#INSERIR IMAGEM - ÍCONE

app_img = Image.open('icone.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(framecima, image=app_img, text= "Controle de Estoque Doméstico", width=900, compound=LEFT, relief=RAISED, anchor=NW, font= ('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

#CRIANDO CAMPOS DE ENTRADA

l_nome = Label(framemeio, text= "Nome", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1,fg=co4)
l_nome.place(x=10,y=10)
e_nome = Entry(framemeio, width=30, justify='left', relief="solid")
e_nome.place(x=130,y=11)

l_local = Label(framemeio, text="Sala/Área", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_local.place(x=10,y=40)
e_local = Entry(framemeio, width=30, justify='left', relief="solid")
e_local.place(x=130,y=41)

l_descricao = Label(framemeio, text="Descrição", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_descricao.place(x=10,y=70)
e_descricao = Entry(framemeio, width=30, justify='left', relief="solid")
e_descricao.place(x=130,y=71)

l_modelo = Label(framemeio, text="Marca/Modelo", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_modelo.place(x=10,y=100)
e_modelo = Entry(framemeio, width=30, justify='left', relief="solid")
e_modelo.place(x=130,y=101)

l_cal = Label(framemeio, text="Data de Compra", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_cal.place(x=10,y=130)
e_cal = DateEntry(framemeio, width=12,bg='darkblue', fg='white', borderwidth=2, year=2022)
e_cal.place(x=130,y=131)

l_com = Label(framemeio, text="Valor da Compra", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_com.place(x=10,y=160)
e_com = Entry(framemeio, width=30, justify='left', relief="solid")
e_com.place(x=130,y=161)

l_serie = Label(framemeio, text="Número de Série", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_serie.place(x=10,y=190)
e_serie = Entry(framemeio, width=30, justify='left', relief="solid")
e_serie.place(x=130,y=191)

#CRIAÇÃO DE BOTÕES

l_carregar = Label(framemeio, text= "Imagem do item", height= 1, anchor=NW,font=("Ivy 10 bold"),bg= co1, fg=co4)
l_carregar.place(x=10,y=220)
botao_carregar = Button(framemeio,command= escolher_imagem,  compound=CENTER, anchor=CENTER, text= "CARREGAR".upper(), width=30, overrelief=RIDGE, font=("Ivy 8"), bg=co1, fg=co4)
botao_carregar.place(x=130,y=221)

#BOTÃO DE INSERÇÃO

img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)
botao_inserir = Button(framemeio, command=inserir, image=img_add, compound=LEFT, anchor=NW, text="Inserir".upper(), width=95, overrelief=RIDGE, font=("Ivy 8"), bg=co1, fg=co0)
botao_inserir.place(x=330,y=10)

#BOTÃO DE ATUALIZAÇÃO

img_update = Image.open('update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)
botao_update = Button(framemeio, image=img_update, compound=LEFT, anchor=NW, text="Atualizar".upper(), width=95, overrelief=RIDGE, font=("Ivy 8"), bg=co1, fg=co0)
botao_update.place(x=330,y=50)

#BOTÃO DE DELETAR

img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_delete = Button(framemeio, image=img_delete, compound=LEFT, anchor=NW, text="Deletar".upper(), width=95, overrelief=RIDGE, font=("Ivy 8"), bg=co1, fg=co0)
botao_delete.place(x=330,y=90)

#BOTÃO DE VER O ITEM

img_item = Image.open('item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)
botao_item = Button(framemeio, image=img_item, compound=LEFT, anchor=NW, text="Ver Item".upper(), width=95, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
botao_item.place(x=330,y=221)

#LABELS DE QUANTIDADE TOTAL E VALORES

l_total = Label(framemeio, width=14,height=3,anchor=CENTER,font=('Ivy 17 bold'),bg=co7,fg=co1,relief=FLAT)
l_total.place(x=450,y=15)
l_valor_total = Label(framemeio,text="Valor Total de Todos os Itens",anchor=NW,font=('Ivy 10 bold'), bg=co7, fg=co1)
l_valor_total.place(x=450,y=15)

l_qtd = Label(framemeio,width=10,height=2,anchor=CENTER,font=('Ivy 25 bold'),bg=co7,fg=co1,relief=FLAT)
l_qtd.place(x=450,y=110)
l_qtd_itens = Label(framemeio,text="Quantidade Total de Itens",anchor=NW,font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_itens.place(x=450,y=114)

#Criando TableView

def mostrar():
    tabela_head = ['Item', 'Nome', 'Sala/Área', 'Descrição', 'Marca/Modelo', 'Data da Compra', 'Valor da Compra', 'Número da Série']
    lista_itens = []

    tree = ttk.Treeview(framebaixo, selectmode="extended", columns= tabela_head, show= "headings")

    #Criando Scrollbar Vertical

    vsb = ttk.Scrollbar(framebaixo, orient="vertical", command=tree.yview)

    #Criando Scrollbar Horizontal

    hsb = ttk.Scrollbar(framebaixo, orient="horizontal", command=tree.xview)

    #Configurando a Tree

    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    framemeio.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center","center"]
    h=[40,150,100,160,130,100,100,100]

    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n+=1

    for item in lista_itens:
        tree.insert('','end', values=item)

    quantidade = []
    for item in lista_itens:
        quantidade.append(item[6])

    Total_valor = sum(quantidade)
    Total_itens = sum(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()

janela.mainloop()