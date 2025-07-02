from docling.document_converter import DocumentConverter

def handle(request, params, json):
    source = params.get("source") or (json and json.get("source"))
    if not source:
        return {"erro": "Fonte do documento não especificada (use ?source=url_ou_caminho)"}, 400

    try:
        converter = DocumentConverter()
        result = converter.convert(source)
        return result.document.export_to_doctags(), 200
    except Exception as e:
        return {"erro": str(e)}, 500
