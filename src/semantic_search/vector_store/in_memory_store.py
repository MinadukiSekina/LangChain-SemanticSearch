from langchain_core.vectorstores import InMemoryVectorStore as LangchainInMemoryVectorStore

from semantic_search.llms.embedding import create_embedding_model
from semantic_search.lodaer.pdf_loader import load_pdf
from semantic_search.splitter.text_splitter import create_text_splitter


class InMemoryVectorStore:
    """ベクトルDBのインスタンスを管理するクラス"""

    _instance = None

    def __new__(cls) -> "InMemoryVectorStore":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._setup_vector_store()
        return cls._instance

    def _setup_vector_store(self) -> None:
        """ベクトルDBの初期化"""
        # ベクトルDBの初期化
        embedding = create_embedding_model()
        self._vector_store = LangchainInMemoryVectorStore(embedding=embedding)
        # ドキュメントの読み込み
        docs = load_pdf()
        # テキストの分割
        text_splitter = create_text_splitter()
        all_splits = text_splitter.split_documents(docs)
        # ドキュメントの追加
        self._vector_store.add_documents(all_splits)

    @property
    def vector_store(self) -> LangchainInMemoryVectorStore:
        """ベクトルDBのインスタンスを返す"""
        return self._vector_store


# シングルトンインスタンスを事前に作成
vector_store_instance = InMemoryVectorStore()
