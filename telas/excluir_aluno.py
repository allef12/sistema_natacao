import tkinter as tk
from tkinter import ttk
from database import conectar
from tkinter import messagebox

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

    def excluir():
      nome = combo_aluno.get()
    
      if nome =="":
          messagebox.showwarning("Aviso","Coloque o nome do aluno")
          
          tela.lift()
                        #coloca o foco na janela
          tela.focus_force()
          return
      
      
      aluno_id = mapa_aluno[nome]

      confirmar = messagebox.askyesno("Confirmar exclusão", f"Deseja excluir o aluno\n\n {nome}?")
      
      if not confirmar:
          tela.lift()
                        #coloca o foco na janela
          tela.focus_force()
          return
     
      try: 
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
                        DELETE FROM alunos
                        WHERE id = ?""", (aluno_id,)) 

        conn.commit()  

        conn.close()
        
        messagebox.showinfo("Sucesso","Aluno excluido com sucesso!")
        #Depois da exclusão limpa o combobox  
        combo_aluno.set("")
        #trazer janela pra frente 
        tela.lift()
        #coloca o foco na janela
        tela.focus_force()
    
      except Exception as e:
        messagebox.showerror("Erro",f"Não foi possível excluir o aluno:\n\n{e}")
    
    #Botão de exclusão
    tk.Button(tela,text="Excluir",command=excluir).pack(pady=10)
            