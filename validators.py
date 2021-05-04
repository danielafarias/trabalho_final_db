# from models import get_diretor


def valida_diretor(nome_completo):

    if len(nome_completo) == 0:
        return False

    # diretor = get_diretor(nome_completo)
    # if len(diretor) != 0:
    #     return False

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

    if len(CPF) == 0 or len(CPF) > 14:
        return False
    return True


def valida_id(id):

    if id == 0:
        return False

    return True