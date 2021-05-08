from flask import Flask, jsonify, request, Response
from serializers import diretor_from_web, diretores_from_db, genero_from_web, generos_from_db, filme_from_web, \
    filmes_from_db, usuarios_from_db, usuario_from_web, titulo_filme_from_web, nome_genero_from_web, \
    nome_diretor_from_web, nome_usuario_from_web, locacao_from_web, locacoes_from_db, pagamento_from_web, \
    pagamentos_from_db
from validators import valida_diretor, valida_genero, valida_filme, valida_usuario, valida_locacao, valida_pagamento
from models import insert_diretor, insert_genero, insert_filme, insert_usuario, update_diretor, update_genero, \
    update_filme, update_usuario, delete_diretor, delete_genero, delete_filme, delete_usuario, select_diretor, \
    get_diretor, get_genero, get_filme, get_usuario, select_genero, select_filme, select_usuario, insert_locacao, \
    get_locacao, insert_pagamento, get_pagamento
from datetime import timedelta, datetime
from random import randint, choice

app = Flask(__name__)


# Criar => Diretor, Gênero, Filme, Usuário
# Criar => enviar dados como json e retornar o json do item criado

@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        id = insert_diretor(**diretor)
        diretor_inserido = get_diretor(id)
        return jsonify(diretores_from_db(diretor_inserido))
    else:
        return jsonify({"erro": "Diretor Inválido."})


