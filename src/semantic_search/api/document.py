from typing import Annotated

from fastapi import APIRouter, Depends

from semantic_search.models.message import LLMResponse
from semantic_search.retriever.vector_retriever import run_retriever

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/")
def run_document_search(result: Annotated[list[str], Depends(run_retriever)]) -> LLMResponse:
    """ドキュメントの検索を実行する"""
    return LLMResponse(result=result)
