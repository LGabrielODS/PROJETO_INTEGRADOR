#IMPORTAÇÃO DE BIBLIOTECAS

from pickle import FRAME
from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd
from turtle import bgcolor
from PIL import Image, ImageTk
from tkcalendar import Calendar

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
l_local = Entry(framemeio, width=30, justify='left', relief="solid")
l_local.place(x=130,y=41)

l_descricao = Label(framemeio, text="Descrição", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_descricao.place(x=10,y=70)
l_descricao = Entry(framemeio, width=30, justify='left', relief="solid")
l_descricao.place(x=130,y=71)

l_modelo = Label(framemeio, text="Marca/Modelo", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_modelo.place(x=10,y=100)
l_modelo = Entry(framemeio, width=30, justify='left', relief="solid")
l_modelo.place(x=130,y=101)

l_cal = Label(framemeio, text="Data de Compra", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_cal.place(x=10,y=130)
l_cal = DateEntry(framemeio, width=30,bg='darkblue', fg='white', borderwidth=2, year=2020)
l_cal.place(x=130,y=131)

l_com = Label(framemeio, text="Valor da Compra", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_com.place(x=10,y=160)
l_com = Entry(framemeio, width=30, justify='left', relief="solid")
l_com.place(x=130,y=161)

l_serie = Label(framemeio, text="Número de Série", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_serie.place(x=10,y=190)
l_serie = Entry(framemeio, width=30, justify='left', relief="solid")
l_serie.place(x=130,y=191)

l_imagem = Label(framemeio, text="Imagem", height= 1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_imagem.place(x=10,y=220)
l_imagem = Entry(framemeio, width=30, justify='left', relief="solid")
l_imagem.place(x=130,y=221)


janela.mainloop()