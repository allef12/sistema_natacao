import tkinter as tk
from database import conectar

def salvar_aluno(nome, telefone, data_nascimento):
    conn = conectar()
    cursor = conn.cursor()
