
def valida_diretor(nome_completo):

    if len(nome_completo) == 0:
        return False

    return True


def valida_genero(nome):

    if len(nome) == 0:
        return False

    return True


def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):

    if len(titulo) == 0:
        return False

    elif ano == 0:
        return False

    elif int(classificacao) < 0 or int(classificacao) > 18:
        return False

    elif preco == 0:
        return False

    elif diretores_id == 0:
        return False

    elif generos_id == 0:
        return False

    return True


def valida_usuario(nome_completo, CPF):

    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True


def valida_locacao(filmes_id, usuarios_id):

    if filmes_id == 0:
        return False

    if usuarios_id == 0:
        return False

    return True


# def valida_pagamento(tipo):
#
#     if tipo == "debito":
#         return tipo[0]
#
#     elif tipo == "credito":
#         return tipo[1]
#
#     else:
#         return tipo[2]