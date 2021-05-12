from funcoes_bd import execute, select, select_column


def insert_pagamento(tipo, status, codigo_pagamento, valor, data, locacoes_id):
    return execute(f"""INSERT INTO pagamentos (tipo, status, codigo_pagamento, valor, data, locacoes_id)
                    VALUES ('%s', %s, %s, %s, %s, %s)""",
                   (tipo, status, codigo_pagamento, valor, data, locacoes_id))


def get_preco(id):
    return select_column("preco", "filmes", "id", id)[0]["preco"]


def get_pagamento(id):
    return select("pagamentos", "id", id)[0]["id"]


def return_pagamento(id):
    return select("pagamentos", "id", id)[0]

