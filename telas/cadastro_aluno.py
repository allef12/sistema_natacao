#importar biblioteca tkinter para criar interface gráfica
import tkinter as tk
#importa de do tkinter um módulo que exibe caixas de diálogo
from tkinter import messagebox
from datetime import datetime
#importar a função conectar que está no database.py
from database import conectar

#cria a função que salva aluno no banco de dados
def salvar_aluno(nome,telefone, data_nascimento):
   
 #Cria a infraestrutura o canal de comunicação
    try:
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
    except Exception as e:
       messagebox.showerror("Erro",f"Erro de tratamento {e}")  

   
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

    tk.Label(tela,text='Telefone').pack()

    entrada_tel = tk.Entry(tela)
    entrada_tel.pack()

    #FORMATAR TELEFONE
    def formatar_tel(event=None):
       texto2 = entrada_tel.get()

       numeros = ''.join(filter(str.isdigit, texto2))
      

       numeros = numeros[:11]

       if len(numeros) >=7:
          texto2 = ( "("+numeros[:2]+")" + numeros[2:7] + "-" + numeros[7:]
                    )
        
       elif len(numeros) >=2:
           texto2 = ("("+numeros[:2]+")" + numeros[2:])
      
       else:
           texto2 = "("+ numeros +")"
    
       entrada_tel.delete(0, tk.END)
       entrada_tel.insert(0, texto2)
    entrada_tel.bind("<KeyRelease>", formatar_tel)   

    tk.Label(tela, text='Data de nascimento').pack()

    entrada_nascimento = tk.Entry(tela)
    entrada_nascimento.pack()
    
    #------------------------------------------
    #FORMATAÇÃO DE DATA
    #---------------------------------------
    def formatar_data(event=None):
       texto = entrada_nascimento.get()

       numeros = ''.join(filter(str.isdigit, texto))
       
       numeros = numeros[:8]
       
       if len(numeros) >= 5:
           texto = (numeros[:2]
                    +"/"
                    +numeros[2:4]
                    +"/"
                    +numeros[4:])
       elif len(numeros) >= 3:
           texto = (numeros[:2]
                    +"/"
                    +numeros[2:])
       else:
           texto = numeros

        
           
       entrada_nascimento.delete(0,tk.END)
       entrada_nascimento.insert(0,texto)
    
    entrada_nascimento.bind("<KeyRelease>", formatar_data)
           
                               

    
#================================================
# Função do botão salvar
#================================================

    def clicar_salvar():
     nome = entrada_nome.get()
     telefone = entrada_tel.get()
     data_nascimento = entrada_nascimento.get()
     
     if nome == "" or telefone == "" or data_nascimento == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
                
        tela.lift()
        tela.focus_force()
                
        return

        
    #--------------------------
    # VALIDAÇÃO SOMENTE TEXTO sem outros caracteres
    #--------------------------
     nome_sem_espaço = nome.replace(" ","")
        
     if not nome_sem_espaço.isalpha():
        messagebox.showwarning("Aviso", "Digite um nome válido!")
            
        tela.lift()
        tela.focus_force()
        return
            
    #--------------------------
    #LIMITA O TAMANHO DO TEXTO
    #--------------------------
     if len(nome) <3 or len(nome) >50:
        messagebox.showwarning("Aviso","Nome deve ter entre 3 a 50 caracteres")
        tela.lift()
        tela.focus_force()
        return

    #----------------------------------------
    #Verifica se tem os 11 números
    #----------------------------------------
     numero_telefone = ''.join(filter(str.isdigit, telefone))

     if len(numero_telefone) != 11:
        messagebox.showwarning("Aviso","Telefone: digite 11 números")

        tela.lift()
        tela.focus_force()
        return

        #----------------------------------------
        # VALIDAÇÃO DE DATA E TRATAMENTO DE ERRO
        #----------------------------------------
     try:
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

     except ValueError:
        messagebox.showerror("Erro","Data: use DD/MM/AAAA")

        tela.lift()
        tela.focus_force()

        return

     salvar_aluno(nome, telefone, data_nascimento)
    
     messagebox.showinfo("Sucesso","Aluno cadastrado com sucesso!")
    
     entrada_nome.delete(0, tk.END)
     entrada_tel.delete(0, tk.END)
     entrada_nascimento.delete(0, tk.END)

     tela.lift()
     tela.focus_force()
     entrada_nome.focus_set()


    tk.Button(
    tela,
    text='Salvar',
    command=clicar_salvar
    ).pack(pady=10)










