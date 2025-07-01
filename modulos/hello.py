from flask import jsonify

def handle(request, params, json):
    nome = params.get("nome", "mundo")
    return jsonify({
        "mensagem": f"Olá, {nome}!",
        "metodo": request.method,
        "body": json
    })
