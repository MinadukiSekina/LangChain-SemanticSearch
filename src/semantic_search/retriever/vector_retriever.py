from typing import Annotated

from fastapi.params import Depends
from langchain_core.vectorstores import VectorStoreRetriever

from semantic_search.models.message import Message
from semantic_search.vector_store.in_memory_store import InMemoryVectorStore

# シングルトンインスタンスを事前に作成
_vector_store_instance = InMemoryVectorStore()


def get_vector_retriever() -> VectorStoreRetriever:
    """ベクトル検索用のインスタンスを取得する"""
    return _vector_store_instance.vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 1},
    )


def run_retriever(
    message: Message,
    retriever: Annotated[VectorStoreRetriever, Depends(get_vector_retriever)],
) -> list[str]:
    """ベクトル検索を実行する"""
    result = retriever.invoke(message.prompt)
    return [content.page_content for content in result]
