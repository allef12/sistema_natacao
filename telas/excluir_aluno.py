import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import conectar
    
def abrir_excluir_aluno():
    #abrir tela
    tela = tk.Tk()
    tela.title("Excluir aluno")
    tela.geometry("400x300")
    #conectar ao banco
   