from funcoes_bd import insert, select, update, delete, select_like


# =====> Inserir Usuario <=====
def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])


# =====> Selecionar Usuario <=====
def get_usuario(id):
    return select("usuarios", "id", id)[0]


# =====> Altera Usuario <=====
def update_usuario(id, nome_completo, CPF):
    update("usuarios", "id", id, ["nome_completo", "CPF"], [nome_completo, CPF])


# =====> Seleciona Usuario por LIKE <=====
def select_usuario(nome_completo):
    return select_like("diretores", "nome_completo", nome_completo)


# =====> Deleta Usuario <=====
def delete_usuario(id):
    delete("usuarios", "id", id)