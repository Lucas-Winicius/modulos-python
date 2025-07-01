from flask import jsonify

def handle(request, params, json):
    return jsonify({
        "status": "ok",
        "query": params,
        "json_recebido": json
    })
