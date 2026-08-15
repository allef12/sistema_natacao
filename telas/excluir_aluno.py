# importa interface gráfica
import tkinter as tk

# importa combobox
from tkinter import ttk

# importa caixa de mensagem
from tkinter import messagebox

# importa conexão com o banco
from database import conectar


def abrir_excluir_aluno():

    # cria a janela
    tela = tk.Toplevel()
    tela.title("Excluir Aluno")
    tela.geometry("400x250")

