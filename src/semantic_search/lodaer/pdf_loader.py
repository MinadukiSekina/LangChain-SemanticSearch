from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf() -> list[Document]:
    """PDFを読み込む"""
    loader = PyPDFLoader("src/semantic_search/example_data/nke-10k-2023.pdf")
    return loader.load()
