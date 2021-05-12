from funcoes_bd import insert, select, update, delete, query


# =====> Insere Filme <=====
def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


# =====> Seleciona Filme <=====
def get_filme(id):
    return select("filmes", "id", id)[0]


# =====> Altera Filme <=====
def update_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


# =====> Deleta Filme <=====
def delete_filme(id):
    delete("filmes", "id", id)


# =====> Seleciona filme por LIKE retornando titulo, nome do genero, nome do diretor <=====
def select_filme(titulo):
    return query(f"""SELECT filme.titulo, genero.nome, diretor.nome_completo FROM filmes AS filme 
                    INNER JOIN generos AS genero ON filme.generos_id = genero.id
                    INNER JOIN diretores AS diretor ON filme.diretores_id = diretores.id 
                    WHERE titulo LIKE %s""", (f"%{titulo}%",))[0]
