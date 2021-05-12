from funcoes_bd import insert, select, update, delete, select_like


# =====> Insere Genero <=====
def insert_genero(nome):
    return insert("generos", ["nome"], [nome])


# =====> Seleciona Genero <=====
def get_genero(id):
    return select("generos", "id", id)[0]


# =====> Altera Genero <=====
def update_genero(id, nome):
    update("generos", "id", id, ["nome"], [nome])


# =====> Deleta Genero <=====
def delete_genero(id):
    delete("generos", "id", id)


# =====> Seleciona genero por LIKE <=====
def select_genero(nome):
    return select_like("generos", "nome", nome)
