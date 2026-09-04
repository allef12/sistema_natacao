import pyodbc

def conectar():

    conexao = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=TI\\SQLEXPRESS;"
        "DATABASE=Natacao;"
        "Trusted_Connection=yes;"
    )

    return conexao
print('CONECTADO AO BANCO!')

