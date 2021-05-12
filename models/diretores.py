from funcoes_bd import insert, select, update, delete, select_like


# =====> Insere diretor <=====
def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])


# =====> Seleciona Diretor <=====
def get_diretor(id):
    return select("diretores", "id", id)[0]


# =====> Altera Diretor <=====
def update_diretor(id, nome_completo):
    return update("diretores", "id", id, ["nome_completo"], [nome_completo])


# =====> Deleta Diretor <=====
def delete_diretor(id):
    delete("diretores", "id", id)


# =====> Seleciona diretor por LIKE <=====
def select_diretor(nome_completo):
    return select_like("diretores", "nome_completo", nome_completo)