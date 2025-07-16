from langchain_google_genai import GoogleGenerativeAIEmbeddings


def create_embedding_model() -> GoogleGenerativeAIEmbeddings:
    """埋め込みモデルを作成する"""
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001")
