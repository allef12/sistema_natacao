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
def abrir_editar_alunos():
    
    tela = tk.Toplevel()
    tela.title("Editar aluno")
    tela.geometry("350x400")

    #-----
    #conectar ao banco
    #-----

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM alunos")
    #variável que puxa informações de id e nome
    dados = cursor.fetchall()

    conn.close()

    #-----
    #listas
    #-----

    lista_nome = []

    mapa_alunos = {}

    for aluno in dados:
        lista_nome.append(aluno.nome)
        mapa_alunos[aluno.nome] = aluno.id

    #---
    #Selecionar aluno
    #--

    tk.Label(tela, text="Aluno").pack(pady=5)

    combo_aluno = ttk.Combobox(tela, values=lista_nome, state="readonly")
    combo_aluno.pack()

    #---
    #campos
    #---

    tk.Label(tela, text="Nome").pack()

    entrada_nome = tk.Entry(tela)
    entrada_nome.pack()

    tk.Label(tela, text="Telefone").pack()

    entrada_tel = tk.Entry(tela)
    entrada_tel.pack()

    tk.Label(tela,text="Data de nascimento").pack()

    entrada_nascimento = tk.Entry(tela)
    entrada_nascimento.pack()

    #---
    #carregar dados
    #---

    def carregar_dados():
        nome = combo_aluno.get()

        if nome =="":
            messagebox.showwarning("Aviso","Preencha o campo")
        
        aluno_id = mapa_alunos[nome] 

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""SELECT nome,telefone,data_nascimento
                          FROM alunos
                          WHERE id = ?""",(aluno_id,))
        
        aluno = cursor.fetchone()

        conn.close()

    #LIMPA OS CAMPOS

    entrada_nome.delete(0,tk.END)
    entrada_tel.delete(0,tk.END)
    entrada_nascimento.delete(0,tk.END)

    


   






        



    





       









       




   


   
   
   

