import tkinter as tk
from tkinter import messagebox
from database import conectar

def salvar_aluno(nome, telefone, data_nascimento):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO alunos(nome, telefone, data_nascimento) VALUES(?, ?, ?)',
                   (nome, telefone, data_nascimento))    
    
    conn.commit()

    conn.close()

def abrir_cadastro():
    
    tela = tk.Toplevel()    
    tela.title('Cadastro do Aluno')
    tela.geometry('400x300')

    tk.Label(tela, text='Nome do Aluno').pack(pady=10)

    entrada_nome = tk.Entry(tela)
    entrada_nome.pack()

    tk.Label(tela, text='Telefone').pack(pady=10)

    entrada_tel = tk.Entry(tela)
    entrada_tel.pack()

    tk.Label(tela, text='Data de nascimento').pack(pady=10)

    entrada_nasc = tk.Entry(tela)
    entrada_nasc.pack()

    def clicar_salvar():

        nome = entrada_nome.get()
        telefone = entrada_tel.get()
        data_nascimento = entrada_nasc.get()

        if nome == "" or telefone == "" or data_nascimento == "":
            messagebox.showwarning('Aviso','Preencha todos os campos')

            return

        salvar_aluno(nome, telefone, data_nascimento)

        messagebox.showinfo('Sucesso', 'Aluno cadastrado com sucesso!')

        entrada_nome.delete(0, tk.END)
        entrada_tel.delete(0, tk.END)
        entrada_nasc.delete(0, tk.END)

        entrada_nome.focus_set()
