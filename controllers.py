# ==> Import Flask
from flask import Flask, jsonify, request
# ==> Import Serializers
from serializers import diretor_from_web, diretor_from_db, genero_from_web, genero_from_db, filme_from_web, \
    filme_from_db, usuario_from_db, usuario_from_web, titulo_filme_from_web, nome_genero_from_web, \
    nome_diretor_from_web, nome_usuario_from_web, locacao_from_web, locacao_from_db, pagamento_from_db
# ==> Import Validators
from validators import valida_diretor, valida_genero, valida_filme, valida_usuario, valida_locacao
# ==> Import Models
from models import insert_diretor, insert_genero, insert_filme, insert_usuario, update_diretor, update_genero, \
    update_filme, update_usuario, delete_diretor, delete_genero, delete_filme, delete_usuario, select_diretor, \
    get_diretor, get_genero, get_filme, get_usuario, select_genero, select_filme, select_usuario, insert_locacao, \
    get_locacao, insert_pagamento, get_preco, get_locacoes_filmes_id, return_locacao, return_pagamento, \
    select_locacao
# ==> Import Datetime
from datetime import timedelta, datetime
# ==> Import Random
from random import randint, choice


app = Flask(__name__)

# =====> POST <=====
# Criar ==> Diretor, Gênero, Filme, Usuário
# Criar ==> enviar dados como json e retornar o json do item criado

@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        id = insert_diretor(**diretor)
        diretor_inserido = get_diretor(id)
        return jsonify(diretor_from_db(diretor_inserido))
    else:
        return jsonify({"erro": "Diretor Inválido."})


@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        id = insert_genero(**genero)
        genero_inserido = get_genero(id)
        return jsonify(genero_from_db(genero_inserido))
    else:
        return jsonify({"erro": "Gênero Inválido."})


@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        id = insert_filme(**filme)
        filme_inserido = get_filme(id)
        return jsonify(filme_from_db(filme_inserido))
    else:
        return jsonify({"erro": "Filme Inválido."})


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id = insert_usuario(**usuario)
        usuario_inserido = get_usuario(id)
        return jsonify(usuario_from_db(usuario_inserido))
    else:
        return jsonify({"erro": "Usuário Inválido."})


# =====> PUT / PATCH <=====
# Alterar ==> Diretor, Gênero, Filme, Usuário
# Alterar ==> enviar dados como json para a url que tem o id do item e retornar o json do item alterado