@app.route("/generos", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        id = insert_genero(**genero)
        genero_inserido = get_genero(id)
        return jsonify(generos_from_db(genero_inserido))
    else:
        return jsonify({"erro": "Gênero Inválido."})


@app.route("/filmes", methods=["POST"])
def inserir_filme():
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        id = insert_filme(**filme)
        filme_inserido = get_filme(id)
        return jsonify(filmes_from_db(filme_inserido))
    else:
        return jsonify({"erro": "Filme Inválido."})


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id = insert_usuario(**usuario)
        usuario_inserido = get_usuario(id)
        return jsonify(usuarios_from_db(usuario_inserido))
    else:
        return jsonify({"erro": "Usuário Inválido."})


# Alterar => Diretor, Gênero, Filme, Usuário
# Alterar => enviar dados como json para a url que tem o id do item e retornar o json do item alterado

@app.route("/diretores/<int:id>", methods=["PUT", "PATCH"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if valida_diretor(diretor):
        update_diretor(id, **diretor)
        diretor_alterado = get_diretor(id)
        return jsonify(diretores_from_db(diretor_alterado), Response[201])
    else:
        return jsonify({"erro": "Diretor Inválido."})


@app.route("/generos/<int:id>", methods=["PUT", "PATCH"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_alterado = get_genero(id)
        return jsonify(generos_from_db(genero_alterado), Response[201])
    else:
        return jsonify({"erro": "Genêro Inválido."})


@app.route("/filmes/<int:id>", methods=["PUT", "PATCH"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        update_filme(id, **filme)
        filme_alterado = get_filme(id)
        return jsonify(filmes_from_db(filme_alterado), Response[201])
    else:
        return jsonify({"erro": "Filme Inválido."})


@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id = update_usuario(id, **usuario)
        usuario_alterado = get_usuario(id)
        return jsonify(usuarios_from_db(usuario_alterado), Response[201])
    else:
        return jsonify({"erro": "Usuário Inválido."})


# Apagar => Diretor, Gênero, Filme, Usuário
# Apagar => requisitar delete na url que tem o id do item, se tiver chave estrangeira,
# exibe uma mensagem de erro tratado

@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    try:
        delete_diretor(id)
        return None, Response[204]
    except:
        return jsonify({"erro": "É impossível apagar este diretor, devido estar conectado a outro valor."})



@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        delete_genero(id)
        return None, Response[204]
    except:
        return jsonify({"erro": "É impossível apagar este gênero, devido estar conectado a outro valor."})


@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        delete_filme(id)
        return None, Response[204]
    except:
        return jsonify({"erro": "É impossível apagar este filme, devido estar conectado a outro valor."})


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return None, Response[204]
    except:
        return jsonify({"erro": "É impossível apagar este usuário, devido estar conectado a outro valor."})


# Buscar => Diretor, Gênero, Filme, Usuário
# Buscar => Buscar por nome/titulo usando LIKE

@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    nome_completo = nome_diretor_from_web(**request.args)
    diretores = select_diretor(nome_completo)
    diretor_from_db = [diretores_from_db(diretor) for diretor in diretores]
    if len(diretores) > 0:
        return jsonify(diretor_from_db)
    else:
        return jsonify({"erro": "Diretor não encontrado."})


@app.route("/generos", methods=["GET"])
def buscar_genero():
    nome = nome_genero_from_web(**request.args)
    generos = select_genero(nome)
    genero_from_db = [generos_from_db(genero) for genero in generos]
    if len(generos) > 0:
        return jsonify(genero_from_db)
    else:
        return jsonify({"erro": "Gênero não encontrado."})


@app.route("/filmes", methods=["GET"])
def buscar_filme():
    titulo = titulo_filme_from_web(**request.args)
    filmes = select_filme(titulo)
    filme_from_db = [filmes_from_db(filme) for filme in filmes]
    if len(filmes) > 0:
        return jsonify(filme_from_db)
    else:
        return jsonify({"erro": "Filme não encontrado."})


@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuario(nome_completo)
    usuario_from_db = [usuarios_from_db(usuario) for usuario in usuarios]
    if len(usuarios) > 0:
        return jsonify(usuario_from_db)
    else:
        return jsonify({"erro": "Usuário não encontrado."})


# Locações:
# Inserir => data_inicio, data_fim, filmes_id, usuarios_id
#  Colocar a data de fim 48h depois da data de inicio (automático)

@app.route("/locacoes", methods=["POST"])
def inserir_locacao():
    locacao = locacao_from_web(**request.json)
    dia_da_locacao = datetime.now()
    prazo = timedelta(hours=48, minutes=0, seconds=0)
    prazo_final = dia_da_locacao + prazo
    if valida_locacao(**locacao):
        id = insert_locacao(dia_da_locacao, prazo_final, **locacao)
        locacao_cadastrada = get_locacao(id)
        return jsonify(locacoes_from_db(locacao_cadastrada))
    else:
        return jsonify({"erro": "Locação inválida"})


# Pagamento:
# Inserir  tipo, status, codigo_pagamento, valor, data, locacoes_id
# locacoes_id  Foreign Key ligando com Locações
#  Preencher o valor do pagamento com o valor do filme <<<<<< DÚVIDA PARA TIRAR SEGUNDA
#  Gerar um código de pagamento aleatório pra preencher no código de pagamento
#  Colocar o status aleatório

@app.route("/pagamentos", methods=["POST"])
def inserir_pagamento():
    pagamento = pagamento_from_web(**request.json)
    status_dos_pagamentos = ("aprovado", "em analise", "reprovado")
    status_atual = choice(status_dos_pagamentos)
    codigo = randint(0, 1000)
    data_pagamento = datetime.now()
    if valida_pagamento(**pagamento):
        id = insert_pagamento(status_atual, codigo, data_pagamento, **pagamento)
        pagamento_registrado = get_pagamento(id)
        return jsonify(pagamentos_from_db(pagamento_registrado))
    else:
        return jsonify({"erro": "Pagamento inválido"}) #ERRO >>> ESTÁ RETORNANDO INVALIDO OU NULO, ARRUMAR FIM DE SEMANA

# Selects de Locações:
# INNER JOIN  Listar locações pelo id do usuário
# ?  Exibir locação pelo id
# INNER JOIN  Listar locações por id do filme
# INNER JOIN  Locações devem ter, nome do usuário, nome do filme, data da locação, status do pagamento

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
