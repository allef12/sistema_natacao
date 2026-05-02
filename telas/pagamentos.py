import tkinter as tk

from tkinter import ttk

from database import conectar

from tkinter import messagebox


def abrir_pagamentos():
    
    tela = tk.Toplevel()
    tela.title("Pagamentos")
    tela.geometry("400x400")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM alunos")
