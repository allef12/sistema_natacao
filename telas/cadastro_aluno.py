import tkinter as tk
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
