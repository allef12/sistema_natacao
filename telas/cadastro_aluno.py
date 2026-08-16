#importar biblioteca tkinter para criar interface gráfica
#importa de do tkinter um módulo que exibe caixas de diálogo
from tkinter import messagebox

#importar a função conectar que está no database.py
from database import conectar

#cria a função que salva aluno no banco de dados
def salvar_aluno(nome,telefone, data_nascimento):
   
 #Cria a infraestrutura o canal de comunicação
    conn = conectar()
    #é o mensageiro, é o objeto que chama um método, leva e trás a mensagem
    cursor = conn.cursor()
    
    #Método que executa a ação que nesse caso guarda informação no banco
    cursor.execute(
       "INSERT INTO alunos(nome, telefone, data_nascimento) VALUES(?, ?, ?)",
       (nome,telefone, data_nascimento)
       )
    #Serve pra dar um ok na operação
    conn.commit()
    
    #Finaliza a conexão, liberando espaço e limitando conexões
    conn.close()

    print('Aluno cadastrado no banco')
#============================================    
#função que vai abrir a interface gráfica 
#============================================
def abrir_cadastro():
    #É um objeto que cria uma janela filha
    tela = tk.Toplevel()
    #É um método que coloca um título na janela
    tela.title('Cadastro de Aluno')
    #Método que define o tamanho da janela
    tela.geometry('300x250')
#============================================
#Método que cria um texto estatico
#=============================================
    tk.Label(tela, text='Nome do aluno').pack()

    entrada_nome = tk.Entry(tela)
    entrada_nome.pack()

    tk.Label(tela,text='telefone').pack()

    entrada_tel = tk.Entry(tela)
    entrada_tel.pack()

    tk.Label(tela, text='data de nascimento').pack()

    nasc = tk.Entry(tela)
    nasc.pack()
#================================================
# Função do botão salvar
#================================================

    def clicar_salvar():
     nome = entrada_nome.get()
     telefone = entrada_tel.get()
     data_nascimento = nasc.get()
     
     if nome == "" or telefone == "" or data_nascimento == "":
       messagebox.showwarning("Aviso", "Preencha todos os campos!")
       
       return
     
     salvar_aluno(nome, telefone, data_nascimento)


    tk.Button(
    tela,
    text='Salvar',
    command=clicar_salvar
    ).pack(pady=10)"""



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

    

    tk.Button(tela, text='Salvar', command= clicar_salvar).pack(pady=10)







