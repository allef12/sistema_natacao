
import tkinter as tk

from tkinter import ttk

from database import conectar

def abrir_inadimplentes():
    
    tela = tk.Toplevel()
    tela.title("Inadimplentes")
    tela.geometry("400x400")
    
    meses = ["Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    
    
    tk.Label(tela,text="Selecione o mês").pack(pady=10)

    combo_mes = ttk.Combobox(tela, values=meses, state="readonly")
    combo_mes.pack(pady=5)
    #Área de exibição dos resultados
    frame_resultado = tk.Frame(tela)
    frame_resultado.pack(pady=10)

    def buscar_inadimplentes():

        mes = combo_mes.get()

        for widget in frame_resultado.winfo_children():
            widget.destroy()

        if mes == "":
            tk.Label(frame_resultado,text="Selecione um mês!").pack()
            return

        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
                    SELECT nome, telefone 
                    FROM alunos 
                    WHERE id NOT IN(
                            SELECT aluno_id
                            FROM pagamentos
                            WHERE mes = ?
                            AND status = 'Pago'
                        )
                       
                        """, (mes,))
            dados = cursor.fetchall()

            #verifica se encontrou os inadimplentes

            if not dados:
                tk.Label(frame_resultado, text="Nenhum inadimplente").pack()

            else:
                for aluno in dados:
                    texto = f"{aluno.nome} - {aluno.telefone}"
                    tk.Label(frame_resultado, text=texto).pack()
                    
            conn.close()
            
        except Exception as e:   
            tk.Label(
                frame_resultado,
                text=f"Erro:{e}",
                fg="red"
            )
            
    tk.Button(
        tela,
        text="Buscar inadimplentes",
        command= buscar_inadimplentes,
        bg="#f44336",
        fg="white"
    ).pack(pady=10)




    
