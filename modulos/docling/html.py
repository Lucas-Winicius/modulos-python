from docling.document_converter import DocumentConverter

def handle(request, params, json):
    source = params.get("source") or (json and json.get("source"))
    if not source or not source.startswith("http"):
        return {"erro": "URL HTML inválida ou ausente"}, 400

    try:
        converter = DocumentConverter()
        result = converter.convert(source)
        return result.document.export_to_doctags(), 200
    except Exception as e:
        return {"erro": str(e)}, 500
