from funcoes_bd import insert, update, delete, select, select_like



def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])


def get_diretor(id):
    return select("diretores", "id", id)[0]


def insert_genero(nome):
    return insert("generos", ["nome"], [nome])


def get_genero(id):
    return select("generos", "id", id)[0]


def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


def get_filme(id):
    return select("filmes", "id", id)[0]


def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])


def get_usuario(id):
    return select("usuarios", "id", id)[0]


def update_diretor(id, nome_completo):
    return update("diretores", "id", id, ["nome_completo"], [nome_completo])


def update_genero(id, nome):
    update("generos", "id", id, ["nome"], [nome])


def update_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


def update_usuario(id, nome_completo, CPF):
    update("usuarios", "id", id, ["nome_completo", "CPF"], [nome_completo, CPF])


def delete_diretor(id):
    delete("diretores", "id", id)


def delete_genero(id):
    delete("generos", "id", id)


def delete_filme(id):
    delete("filmes", "id", id)


def delete_usuario(id):
    delete("usuarios", "id", id)


def select_diretor(nome_completo):
    return select_like("diretores", "nome_completo", f"%{nome_completo}%")


def select_genero(nome):
    return select_like("generos", "nome", f"%{nome}%")


def select_filme(titulo):
    return select_like("filmes", "titulo", f"%{titulo}%")


def select_usuario(nome_completo):
    return select_like("diretores", "nome_completo", f"%{nome_completo}%")


