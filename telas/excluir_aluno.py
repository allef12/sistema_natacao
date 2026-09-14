import tkinter as tk
from tkinter import ttk
from database import conectar
from tkinter import messagebox


def abrir_excluir_aluno():

    # Criar e configurar a janela
    tela = tk.Toplevel()
    tela.title("Excluir Aluno")
    tela.geometry("400x300")

    # Cria lista de alunos
    lista_alunos = []

    # Mapeia nome do aluno -> id
    mapa_aluno = {}

    # Cria rótulo de texto
    tk.Label(tela, text="Selecione o aluno").pack()

    # Cria campo de seleção
    combo_aluno = ttk.Combobox(
        tela,
        values=lista_alunos,
        state="readonly"
    )
    combo_aluno.pack()

    def excluir():

        nome = combo_aluno.get()

        if nome == "":
            messagebox.showwarning(
                "Aviso",
                "Coloque o nome do aluno"
            )

            tela.lift()
            tela.focus_force()
            return

        aluno_id = mapa_aluno[nome]

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Deseja excluir o aluno\n\n{nome}?"
        )

        if not confirmar:
            tela.lift()
            tela.focus_force()
            return

        try:

            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM alunos
                WHERE id = ?
            """, (aluno_id,))

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Sucesso",
                "Aluno excluído com sucesso!"
            )

            # Atualiza a lista do Combobox
            carregar_alunos()

            # Limpa a seleção
            combo_aluno.set("")

            # Traz a janela para frente
            tela.lift()

            # Coloca o foco na janela
            tela.focus_force()

        except Exception as e:

            messagebox.showerror(
                "Erro",
                f"Não foi possível excluir o aluno:\n\n{e}"
            )

    # Botão de exclusão
    tk.Button(
        tela,
        text="Excluir",
        command=excluir
    ).pack(pady=10)

