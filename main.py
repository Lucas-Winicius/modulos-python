from flask import Flask, request, jsonify, abort
import importlib
import os

app = Flask(__name__)
MODULOS_DIR = "modulos"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE"])
def carregar_modulo(path):
    if not path:
        return jsonify({"mensagem": "API Modular Flask"}), 200

    # Convertendo a rota para o nome do módulo Python: /rota/hello → modulos.rota.hello
    partes = path.strip("/").split("/")
    if any(not parte.isidentifier() for parte in partes):
        abort(404)

    nome_modulo = ".".join([MODULOS_DIR] + partes)

    try:
        mod = importlib.import_module(nome_modulo)

        if not hasattr(mod, "handle") or not callable(mod.handle):
            abort(404)

        # Passando dados da requisição ao módulo
        return mod.handle(
            request=request,
            params=request.args.to_dict(),
            json=request.get_json(silent=True)
        )

    except ModuleNotFoundError:
        abort(404)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)