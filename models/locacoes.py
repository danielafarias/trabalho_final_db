from funcoes_bd import execute, query, select_column, select


# =====> Insere locação <=====
def insert_locacao(data_inicio, data_fim, filmes_id, usuarios_id):
    return execute(f"""INSERT INTO locacoes (data_inicio, data_fim, filmes_id, usuarios_id)
                    VALUES (%s, %s, %s, %s)""",
                   (data_inicio, data_fim, filmes_id, usuarios_id))


# =====> Seleciona os ID dos filmes na tabela de Locações <=====
def get_locacoes_filmes_id(id):
    return select_column("filmes_id", "locacoes", "id", id)[0]["filmes_id"]


# =====> Seleciona ID de locações <=====
def get_locacao(id):
    return select("locacoes", "id", id)[0]["id"]


# =====> Seleciona ID de locações sem especificar coluna de retorno <=====
def return_locacao(id):
    return select("locacoes", "id", id)[0]


# =====> Seleciona nome de usuario, titulo de filmes, data de pagamento com JOIN em locações <=====
def select_locacao(id):
    return query(f"""SELECT nome_completo, titulo, DATE_FORMAT(data, '%d-%m-%Y %H:%i:%S'), status FROM locacoes AS l
                    INNER JOIN usuarios AS u ON l.usuarios_id = u.id
                    INNER JOIN filmes AS f ON l.filmes_id = f.id
                    INNER JOIN pagamentos AS p ON l.id = p.locacoes_id
                    WHERE l.id = %s""", (id,))[0]
