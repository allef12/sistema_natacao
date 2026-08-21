import tkinter as tk
from tkinter import ttk
from database import conectar

def abrir_excluir_aluno():
    #Criar e configurar a janela
    tela = tk.Toplevel()
    tela.title("Excluir Aluno")
    tela.geometry("400x300")


    #Cria a conexão com o banco de dados
    conn = conectar()
    #cria o mensageiro, controla o fluxo com o banco
    cursor = conn.cursor()
    #Executa a ação de fazer a consulta
    cursor.execute("""SELECT id,nome
                    FROM alunos""")
    #armazena dados capturados do banco
    dados = cursor.fetchall()
    #fecha conexão com o banco
    conn.close()


    #Cria lista de aluno 
    lista_alunos = []
    #mapeia id com nome
    mapa_aluno = {}
    #Percorrendo a lista
    for aluno in dados:
        #adicionar nome e ir deixando no final da lista
        lista_alunos.append(aluno.nome)
        #associa aluno > id
        mapa_aluno[aluno.nome] = aluno.id

    #Cria rótulo de texto
    tk.Label(tela, text="Selecione o aluno").pack()
    #Cria campo de seleção, uma lista suspensa
    combo_aluno = ttk.Combobox(tela,values=lista_alunos, state="readonly")
    combo_aluno.pack()

