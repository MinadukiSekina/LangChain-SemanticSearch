from langchain_community.document_loaders import PyPDFLoader

file_path = "src/semantic_search/example_data/nke-10k-2023.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

print(len(docs))

print(f"{docs[0].page_content[:200]}\n")
print(docs[0].metadata)
