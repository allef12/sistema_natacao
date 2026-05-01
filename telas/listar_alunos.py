import tkinter as tk

from database import conectar

def abrir_lista():
   
    tela = tk.Toplevel()
    tela.title("lista")
    tela.geometry("400x300")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('SELECT nome, telefone, data_nascimento FROM alunos')
