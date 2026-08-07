"""O @app.get("/alunos") é como uma plaquinha escrita "Sala dos Alunos".
A função alunos() é a sala.

Se existir só a placa, mas não existir a sala, para onde a pessoa vai entrar?"""

"""As chaves ({}) significam:

"Aqui eu aceito qualquer valor e vou guardar esse valor."

Sem as chaves, o FastAPI entende que a URL tem que ser exatamente igual.

Pensa numa porta com um endereço.

Se a porta está marcada:

/alunos

Só entra quem bater exatamente em:

/alunos

Se alguém bater em:

/alunos/42

É outra porta.

Agora, se a porta está marcada:

/alunos/{id}

Ela diz:

"Depois de /alunos/, pode vir qualquer valor."""
from fastapi import FastAPI

app = FastAPI() # quando alguém acessa, o app recebe a requisição

@app.get("/") # registra uma rota para requisições GET (buscar informações).
def inicio(): #associa a função a rota
    return{"mensagem":"API funcionando carai"}


@app.get("/alunos/{id}")
def buscar_aluno(id):
    return{"ok":id}