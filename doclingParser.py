from docling.document_converter import DocumentConverter

source = "https://winicus.xyz"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source, headers='')
print(result.document.export_to_markdown())  # output: ## Docling Technical Report[...]
