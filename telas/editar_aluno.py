# importa interface gráfica
import tkinter as tk

# importa combobox
from tkinter import ttk

# importa caixa de mensagem
from tkinter import messagebox

# importa conexão com banco
from database import conectar


#-------
#Janelas
#-------

tela = tk.Toplevel()
tela.title("Editar aluno")
tela.geometry("350x400")
