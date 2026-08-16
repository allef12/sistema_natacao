
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
    status = ["Pago"]

    tk.Label(tela, text="Meses").pack(pady=5)
    
    combo_mes = ttk.Combobox(tela, values=meses, state="readonly")
    combo_mes.pack()
    
    tk.Label(tela, text="Valor").pack()
    
    Planos = ['150 R$','300 R$']
    
    combo_valor = ttk.Combobox(tela, values=Planos, state="readonly")
    combo_valor.pack()
    
    tk.Label(tela, text="status").pack()
    
    combo_status = ttk.Combobox(tela, values=status, state="readonly")
    combo_status.pack()
    
    def salvar_pagamento():
        nome = combo_nome.get()
        mes = combo_mes.get()
        valor = combo_valor.get()
        status = combo_status.get()
        
        if nome =="" or mes =="" or valor =="" or status =="":
            messagebox.showwarning(
                "ERRO",
                "Preencha todos os campos")
            
            return
        
        valor = valor.replace("R$","")
        valor = float(valor)

        aluno_id = mapa_alunos[nome]
        
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO pagamentos (aluno_id,mes,valor,status)VALUES(?,?,?,?)",
                       (aluno_id,mes,valor,status))
        
        conn.commit()

        conn.close()
        
        messagebox.showinfo("Sucesso","Pagamento salvo com sucesso")

    botao = tk.Button(tela, text="Salvar pagamento", command=salvar_pagamento)
    botao.pack(pady=10)
        
        
        
        
        

   
        
        
     





