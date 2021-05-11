from funcoes_bd import insert, update, delete, select, select_like, query, select_id


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
    return query(f"""SELECT filme.titulo, genero.nome, diretor.nome_completo FROM filmes AS filme 
                    INNER JOIN generos AS genero ON filme.generos_id = genero.id
                    INNER JOIN diretores AS diretor ON filme.diretores_id = diretores.id 
                    WHERE titulo LIKE %s""", (titulo,))[0]


def select_usuario(nome_completo):
    return select_like("diretores", "nome_completo", f"%{nome_completo}%")


# def insert_locacao(valores):
#     return execute(f"""INSERT INTO locacoes (data_inicio, data_fim, filmes_id, usuarios_id)
#                     VALUES ({','.join(['%s' for valor in valores])})""", (valores,))


# def insert_pagamento(valores):
#     return execute(f"""INSERT INTO pagamentos (tipo, status, codigo_pagamento, valor, data, locacoes_id)
#                     VALUES ({','.join(['%s' for valor in valores])})""", valores)


def insert_locacao(data_inicio, data_fim, filmes_id, usuarios_id):
    return insert("locacoes", ["data_inicio", "data_fim", "filmes_id", "usuarios_id"],
                  [data_inicio, data_fim, filmes_id, usuarios_id])


def insert_pagamento(tipo, status, codigo_pagamento, valor, data, locacoes_id):
    return insert("pagamentos", ["tipo", "status", "codigo_pagamento", "valor", "data", "locacoes_id"],
                  [tipo, status, codigo_pagamento, valor, data, locacoes_id])


def get_preco():
    return query("""SELECT preco FROM filmes INNER JOIN locacoes ON filmes.id = locacoes.filmes_id""")


def get_locacao_id(id):
    return select_id("locacoes", "id", id)
#
#
# def get_preco():
#     return select_column("preco", "filmes", "locacoes", "id", "id")[0]
#
#

#
#
# def get_pagamento(id):
#     return select("pagamentos", "id", id)
#
#
def get_locacao(id1, id2):
    return query(f"""SELECT locacoes.id, pagamentos.id FROM locacoes 
                INNER JOIN pagamentos ON locacoes.id = pagamentos.locacoes_id
                WHERE locacoes.%s = pagamentos.%s""", (id1, id2))[0]