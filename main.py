#IMPORTAÇÃO DE BIBLIOTECAS
from pickle import FRAME
from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd

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

framedireita = Frame(janela, width=1050, height=300, bg=co1, relief="sunken")
framedireita.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

janela.mainloop()
