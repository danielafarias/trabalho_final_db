from mysql.connector import connect

# try:
#     with connect(
#         host="localhost",
#         user="root",
#         password="root",
#         database="locadora") as connection:
#         print(connection)
# except Error as e:
#     print(e)


def execute(sql, params=None):
    with connect(host="localhost", user="root", password="root", database="locadora") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()


def query(sql, params=None):
    with connect(host="localhost", user="root", password="root", database="locadora") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()


def insert(tabela, colunas, valores):
    execute(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(['%s' for valor in valores])})", valores)


def delete(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))


def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])


# def select(tabela, chave=1, valor_chave=1, limit=100, offset=0):
#     return query(f"""SELECT * FROM {tabela} WHERE {chave} LIKE '%' LIMIT {limit} offset {offset}""", (valor_chave,))

def select(tabela, chave, valor_chave):
    return query(f"SELECT * FROM {tabela} WHERE {chave} LIKE %s", [valor_chave])
