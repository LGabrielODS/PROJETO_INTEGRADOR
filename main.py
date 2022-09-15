#IMPORTAÇÃO DE BIBLIOTECAS

from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd

#CORES

co0 = "#2e2d2b" #PRETO
co1 = "feffff" #BRANCO
co2 = "4fa882" #VERDE
co3 = "38576b" #VALOR
co4 = "403d3d" #LETRA
co5 = "e06636" #LARANJA
co6 = "038cfc" #AZUL
co7 = "3fbfb9" #VERDE1
co8 = "263738" #VERDE+
co9 = "#e9edf5" #CINZA

#CRIANDO JANELA EM BRANCO

janela = Tk()
janela.title("")
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

janela.mainloop()
