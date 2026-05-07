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

    dados = cursor.fetchall()

    conn.close()

    lista_alunos = []

    mapa_alunos = {}

    for aluno in dados:
        lista_alunos.append(aluno.nome)
        mapa_alunos[aluno.nome] = aluno.id
    
    tk.Label(tela,text="Nome").pack(pady=5)
    
    combo_nome = ttk.Combobox(tela, values=lista_alunos, state="readonly")
    combo_nome.pack()
    
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro', 'novembro','dezembro']
    
    tk.Label(tela, text="Meses").pack(pady=5)
    
    combo_mes = ttk.Combobox(tela, values=meses, state="readonly")
    combo_mes.pack()
    
    tk.Label(tela, text="Valor").pack()
    
    entrada_valor = tk.Entry(tela)
    entrada_valor.pack()
    
    tk.Label(tela, text="status").pack()
    
    entrada_status = tk.Entry(tela)
    entrada_status.pack()
