"""# importa interface gráfica
import tkinter as tk

# importa combobox
from tkinter import ttk

# importa conexão com banco
from database import conectar


def abrir_inadimplentes():

    # cria nova janela
    tela = tk.Toplevel()
    tela.title("Inadimplentes")
    tela.geometry("400x400")

    # lista de meses
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    # texto
    tk.Label(tela, text="Selecione o mês").pack(pady=5)

    # combobox
    combo_mes = ttk.Combobox(tela, values=meses, state="readonly")
    combo_mes.pack()

    # área de resultados
    frame_resultado = tk.Frame(tela)
    frame_resultado.pack(pady=10, fill="both", expand=True)


    def buscar_inadimplentes():

        # pega o mês selecionado
        mes = combo_mes.get()

        # limpa tela
        for widget in frame_resultado.winfo_children():
            widget.destroy()

        # validação
        if mes == "":
            tk.Label(frame_resultado, text="Selecione um mês!", fg="red").pack()
            return

        try:
            # conecta no banco
            conn = conectar()
            cursor = conn.cursor()

            # consulta: alunos que NÃO pagaram naquele mês
            cursor.execute(""
                            SELECT nome, telefone
                            FROM alunos
                            WHERE id NOT IN (
                                SELECT aluno_id
                                FROM pagamentos
                                WHERE mes = ?
                                AND status = 'Pago'
                            )
                            AND id IN (
                                SELECT aluno_id
                                FROM pagamentos
                                WHERE mes = ?
                            )
                        "", (mes, mes))

            dados = cursor.fetchall()

            # se não houver inadimplentes
            if not dados:
                tk.Label(frame_resultado, text="Nenhum inadimplente 🎉").pack()
            else:
                # mostrar alunos
                for aluno in dados:
                    texto = f"{aluno.nome} - {aluno.telefone}"
                    tk.Label(frame_resultado, text=texto, anchor="w").pack(fill="x", padx=10)

            conn.close()

        except Exception as e:
            tk.Label(frame_resultado, text=f"Erro: {e}", fg="red").pack()


    # botão buscar
    tk.Button(
        tela,
        text="Buscar Inadimplentes",
        command=buscar_inadimplentes,
        bg="#f44336",
        fg="white"
    ).pack(pady=10)"""
    
    


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




    
