# =====> Diretor requisitado da web <=====
def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
    }


# =====> Diretor pego do banco de dados <=====
def diretor_from_db(diretor):
    return {
        "id": diretor["id"],
        "nome_completo": diretor["nome_completo"],
    }


# =====> Genero requisitado da Web <=====
def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else "",
    }


# =====> Genero pego do banco de dados <=====
def genero_from_db(genero):
    return {
        "id": genero["id"],
        "nome": genero["nome"]
    }


# =====> Filme requisitado da web <=====
def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else ""
    }


# =====> Filme recebido pelo banco de dados <=====
def filme_from_db(filme):
    return {
        "id": filme["id"],
        "titulo": filme["titulo"],
        "ano": filme["ano"],
        "classificacao": filme["classificacao"],
        "preco": filme["preco"],
        "diretores_id": filme["diretores_id"],
        "generos_id": filme["generos_id"]
    }


# =====> Usuario requisitado pela web <=====
def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else "",
    }


# =====> Usuario recebido pelo banco de dados <=====
def usuario_from_db(usuario):
    return {
        "id": usuario["id"],
        "nome_completo": usuario["nome_completo"],
        "CPF": usuario["CPF"]
    }


# =====> Nome do diretor requisitado pela web <=====
def nome_diretor_from_web(**kwargs):
    return {
        kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }


# =====> Nome do genero requisitado pela web <=====
def nome_genero_from_web(**kwargs):
    return {
        kwargs["nome"] if "nome" in kwargs else ""
    }


# =====> Titulo do filme requisitado pela web <=====
def titulo_filme_from_web(**kwargs):
    return {
        kwargs["titulo"] if "titulo" in kwargs else ""
    }


# =====> Nome do usuario requisitado pela web <=====
def nome_usuario_from_web(**kwargs):
    return {
        kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }


# =====> Locação requisitada pela web <=====
def locacao_from_web(**kwargs):
    return {

        "filmes_id": kwargs ["filmes_id"] if "filmes_id" in kwargs else "",
        "usuarios_id": kwargs ["usuarios_id"] if "usuarios_id" in kwargs else ""
    }


# =====> Locação recebida pelo banco de dados <=====
def locacao_from_db(locacao):
    return {
        "id": locacao["id"],
        "data_inicio": (locacao["data_inicio"]).strftime('%d-%m-%Y %H:%M:%S'),  # =====> Formata datas
        "data_fim": (locacao["data_fim"]).strftime('%d-%m-%Y %H:%M:%S'),
        "filmes_id": locacao["filmes_id"],
        "usuarios_id": locacao["usuarios_id"]
    }


# =====> Pagamento requisitado pela web <=====
def pagamento_from_web(**kwargs):
    return {
        "tipo": kwargs["tipo"] if "tipo" in kwargs else ""
    }


# =====> Pagamento recebido pelo banco de dados <=====
def pagamento_from_db(pagamento):
    return {
        "id": pagamento["id"],
        "tipo": str(pagamento["tipo"]),
        "status": str(pagamento["status"]),
        "codigo_pagamento": str(pagamento["codigo_pagamento"]),
        "valor": str(pagamento["valor"]),
    }