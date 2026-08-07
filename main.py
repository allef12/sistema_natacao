"""import tkinter as tk
from telas.listar_alunos import abrir_lista
from telas.cadastro_aluno import abrir_cadastro
from telas.pagamentos import abrir_pagamentos
from telas.listar_pagamentos import abrir_lista_pagamentos

janela = tk.Tk()
janela.title("Sistema de Natação")
janela.geometry("700x600")

titulo = tk.Label(
    janela,
    text="Sistema de Gestão de Alunos",
    font=("Arial",16)
)

titulo.pack(pady=20)

botao1 = tk.Button(
    janela,
    text="Cadastrar Aluno",
    width=20,
    command=abrir_cadastro
)

botao1.pack(pady=10)

botao2 = tk.Button(
    janela,
    text="Pagamentos",
    width=20,
    command=abrir_pagamentos
)

botao2.pack(pady=10)

botao3 = tk.Button(
    janela,
    text="Inadimplentes",
    width=20
)

botao3.pack(pady=10)

botao4 = tk.Button(
    janela,
    text="Ver Alunos",
    width=20,
    command=abrir_lista
)

botao4.pack(pady=10)

botao5 = tk.Button(
    janela,
    text="Ver Pagamentos",
    width=20,
    command=abrir_lista_pagamentos
) 

botao5.pack(pady=10)

janela.mainloop()"""


from database import conectar

import tkinter as tk 

from telas.cadastro_aluno import abrir_cadastro
from telas.pagamentos import abrir_pagamentos
from telas.listar_alunos import abrir_lista
from telas.listar_pagamentos import abrir_lista_pagamentos
from telas.inadimplentes import abrir_inadimplentes
from telas.editar_aluno import abrir_editar_alunos


janela = tk.Tk()
janela.title('Sistema de Natação')
janela.geometry('500x400')

titulo = tk.Label(janela , text='Sistema Natação Mariana', font=('Arial',20))
titulo.pack(pady=20)

botao1 = tk.Button(janela, text='Cadastrar Aluno', width=20, command=abrir_cadastro)
botao1.pack(pady=10)

botao2 = tk.Button(janela,text='Fazer pagamento',width=20,command=abrir_pagamentos )
botao2.pack(pady=10)

botao3 = tk.Button(janela,text='listar alunos', width=20, command=abrir_lista)
botao3.pack(pady=10)

botao4 = tk.Button(janela,text='listar pagamentos', width=20,command=abrir_lista_pagamentos)
botao4.pack(pady=10)

botao5 = tk.Button(janela,text='listar inadimplentes', width=20,command=abrir_inadimplentes)
botao5.pack(pady=10)

botao6 = tk.Button(janela, text="Editar aluno",width=20,command=abrir_editar_alunos)
botao6.pack(pady=10)






janela.mainloop()