@app.route("/diretores/<int:id>", methods=["PUT", "PATCH"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if valida_diretor(diretor):
        update_diretor(id, **diretor)
        diretor_alterado = get_diretor(id)
        return jsonify(diretor_from_db(diretor_alterado))
    else:
        return jsonify({"erro": "Diretor Inválido."})


@app.route("/generos/<int:id>", methods=["PUT", "PATCH"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_alterado = get_genero(id)
        return jsonify(genero_from_db(genero_alterado))
    else:
        return jsonify({"erro": "Genêro Inválido."})


@app.route("/filmes/<int:id>", methods=["PUT", "PATCH"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        update_filme(id, **filme)
        filme_alterado = get_filme(id)
        return jsonify(filme_from_db(filme_alterado))
    else:
        return jsonify({"erro": "Filme Inválido."})


@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id = update_usuario(id, **usuario)
        usuario_alterado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_alterado))
    else:
        return jsonify({"erro": "Usuário Inválido."})


# =====> DELETE <=====
# Apagar => Diretor, Gênero, Filme, Usuário
# Apagar => requisitar delete na url que tem o id do item, se tiver chave estrangeira, exibe uma mensagem de erro

@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    try:
        delete_diretor(id)
        return ('', 204)
    except:
        return jsonify({"erro": "É impossível apagar este diretor, devido estar conectado a outro valor."})


@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        delete_genero(id)
        return ('', 204)
    except:
        return jsonify({"erro": "É impossível apagar este gênero, devido estar conectado a outro valor."})


@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        delete_filme(id)
        return ('', 204)
    except:
        return jsonify({"erro": "É impossível apagar este filme, devido estar conectado a outro valor."})


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return ('', 204)
    except:
        return jsonify({"erro": "É impossível apagar este usuário, devido estar conectado a outro valor."})


# =====> GET <=====
# Buscar => Diretor, Gênero, Filme, Usuário
# Buscar => Buscar por nome/titulo usando LIKE

@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    nome_completo = nome_diretor_from_web(**request.args)
    diretores = select_diretor(nome_completo)
    diretores_from_db = diretor_from_db(diretores)
    if len(diretores) > 0:
        return jsonify(diretores_from_db)
    else:
        return jsonify({"erro": "Diretor não encontrado."})


@app.route("/generos", methods=["GET"])
def buscar_genero():
    nome = nome_genero_from_web(**request.args)
    generos = select_genero(nome)
    generos_from_db = [genero_from_db(genero) for genero in generos]
    if len(generos) > 0:
        return jsonify(generos_from_db)
    else:
        return jsonify({"erro": "Gênero não encontrado."})


@app.route("/filmes", methods=["GET"])
def buscar_filme():
    titulo = titulo_filme_from_web(**request.args)
    filmes = select_filme(titulo,)
    filmes_from_db = [filme_from_db(filme) for filme in filmes]
    if len(filmes) > 0:
        return jsonify(filmes_from_db,)
    else:
        return jsonify({"erro": "Filme não encontrado."})


@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuario(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    if len(usuarios) > 0:
        return jsonify(usuarios_from_db)
    else:
        return jsonify({"erro": "Usuário não encontrado."})


# ====> LOCAÇÕES: <====
# Inserir => data_inicio, data_fim, filmes_id, usuarios_id
# data_fim => prazo 48h (automático)

# ====> Pagamento deve ser feito junto, no mesmo endpoint

# ====> PAGAMENTOS: <====
# Inserir => tipo, status, codigo_pagamento, valor, data, locacoes_id
# locacoes_id => Foreign Key ligando com Locações
# valor => preco de filmes
# codigo_pagamento => aleatorio
# status => aleatorio


@app.route("/locacoes", methods=["POST"])
def inserir_locacao():
    locacao = locacao_from_web(**request.json)
    status_dos_pagamentos = ("aprovado", "em analise", "reprovado")
    tipos_de_pagamentos = ("debito", "credito", "paypal") # PRETENDO RETIRAR O MODO AUTOMATICO DO TIPO DE PAGAMENTO
    status_atual = choice(status_dos_pagamentos)
    tipo_atual = choice(tipos_de_pagamentos)
    codigo = randint(1000, 2000)
    dia_da_locacao = datetime.now()
    prazo = timedelta(hours=48, minutes=0, seconds=0)
    prazo_final = dia_da_locacao + prazo
    if valida_locacao(**locacao):
        id1 = insert_locacao(dia_da_locacao, prazo_final, **locacao)
        id_filme = get_locacoes_filmes_id(id1)
        valor_filme = get_preco(id_filme)
        locacao_id = get_locacao(id1)
        id2 = insert_pagamento(tipo_atual, status_atual, codigo, valor_filme, dia_da_locacao, locacao_id)
        locacao_inserido = return_locacao(id1)
        pagamento_inserido = return_pagamento(id2)
        return jsonify(locacao_from_db(locacao_inserido), pagamento_from_db(pagamento_inserido))
    else:
        return jsonify({"erro": "Locação inválida."})


# ====> GET DE LOCAÇÕES: <====
# => Locações devem ter, nome do usuário, nome do filme, data da locação, status do pagamento


# => Exibir locação pelo id [Exibindo: nome do usuário, nome do filme, data da locação, status do pagamento]
@app.route("/locacoes/<int:id>", methods=["GET"])
def buscar_locacao(id):
    try:
        return select_locacao(id)
    except:
        return jsonify({"erro": "Locação não encontrada."})


# => Listar locações pelo id do usuário


# => Listar locações por id do filme


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
