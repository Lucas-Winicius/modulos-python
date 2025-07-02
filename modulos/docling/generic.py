import os
import tempfile
from docling.document_converter import DocumentConverter

def _salvar_arquivo_upload(arquivo):
    temp_dir = tempfile.mkdtemp()
    caminho = os.path.join(temp_dir, arquivo.filename)
    arquivo.save(caminho)
    return caminho

def handle(request, params, json):
    source = None

    # Verifica se é um arquivo enviado
    if request.files and "file" in request.files:
        arquivo = request.files["file"]
        source = _salvar_arquivo_upload(arquivo)

    # Verifica se foi passado via JSON ou query param
    elif json and "source" in json:
        source = json["source"]
    elif "source" in params:
        source = params["source"]

    if not source:
        return {"erro": "Nenhuma fonte de documento fornecida"}, 400

    try:
        converter = DocumentConverter()
        result = converter.convert(source)
        return result.document.to_dict(), 200
    except Exception as e:
        return {"erro": str(e)}, 500
