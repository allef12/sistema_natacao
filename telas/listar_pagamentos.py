import tkinter as tk

from tkinter import ttk

from database import conectar

def abrir_lista_pagamentos():

    tela = tk.Toplevel()
    tela.title("Listar pagamentos")
    tela.geometry("400x400")
