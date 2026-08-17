import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import conectar
    
def abrir_excluir_aluno():
    #abrir tela
    tela = tk.Tk()
    tela.title("Excluir aluno")
    tela.geometry("400x300")
    #conectar ao banco
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""SELECT id, nome FROM alunos""")
    
    dados = cursor.fetchall()
    #Teste merge
    
    conn.close()

    lista_nomes = []

    mapa_alunos = {}
    
    for aluno in dados:
        lista_nomes.append(aluno.nome)
        mapa_alunos[aluno.nome] = aluno.id

    tk.Label(tela, text="Selecione o aluno").pack()

    combo_aluno = ttk.Combobox(tela, values=lista_nomes, state="readonly")
    combo_aluno.pack()
    #---------------------
    # FUNÇÃO QUE EXCLUI ALUNOS
    #---------------------
    
    def excluir():
        nome = combo_aluno.get()
        
        if nome == "":
            messagebox.showwarning("Aviso","Selecione um aluno.")
        
        aluno_id = mapa_alunos[nome]
        
        confirmar = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir o aluno:\n\n {nome}?")
        
        if not confirmar:
            return
        
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
                       DELETE FROM alunos
                       WHERE id = ?"""(aluno_id,))

        conn.commit()               

        conn.close()

        messagebox.showinfo("Sucesso","Cliente excluido com sucesso")
        
        #limpa os campos
        combo_aluno.set("")
        #Traz a janela pra frente
        tela.lift()
        #coloca o foco nessa janela
        tela.focus_force()

    
    botao = tk.Button(tela,text="excluir",command=excluir)
    botao.pack()
                
            
            
            
     
    
    

            

        


   

    
    
    
        