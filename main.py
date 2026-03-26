from database import conectar

import tkinter as tk 

janela = tk.Tk()
janela.title('Sistema de Natação')
janela.geometry('500x400')

titulo = tk.Label(janela , text='Sistema Natação Mariana', font=('Arial',20))
titulo.pack(pady=20)

botao1 = tk.Button(janela, text='Cadastrar Aluno', width=20, command=abrir_cadastro)
botao1.pack()
