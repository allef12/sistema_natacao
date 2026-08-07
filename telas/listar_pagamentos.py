

import tkinter as tk

from tkinter import ttk

from database import conectar

def abrir_lista_pagamentos():

    tela = tk.Toplevel()
    tela.title("Listar pagamentos")
    tela.geometry("400x400")

    meses = ["Janeiro", "Fevereiro", "Março", "Abril",
            "Maio", "Junho", "Julho", "Agosto",
            "Setembro", "Outubro", "Novembro", "Dezembro"]

    tk.Label(tela, text="Selecione o mês").pack(pady=10)

    combo_mes = ttk.Combobox(tela, values=meses, state="readonly")
    combo_mes.pack()

    frame_resultado = tk.Frame(tela)
    frame_resultado.pack(pady=10)

    def buscar_pagamentos():
        
        mes = combo_mes.get()

        for widget in frame_resultado.winfo_children():
            widget.destroy()
        
        if mes == "":
            tk.Label(tela, text="Nenhum mês foi selecionado")

            return
        
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""SELECT a.nome, p.mes, p.valor,p.status
                            FROM alunos a
                            JOIN pagamentos p ON a.id = p.aluno_id
                            WHERE p.mes = ? 
                            """,(mes,))
            
            dados = cursor.fetchall()

            if not dados:
                tk.Label(frame_resultado,
                        text="Nenhum pagamento encontrado para este mês").pack()
            
            else:
                for pagamento in dados:
                    texto = f"{pagamento.nome} | {pagamento.mes} | R${pagamento.valor} | {pagamento.status}"

                    tk.Label(frame_resultado, text=texto, anchor="w").pack(fill="x", padx=10)

            conn.close()
        
        except Exception as e:
            tk.Label(frame_resultado, text=f"Erro ao acessar banco:{e}",fg="red").pack()
    
    tk.Button(
        tela,
        text="Buscar Pagamentos",
        command=buscar_pagamentos,
        bg="#2196F3",
        fg="white"
    ).pack(pady=10)








    
   
            


        

