from mysql.connector import connect


# =====> Função de Execute <=====
def execute(sql, params=None):
    with connect(host="localhost", user="root", password="root", database="locadora") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid


# =====> Função de Query <=====
def query(sql, params=None):
    with connect(host="localhost", user="root", password="root", database="locadora") as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()


# =====> Função de Inserir <=====
def insert(tabela, colunas, valores):
    return execute(f"""INSERT INTO {tabela} ({','.join(colunas)}) 
    VALUES ({','.join(['%s' for valor in valores])})""", valores)


# =====> Função de Deletar <=====
def delete(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))


# =====> Função de Alterar <=====
def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])


# =====> Função de Selecionar <=====
def select(tabela, chave, valor_chave):
    return query(f"SELECT * FROM {tabela} WHERE {chave} = %s", (valor_chave,))


# =====> Função de Selecionar com LIKE <=====
def select_like(tabela, chave, valor_chave):
    return query(f"""SELECT * FROM {tabela} WHERE {chave} LIKE %s""", (f"%{valor_chave}%",))


# =====> Função de Selecionar com ID de padrão <=====
def select_id(tabela, chave, valor_chave):
    return query(f"SELECT id FROM {tabela} WHERE {chave} = %s", (valor_chave,))


# =====> Função de Selecionar que pede colunas <=====
def select_column(coluna, tabela, chave, valor_chave):
    return query(f"SELECT {coluna} FROM {tabela} WHERE {chave} = %s", (valor_chave,))
